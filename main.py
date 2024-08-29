import requests
import selectorlib
import smtplib, ssl
import os

URL = "https://programmer100.pythonanywhere.com/tours/"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/39.0.2171.95 Safari/537.36'}


def scrape(url):
    """Scrape the page source from the page source"""
    response = requests.get(url, headers=HEADERS)
    text = response.text
    return text


def extract(text):
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    value = extractor.extract(text)["tours"]
    return value


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "tgateley22@gmail.com"
    password = os.getenv("webcam_detect")

    receiver = "tgateley22@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


def store(extracted):
    with open("data.txt", 'a') as file:
        file.write(extracted + "\n")


def read(extracted):
    with open("data.txt", "r") as file:
        return file.read()


if __name__ == "__main__":
    scraped = scrape(URL)
    extracted = extract(scraped)
    print(extracted)
    file = read(extracted)
    if extracted != "No upcoming tours":
        if extracted not in file:
            store(extracted)
            send_email(message="New Event found")
