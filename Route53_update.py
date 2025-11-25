import boto3
from itertools import islice
import copy
from hosted_zones_NLB_xconf import HOSTED_ZONES
# ===== CONFIG =====
BATCH_SIZE = 100  # Adjust as needed (100-1000)


# ===== FUNCTIONS ====

def load_hosted_zones():
    with open(config_file, "r") as f:
        return json.load(f)


def batch_iterable(iterable, size):
    """Split iterable into batches."""
    it = iter(iterable)
    while True:
        batch = list(islice(it, size))
        print(batch)
        if not batch:
            break
        yield batch

def fetch_all_records(hosted_zone_id):
    """Fetch all records from Route53 hosted zone."""
    route53 = boto3.client("route53")
    records = []
    paginator = route53.get_paginator("list_resource_record_sets")
    for page in paginator.paginate(HostedZoneId=hosted_zone_id):
        records.extend(page["ResourceRecordSets"])
    return records




def create_changes(records, old_dns, new_dns):
    changes = []
    old_dns = old_dns.rstrip(".").lower() + "."
    new_dns = new_dns.rstrip(".") + "."
    for record in records:
        changed = False
        new_record = copy.deepcopy(record)

        # Handle ResourceRecords
        #if "ResourceRecords" in record:
        #    new_values = []
        #    for rr in record["ResourceRecords"]:
        #        rr_value = rr["Value"].rstrip(".").lower() + "."
        #        #print(f"Checking: {rr_value} vs {old_dns}")
        #        if rr_value == old_dns:
        #            new_values.append({"Value": new_dns})
        #            changed = True
        #        else:
        #            new_values.append(rr)
        #    new_record["ResourceRecords"] = new_values

        # Handle AliasTarget
        if "AliasTarget" in record:
            dns_name = record["AliasTarget"]["DNSName"].rstrip(".").lower() + "."
            #print(f"Alias check: {dns_name} vs {old_dns}")
            if dns_name == old_dns:
                alias_copy = record["AliasTarget"].copy()
                alias_copy["DNSName"] = new_dns
                new_record["AliasTarget"] = alias_copy
                changed = True

        if changed:
            #print(f"→ Updating record: {record['Name']}")
            changes.append({
                "Action": "UPSERT",
                "ResourceRecordSet": new_record
            })

    return changes

def update_route53_in_batches(changes, hosted_zone_id, batch_size):
    """Send batches of changes to Route53."""
    route53 = boto3.client("route53")
    for i, batch in enumerate(batch_iterable(changes, batch_size), start=1):
        print(f"[Batch {i}] Updating {len(batch)} records...")
        try:
            response = route53.change_resource_record_sets(
                HostedZoneId=hosted_zone_id,
                ChangeBatch={"Changes": batch}
            )
            print(f"Batch {i} submitted successfully: Change ID {response['ChangeInfo']['Id']}")
        except Exception as e:
            print(f"Error in batch {i}: {e}")

# ===== MAIN =====

if __name__ == "__main__":
    for HOSTED_ZONE_ID, nlb_pairs in HOSTED_ZONES.items():
        print(f"\n🔹 Processing Hosted Zone: {HOSTED_ZONE_ID}")
    
        all_records = fetch_all_records(HOSTED_ZONE_ID)
        print(f"Fetched {len(all_records)} records from zone {HOSTED_ZONE_ID}")

        for OLD_NLB_DNS, NEW_NLB_DNS in nlb_pairs:
            print(f"\n  ➤ Old NLB: {OLD_NLB_DNS}")
            print(f"  ➤ New NLB: {NEW_NLB_DNS}")

            changes = create_changes(all_records, OLD_NLB_DNS, NEW_NLB_DNS)
            print(f"  Found {len(changes)} changes for this mapping")

            if changes:
                print("Updating Route53 in batches...")
                update_route53_in_batches(changes, HOSTED_ZONE_ID, BATCH_SIZE)
            else:
                print("No changes found. Exiting.")

