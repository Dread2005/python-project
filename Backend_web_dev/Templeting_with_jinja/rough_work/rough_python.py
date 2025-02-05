import requests

my_name = {
    "name": input("Enter name: ")
              }
age_response = requests.get("https://api.agify.io?", params=my_name)
age_json = age_response.json()
age = age_json["age"]
#print(age)

sexuality_response = requests.get("https://api.genderize.io?", params=my_name)
sexuality_json = sexuality_response.json()
gender_guesser = sexuality_json["gender"]
probability_counter = sexuality_json["probability"]
print(f"age:{age}, Gender:{gender_guesser}, gender_probability:{probability_counter}")