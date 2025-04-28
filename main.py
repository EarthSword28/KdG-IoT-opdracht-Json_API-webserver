# BRONNEN
  # Oakeshott's Typology of the Medieval Sword A Summary: https://albion-swords.com/articles/oakeshott-typology.htm

  # Canvas cursus: https://canvas.kdg.be/courses/49875
  # CSS: https://www.w3schools.com/css/default.asp
  # HTML: https://www.w3schools.com/html/
  # Python Requests Module reference page: https://www.w3schools.com/python/module_requests.asp (02/04/2025)
  # Getting Started with Python HTTP Requests for REST APIs: https://www.datacamp.com/tutorial/making-http-requests-in-python (02/04/2025)
  # bepaalde delen van de text formatten: https://stackoverflow.com/questions/4622808/html-changing-colors-of-specific-words-in-a-string-of-text

DEBUG = False

def printDebug(bericht: str):
  if DEBUG == True:
    print(bericht)

import requests
from flask import Flask, render_template

app = Flask(__name__)

BASE_URL = "https://my-json-server.typicode.com/EarthSword28/KdG-IoT-opdracht-Json_API-webserver"
TYPES_URL = f"{BASE_URL}/Types"
SUB_TYPES_URL = f"{BASE_URL}/Sub-Types"

# haal de lijst op van alle beschikbare types zwaarden, en geef deze weer op de webserver
@app.route("/")
def serverMainPage():
  response = requests.get(TYPES_URL)
  response_dict = response.json()
  list_id = []
  list_type = []
  # haal de lijst van alle beschikbare types zwaarden op
  for dictionary in response_dict:
    dictionary_ID = dictionary["id"]
    dictionary_Type = dictionary["Type"]
    # check of de data correct is
    if ((type(dictionary_ID) == int) and (dictionary_ID not in list_id)) and ((type(dictionary_Type) == str) and (dictionary_Type != "")):
      list_id.append(dictionary["id"])
      list_type.append(dictionary["Type"])
  printDebug(list_id)
  printDebug(list_type)
  if (list_id != []) and (list_type != []):
    # geef de lijst van de beschikbare types zwaarden weer op de webserver
    return render_template("mainPage.html", id_list=list_id, type_list=list_type)
  else:
    # zorg ervoor dat er altijd een respons word gegeven
    return f"Geen types beschikbaar"

# geef de informatie over een bepaald type zwaard weer
@app.route("/page/<int:id>")
def serverSubPage(id):
  payload = {"id": id}  # de id van het type zwaard
  response = requests.get(TYPES_URL, params=payload).json()  # haal de informatie van het gewenste type zwaard op
  response_list = response[0]  # zet de gewenste informatie in een lijst
  printDebug(response_list)

  # initieer de lijsten met de informatie over het type zwaard
  key_list = ["id", "Type", "Profile", "Cross-section", "Average Blade Length in inches (Lower Range)", "Average Blade Length in inches (Upper Range)", "Fuller", "Point", "Grip", "Primary purpose", "Period"]
  value_list = []
  count_list = []
  # zet de informatie over het type zwaard in de lijsten met informatie
  for key in response_list:
    value_list.append(response_list[key])
    count_list.append(len(count_list))
  printDebug(value_list)
  printDebug(count_list)
  # haal de informatie over de subtypes van het zwaard op
  sub_response = requests.get(SUB_TYPES_URL, params=payload).json()
  count_response = sub_response[0]["count"]
  sub_type_list = []
  # als het zwaard subtypes heeft, sla deze informatie op
  if count_response > 0:
    sub_list = sub_response[0]["Sub-Types"]
    for item in sub_list:
      sub_type_list.append(item["Sub-Type"])
  # haal de informatie op over de algemen informatie van de beschikbare zwaarden
  id_length = requests.get(TYPES_URL).json()
  type_count = len(id_length)
  name_type = response[0]["Type"]
  printDebug(sub_type_list)
  if (value_list != []) and (count_list != []):
    # geef de beschikbare informatie over het type zwaard weer op de webserver
    return render_template("subPage.html", list_keys=key_list, list_values=value_list, list_count=count_list, sub_count=count_response, list_sub_types=sub_type_list, max_types=type_count, type_id=id, type_name=name_type)
  else:
    # zorg ervoor dat er altijd een respons word gegeven
    return f"ERROR: gegevens niet beschikbaar"

app.run(host='0.0.0.0', port=5000)      # http://localhost:5000