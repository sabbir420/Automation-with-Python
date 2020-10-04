#check website url
import re
def check_web_addr(text):
  pattern = r"[A-Za-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[A-Za-z]{2,5}?$"
  result = re.search(pattern, text)
  return result != None

print(check_web_addr("gmail.com")) # True
print(check_web_addr("www@google")) # False
print(check_web_addr("www.Coursera.org")) # True
print(check_web_addr("web-address.com/homepage")) # False
print(check_web_addr("My_Favorite-Blog.US")) # True

#Matching time format
import re
def check_time(text):
  pattern = r"^([1-9]|1[0-2]){1,2}:([0-5]|[7-9]|[1-4][0-9]|5[0-9]|[ ]){2}[a-zA-Z][ampmAMPM]"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:02am")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#matching acronym 
import re
def contains_acronym(text):
  pattern = r"\(.*?\)"
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True