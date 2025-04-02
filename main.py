# BRONNEN
  # Canvas cursus: https://canvas.kdg.be/courses/49875
  # Python Requests Module reference page: https://www.w3schools.com/python/module_requests.asp (02/04/2025)
  # Getting Started with Python HTTP Requests for REST APIs: https://www.datacamp.com/tutorial/making-http-requests-in-python (02/04/2025)

import requests
from flask import Flask, render_template

app = Flask(__name__)

BASE_URL = "https://my-json-server.typicode.com/EarthSword28/KdG-IoT-opdracht-Json_API-webserver"
TYPES_URL = "https://my-json-server.typicode.com/EarthSword28/KdG-IoT-opdracht-Json_API-webserver/Types"
SUB_TYPES_URL = "https://my-json-server.typicode.com/EarthSword28/KdG-IoT-opdracht-Json_API-webserver/Sub-Types"

@app.route("/")
def serverMainPage():
  response = requests.get(TYPES_URL)
  response_dict = response.json()
  list_type = []
  for dictionary in response_dict:
    list_type.append(dictionary["Type"])
  return render_template("mainPage.html", type_list=list_type)

app.run(host='0.0.0.0', port=5000)      # http://localhost:5000