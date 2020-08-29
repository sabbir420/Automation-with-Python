#!/usr/bin/env python3

import os
from datetime import date
import reports
import emails
import glob

date = date.today() #fetching the present date from datetime module
title = "Processed Update on {}".format(date.strftime("%B %d, %Y")) #PDF title

text_files = glob.glob("/home/student-04-e1a4e4b25306/supplier-data/descriptions/*.txt")
txt_list = []
#parsing through all the text files in descriptions direcrtory
for files in text_files:
	with  open(files,"r") as f:
        reader = f.read().split("\n")
        txt_list.append(reader) #making a list of lists from the text data

#fetching the body of the PDF from the txt_list

para_g = ""
for fields in txt_list:
    mesg = ""
    mesg = "Name: {}<br/> Weight: {}<br/><br/>".format(fields[0],fields[1])
    para_g = para_g + mesg

if __name__ == "__main__":
    #assigning all the values required for sending mail
    sender = "automation@example.com"
    recipient = "student-04-e1a4e4b25306@example.com"
    subject = " Upload Completed - Online Fruit Store "
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    attachment_path = "/tmp/processed.pdf"

    reports.generate_report("/tmp/processed.pdf",title,para_g)  #generate pdf file by calling generate_report from reports.py
    msg = emails.generate_email(sender, recipient, subject, body, attachment_path) #create a instance of generate_email method from emails.py
    emails.send_email(msg) #send email to the recipient using the send_email method from emails.py