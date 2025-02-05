import requests
import smtplib

my_email = "tshifhiwachedzafordjr@gmail.com"
password = "dytb vcdi wpwl sqqt"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

stock_api_key = " SC4BSAPYHGSH2MKE"
stocks_data_endpoint = "https://www.alphavantage.co/query?"

function = "TIME_SERIES_DAILY"

stock_data_params = {
    "function": function,
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": stock_api_key
}

news_endpont = "https://newsapi.org/v2/top-headlines?"
news_api_key = "e668fa751d124c22952f1845c34ca406"
company = "tesla"

news_param = {
    "q": company,
    "page": 1,
    "pageSize": 3,
    "apiKey": news_api_key,
    "country": "us"

}

stock_data_req = requests.get(url=stocks_data_endpoint, params=stock_data_params)
stock_data_req.raise_for_status()
stock_data_json = stock_data_req.json()

close_price = stock_data_json["Time Series (Daily)"]

data_list = [value for (key, value) in close_price.items()]

Yesterday_stock_close_price = abs(float(data_list[0]["4. close"]))
Day_before_stock_close_price = abs(float(data_list[1]["4. close"]))

Percent_difference = (Yesterday_stock_close_price / Day_before_stock_close_price) * 100
print(Percent_difference)

if Percent_difference <= 98:
    news_req = requests.get(url=news_endpont, params=news_param)
    news_req.raise_for_status()
    news_json = news_req.json()
    article = news_json["articles"][0]["title"]
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(user=my_email, password=password)
        connector.sendmail(to_addrs=my_email, from_addr=my_email,
                           msg=f"Subject:Went Down \n\n Brief: {article}")
if Percent_difference >= 105:
    news_req = requests.get(url=news_endpont, params=news_param)
    news_req.raise_for_status()
    news_json = news_req.json()
    article = news_json["articles"][0]["title"]
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(user=my_email, password=password)
        connector.sendmail(to_addrs=my_email, from_addr=my_email,
                           msg=f"Subject:Went UP \n\n Brif: {article}")



# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
