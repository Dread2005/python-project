import requests
from datetime import datetime

#Types of HTTP requests
#Get (request.get()) gets information
#Post (request.post()) receives information
#Put (request.put()) updates data in external data e.g. Google sheets
#Delete (request.delete()) Delete external data

USERNAME = "dreadford2005"
TOKEN = "Dreadfordjr2005"
GRAPH_ID = "meditation71"

Pixela_endpoint = "https://pixe.la/v1/users"
# parameters = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
#             }

#############Post:
# request = requests.post(url=Pixela_endpoint, json=parameters)
# print(request.text)

# graph_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs"
# graph_parameters = {
#     "id": GRAPH_ID,
#     "name": "Meditation Tracker",
#     "type": "int",
#     "unit": "Minute",
#     "color": "shibafu"
# }

###############Header:
#used to help hide stuff
header = {
    "X-USER-TOKEN": TOKEN,
}

# graph_request = requests.post(url=graph_endpoint, json=graph_parameters, headers=graph_header)
# print(graph_request.text)
today = datetime.now()

graph_pixle_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixle_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "50",
}
# pixel_req = requests.post(url=graph_pixle_endpoint, json=pixle_params, headers=header)
# print(pixel_req.text)
date = pixle_params["date"]

############ Put:
# update_pixel_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# update_pixel = {
#     "quantity": "4"
# }
# update_req = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=header)
# print(update_req.text)

############## Delete:

# delete_endpoint = f"{Pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
# delete_req = requests.delete(url=delete_endpoint, headers=header)
# print(delete_req.text)