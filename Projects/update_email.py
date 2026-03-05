import requests
import smtplib, ssl
def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "hkaranam241@gmail.com"
    password = "jlxl bxyr glgo waho"

    receiver = "hkkaranam@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

api_key="5ee054ba41eb4a968f618f8e3eb82d60"
url="https://newsapi.org/v2/everything?q=tesla&from=2026-02-05&sortBy=publishedAt&apiKey=5ee054ba41eb4a968f618f8e3eb82d60&language=en"
reponse=requests.get(url)
content=reponse.json()
body=""
for article in content["articles"][:20]:
    if (article["title"] and article["description"]) is not None:
        body= body + article["title"] \
        + "\n" + article["description"] \
        + "\n" + article["url"]+ 2*"\n"
body="subject: Todays News\n"+ body
body=body.encode("utf-8")
send_email(message=body)
