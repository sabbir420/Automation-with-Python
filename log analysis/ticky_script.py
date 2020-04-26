#!/usr/bin/env python3

import re
import sys
import csv
import os
import operator

error_messages = {}
per_user = {}
log_file = sys.argv[1]

def create_dictionary(log_file):
  with open(log_file, mode='r',encoding='UTF-8') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", line)
      if result is None:
        return None
      if result[2] not in error_messages.keys():
          error_messages[result[2]] = 0
      else:
        error_messages[result[2]] += 1
      if result[3] not in per_user.keys():
        per_user[result[3]] = {}
        per_user[result[3]]["INFO"] = 0
        per_user[result[3]]["ERROR"] = 0       
      if result[1] == "INFO":
        per_user[result[3]]["INFO"] += 1
      else:
        per_user[result[3]]["ERROR"] += 1   
  file.close()   
  return error_messages, per_user

def create_csv_files():
  dictionary = create_dictionary(log_file)
  error_dictionary = dictionary[0]
  user_dictionary = dictionary[1]
  error_dictionary = sorted(error_dictionary.items(), key = operator.itemgetter(1), reverse = True)
  user_dictionary = sorted(user_dictionary.items())

  with open("error_message.csv", 'w') as file:
    file.write("Error,Count\n")
    for error in error_dictionary:
      a,b = error
      file.write(str(a)+','+str(b)+'\n')
  file.close()

  with open("user_statistics.csv", 'w') as file:
    file.write("Username,INFO,ERROR\n")
    for stats in user_dictionary:
      a, b = stats
      file.write(str(a)+','+str(b["INFO"])+','+str(b["ERROR"])+'\n')
  file.close()

if __name__ == '__main__':
  create_csv_files()