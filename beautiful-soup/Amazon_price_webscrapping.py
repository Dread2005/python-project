from bs4 import BeautifulSoup
import requests
import smtplib
import lxml
my_email = "tshifhiwachedzafordjr@gmail.com"
password = "dytb vcdi wpwl sqqt"

amazon_price_url = ("https://www.amazon.co.za/Volkano-Bluetooth-Headphones-Hands-Free-Compatible/dp/B07H8L9RDZ?ref_=Oct_d"
                    "_obs_d_28034761031_3&pd_rd_w=AbXpG&content-id=amzn1.sym.2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_p"
                    "=2abdd2d5-c466-424f-ab98-7f9c6148446d&pf_rd_r=ZT2TYDRP28HFA5DBFMJ0&pd_rd_wg=De7fR&pd_rd_r=5f760322-"
                    "68c4-453d-8d66-886f6bec604c&pd_rd_i=B07H8L9RDZ")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "en-ZA,en-GB;q=0.9,en-US;q=0.8,en;q=0.7"
}
req_amazon = requests.get(amazon_price_url, headers=headers)
http_ = req_amazon.text

sp = BeautifulSoup(http_, features="html.parser")
product_name = sp.find(name="span", id="productTitle", class_="a-size-large product-title-word-break")
print(product_name.text)
html_price = sp.find(name="span", class_="a-price-whole")
price = html_price.getText()
price_num = int(price.split(".")[0])
print(price_num)


if price_num > 249:
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(user=my_email, password=password)
        connector.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Amazon price\n\n"
                                                                      f"went down from 249 to {str(price_num)}")

else:
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(user=my_email, password=password)
        connector.sendmail(from_addr=my_email, to_addrs=my_email, msg=f"Subject:Amazon price\n\n"
                                                                      f"NO CHANGE: {str(price_num)}")
