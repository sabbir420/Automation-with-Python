#! /usr/bin/env python3

import os
import requests

# Path to the data
path = "/data/feedback/"

keys = ["title", "name", "date", "feedback"]

folder = os.listdir(path)
for file in folder:
    keycount = 0
    fb = {}
    with open(path + file) as fl:
        for line in fl:
            value = line.strip()
            fb[keys[keycount]] = value
            keycount += 1
    print(fb)
    response = requests.post("http://<IP Address>/feedback/",
    json=fb)
print(response.request.body)
print(response.status_code)