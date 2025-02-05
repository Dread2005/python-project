import smtplib
import datetime as dt
import random

my_email = "tshifhiwachedzafordjr@gmail.com"
password = "dytb vcdi wpwl sqqt"

date_time = dt.datetime
now_time = date_time.now()
day = now_time.weekday()

with open("Birthday Wisher (Day 32) start/quotes.txt") as quotes:
    quote = quotes.readlines()

print(day)
if day == 4:
    mot_quote = random.choice(quote)
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(user=my_email, password=password)
        connector.sendmail(my_email, "chiedzafordjr@gmail.com",
                           msg=f"Subject: Inspiration \n\n {mot_quote}")

