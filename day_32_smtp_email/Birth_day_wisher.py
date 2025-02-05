##################### Normal Starting Project ######################
import datetime as dt
import random
import smtplib

import pandas
my_email = "tshifhiwachedzafordjr@gmail.com"
password = "dytb vcdi wpwl sqqt"

date = dt.datetime
current_date = date.now()
today = (current_date.month, current_date.day)

data = pandas.read_csv("birthdays.csv")

# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
birthdays_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}
if today in birthdays_dic:
    bday_person = birthdays_dic[today]
    letter = random.randint(1, 3)
    with open(f"letter_templates/letter_{letter}.txt") as bday_letter:
        nm_replace = bday_letter.read()
        name = bday_person["name"]
        #print(name)
        the_letter = nm_replace.replace("[NAME]", name)
        the_letter2 = the_letter.replace("Angela", "Chiyedza")
        print(the_letter2)
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(user=my_email, password=password)
        connector.sendmail(from_addr=my_email, to_addrs="Midziwellness@gmail.com",
                           msg=f"Subject:Happy Birthday\n\n"
                               f"{the_letter2}")







