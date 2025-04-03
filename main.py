# BRONNEN
  # Oakeshott's Typology of the Medieval Sword A Summary: https://albion-swords.com/articles/oakeshott-typology.htm

  # Canvas cursus: https://canvas.kdg.be/courses/49875
  # CSS: https://www.w3schools.com/css/default.asp
  # Python Requests Module reference page: https://www.w3schools.com/python/module_requests.asp (02/04/2025)
  # Getting Started with Python HTTP Requests for REST APIs: https://www.datacamp.com/tutorial/making-http-requests-in-python (02/04/2025)
  # bepaalde delen van de text formatten: https://stackoverflow.com/questions/4622808/html-changing-colors-of-specific-words-in-a-string-of-text

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
  list_id = []
  list_type = []
  for dictionary in response_dict:
    list_id.append(dictionary["id"])
    list_type.append(dictionary["Type"])
  return render_template("mainPage.html", id_list=list_id, type_list=list_type)

@app.route("/page/<int:id>")
def serverSubPage(id):
  payload = {"id": id}
  response = requests.get(TYPES_URL, params=payload).json()
  response_list = response[0]
  print(response_list)
  key_list = ["id", "Type", "Profile", "Cross-section", "Average Blade Length in inches (Lower Range)", "Average Blade Length in inches (Upper Range)", "Fuller", "Point", "Grip", "Primary purpose", "Period"]
  value_list = []
  count_list = []
  for key in response_list:
    value_list.append(response_list[key])
    count_list.append(len(count_list))
  print(value_list)
  print(count_list)
  sub_response = requests.get(SUB_TYPES_URL, params=payload).json()
  count_response = sub_response[0]["count"]
  sub_type_list = []
  if count_response > 0:
    sub_list = sub_response[0]["Sub-Types"]
    for item in sub_list:
      sub_type_list.append(item["Sub-Type"])
  id_length = requests.get(TYPES_URL).json()
  type_count = len(id_length)
  name_type = response[0]["Type"]
  print(sub_type_list)
  return render_template("subPage.html", list_keys=key_list, list_values=value_list, list_count=count_list, sub_count=count_response, list_sub_types=sub_type_list, max_types=type_count, type_id=id, type_name=name_type)

app.run(host='0.0.0.0', port=5000)      # http://localhost:5000