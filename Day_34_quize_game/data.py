import requests
import html

question_data1 = requests.get("https://opentdb.com/api.php?amount=10&difficulty=medium&type=boolean")
question_data1.raise_for_status()
question_json = question_data1.json()
questions = question_json["results"]



