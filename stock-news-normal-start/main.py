STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

[dict(source=dict(id=None, name='Investing.com'), author='Investing.com',
      title="Fed decision, megacap earnings ahead this week - what's moving markets",
      description="Fed decision, megacap earnings ahead this week - what's moving markets",
      url='https://www.investing.com/news/economy/fed-decision-megacap-earnings-ahead-this-week--whats-moving-markets-3402401',
      urlToImage='https://i-invdn-com.investing.com/news/moved_LYNXNPEK33099_L.jpg', publishedAt='2024-04-29T07:30:01Z',
      content='Investing.com --\xa0Stock futures in New York tick higher to begin a new trading week, with markets preparing for a major Federal Reserve monetary policy announcement. More megacap corporate results are… [+5459 chars]'), {'source': {'id': None, 'name': 'Marketscreener.com'}, 'author': None, 'title': 'Tesla Wins Data-Security Clearance in China', 'description': '(marketscreener.com) \n By Jiahui Huang \n\n\n Tesla has become the first foreign automaker to win approval from data-security regulators in China, which could pave the way for its vehicles to be used by the government, state-run enterprises and at military sites…', 'url': 'https://www.marketscreener.com/quote/stock/TESLA-INC-6344549/news/Tesla-Wins-Data-Security-Clearance-in-China-46561176/', 'urlToImage': 'https://www.marketscreener.com/images/reuters/2023-11-18T141510Z_1_LYNXMPEJAH05D_RTROPTP_3_TOTW-EV-BRANDS.JPG', 'publishedAt': '2024-04-29T07:26:19Z', 'content': 'By Jiahui Huang \r\nTesla has become the first foreign automaker to win approval from data-security regulators in China, which could pave the way for its vehicles to be used by the government, state-ru… [+1540 chars]'}, {'source': {'id': None, 'name': 'Marketscreener.com'}, 'author': None, 'title': 'News Highlights: Top Company News of the Day - Monday at 3 AM ET', 'description': '(marketscreener.com) \nTesla Wins China\'s Backing for Driver-Assistance Service \n \n\n Tentative approval for the "Full Self-Driving" software feature follows Elon Musk\'s unannounced visit to Beijing and a meeting with the Chinese premier. \n\n \nPhilips Settles U.…', 'url': 'https://www.marketscreener.com/quote/stock/TPG-TELECOM-LIMITED-111315528/news/News-Highlights-Top-Company-News-of-the-Day-Monday-at-3-AM-ET-46561107/', 'urlToImage': 'https://www.marketscreener.com/images/twitter_MS_fdblanc.png', 'publishedAt': '2024-04-29T07:16:43Z', 'content': 'Tesla Wins China\'s Backing for Driver-Assistance Service \r\nTentative approval for the "Full Self-Driving" software feature follows Elon Musk\'s unannounced visit to Beijing and a meeting with the Chin… [+2008 chars]'}]
