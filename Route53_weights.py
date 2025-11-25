import boto3
import copy
from itertools import islice

BATCH_SIZE = 100

def batch_iterable(iterable, size):
    """Split iterable into batches."""
    it = iter(iterable)
    while True:
        batch = list(islice(it, size))
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

def create_weight_changes(records, target_nlb, new_weight):
    """
    Find *all weighted records* pointing to the target NLB and update their weight.
    """
    target_nlb = target_nlb.rstrip(".").lower() + "."
    changes = []

    for record in records:
        # Consider only weighted alias records
        if "AliasTarget" in record and "Weight" in record:
            alias_dns = record["AliasTarget"]["DNSName"].rstrip(".").lower() + "."
            if alias_dns == target_nlb:
                print(f" Found weighted record: {record['Name']} (was {record['Weight']})")

                new_record = copy.deepcopy(record)
                new_record["Weight"] = int(new_weight)

                changes.append({
                    "Action": "UPSERT",
                    "ResourceRecordSet": new_record
                })

    print(f"Total records to update: {len(changes)}")
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
            print(f" Batch {i} submitted successfully: Change ID {response['ChangeInfo']['Id']}")
        except Exception as e:
            print(f" Failed to update Batch {i}: {e}")

def main():
    hosted_zone_id = "xxxxxxxxxxxxxx"  # 🔹 Replace with your hosted zone ID
    target_nlb = "xxxxxxxxxxxxxxxxxx"
    new_weight = 0  # Set all endpoints pointing to this NLB to weight 0

    print(f" Fetching all records for hosted zone {hosted_zone_id}...")
    records = fetch_all_records(hosted_zone_id)

    print(f" Creating weight updates for records pointing to NLB: {target_nlb}")
    changes = create_weight_changes(records, target_nlb, new_weight)

    if not changes:
        print("No weighted records found pointing to the given NLB.")
        return

    print(f" Updating {len(changes)} records in Route53...")
    update_route53_in_batches(changes, hosted_zone_id, BATCH_SIZE)
    print(" Weight update completed!")

if __name__ == "__main__":
    main()
