#! /usr/bin/env python3
import requests
import glob

url = "http://localhost/upload/"
for files in glob.glob("/home/student-04-e1a4e4b25306/supplier-data/images/*.jpeg"):
	with open(files, 'rb') as f:
		r = requests.post(url, files={'file': f}) #add images to ip_address/media/images