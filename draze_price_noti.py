import requests
import smtplib
from bs4 import BeautifulSoup
import time



def check_mail():
    URL= 'https://itti.com.np/apple-m1-macbook-pro-2020-price-nepal'
    headers= {'user-agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"}
    page= requests.get(URL, headers=headers)
    soup= BeautifulSoup(page.content, "html.parser")
    title = soup.find(class_ ='page-title-wrapper product').get_text()
    price = soup.find(class_= "price").get_text()
    cp_str=price[3:].replace(',', '')
    converted_price = int(float(cp_str))
    if (converted_price>=200000):
        send_mail()
    print(title.strip())
    print(converted_price)


def send_mail():
    server= smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('your email', 'your password')
    subject='Bro Price fell down'
    body= 'check Daraz website: https://itti.com.np/apple-m1-macbook-pro-2020-price-nepal'
    msg= f"Subject:{subject}\n\n{body}"

    server.sendmail(
        'from:email',
        'to:email',
        msg
    )
    print('EMIAL HAS BEEN SEND')
    server.quit()
while True:
    check_mail()
    time.sleep(60*60*24)






