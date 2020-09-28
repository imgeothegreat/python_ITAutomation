#! /usr/bin/env python3

import psutil
import shutil
import socket
import emails

cpu_usage = psutil.cpu_percent(0.1)
disk_space = psutil.disk_usage('/')
memory = psutil.virtual_memory()
hostname = "localhost"
hostname_check = False
hostname_value =socket.gethostbyname(hostname)

free_disk = 100 - disk_space[3]
free_memory = int(memory[1] / (1024*1024))

#email infos
sender = "automation@example.com"
recipient = "student-00-1d7bc0b92d3f@example.com"
subject = ""
body = "Please check your system and resolve the issue as soon as possible."

def send_error():
    message = emails.error_email(sender,recipient,subject,body)
    emails.send_email(sender,message)

if(cpu_usage>80):
    subject = "Error - CPU usage is over 80%"
    send_error()

if(free_disk < 20):
    subject = "Error - Available disk space is less than 20%"
    send_error()

if(free_memory < 500):
    subject = "Error - Available memory is less than 500MB"
    send_error()

if hostname_value != "127.0.0.1":
    subject = "Error - localhost cannot be resolved to 127.0.0.1"
    send_error()
