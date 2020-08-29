#!/usr/bin/env python3

import socket
import shutil
import psutil
import emails

#send email if a error occurs
def error_mail(subject_line):
    sender = "automation@example.com"
    recipient = "student-03-562c2b1ab9c3@example.com"
    subject = subject_line
    body = "Please check your system and resolve the issue as soon as possible."

    msg = emails.generate_error_report(sender, recipient, subject, body) #create a instance of generate_error_report method from emails.py
    emails.send_email(msg) #send email to the recipient using the send_email method from emails.py

#----------------------------------------------------------------------------------------------

#checking for free space in disk
def check_disk_usage():
    du = shutil.disk_usage("/")
    free_percent = du.free/du.total*100
    if free_percent < 20:
        subject_line = "Error - Available disk space is less than 20%"
        error_mail(subject_line)

#check for cpu usage for 1 second
def check_cpu_percent():
    usage = psutil.cpu_percent(1)
    if usage > 80:
        subject_line = "Error - CPU usage is over 80%"
        error_mail(subject_line)

#check for Available RAM
def check_RAM_mem():
    RAM_data = psutil.virtual_memory()
    avail_mem = int(RAM_data.available//1024**2)
    if avail_mem < 500:
        subject_line = "Error - Available memory is less than 500MB"
        error_mail(subject_line)

#check for "localhost" ip address resolved to "127.0.01"
def check_ip():
    ip_addr = socket.gethostbyname("localhost")
    if ip_addr != "127.0.0.1":
        subject_line = "Error - localhost cannot be resolved to 127.0.0.1"
        error_mail(subject_line)

if __name__ == "__main__":
    #call all the defined functions
    check_disk_usage()
    check_cpu_percent()
    check_RAM_mem()
    check_ip()