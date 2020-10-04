
#!/usr/bin/env python3

from PIL import Image
import os

def convert(file):
  dest = "/home/shossain/" + file
  src = os.getcwd() + "/images/" + file
  im = Image.open(src)
  im.rotate(90).resize((128, 128)).convert('RGB').save(dest, 'JPEG')

if __name__ == "__main__":
  file_list = os.listdir(os.getcwd() + "/images/")
  for file in file_list:
    convert(file)
