import requests
from flask import Flask, render_template

app = Flask(__name__)

BASE_URL = "https://my-json-server.typicode.com/EarthSword28/KdG-IoT-opdracht-Json_API-webserver"

r = requests.get((BASE_URL+"/Types"), params={"Type": "X"})

dictionary = r.json()

x = dictionary[0]["Type"]

print(r.url)