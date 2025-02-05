###API keys:
#this is like a personal account number and password, this lets the provider track how you're using their data
#and authorise your usage of their data
#api_key = "09bd9e09bb3e03215d0a2a86655e4bac"
import smtplib
import requests

email = "Tshifhiwachedzafordjr@gmail.com"
password = "dytb vcdi wpwl sqqt"

weather_endpoint = "https://api.openweathermap.org/data/2.5/forecast?"
api_key = "09bd9e09bb3e03215d0a2a86655e4bac"

weather_params = {
    "appid": api_key,
    "lat": -26.170950,
    "lon": 28.107229,
    "cnt": 4
}
current_weather_data = requests.get(weather_endpoint, params= weather_params)
current_weather_data.raise_for_status()
current_w_json = current_weather_data.json()

print(current_w_json)
#
# first_temp = current_w_json["list"][0]["main"]["temp"]
Will_rain = False
Ids = {
    "ID1": current_w_json["list"][0]["weather"][0]["id"],
    "ID2": current_w_json["list"][1]["weather"][0]["id"],
    "ID3": current_w_json["list"][2]["weather"][0]["id"],
    "ID4": current_w_json["list"][3]["weather"][0]["id"]
}
for (key, value) in Ids.items():
    if value < 700:
        Will_rain = True

if Will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(email, password)
        connector.sendmail(from_addr=email, to_addrs=email,
                           msg="Subject:Weather Status \n\n"
                               "Bring an umbrella ")
else:
    with smtplib.SMTP("smtp.gmail.com") as connector:
        connector.starttls()
        connector.login(email, password)
        connector.sendmail(from_addr=email, to_addrs=email,
                           msg="Subject:Weather Status \n\n"
                               "no need for an umbrella")


### Environment variables ###
# you can edit variables without touching code
#like changing the email_to address

# you can use these variables for security too
# it lets use separate sensitive info, like API keys from our code base
# hide api keys:export OWM_API_KEY=09bd9e09bb3e03215d0a2a86655e4bac
