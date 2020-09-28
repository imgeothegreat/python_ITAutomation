#!/usr/bin/env python3

import os
import datetime
import reports
import emails

BASEPATH = "supplier-data/descriptions/"
folder = os.listdir(BASEPATH)

#attachment
attachment_path = "/tmp/processed.pdf"
#datetime
date = datetime.datetime.now()
#title
title = "Processed Update on " + str(date.month) + "-" +  str(date.day) + "-"  + str(date.year)
#paragraph
paragraph = []

for file in folder:
    with open(BASEPATH+file, 'r') as f:
        name = f.readline().rstrip("\n")
        weight = f.readline().rstrip("\n")
        description = f.readline().rstrip("\n")

        space = "\n"
        list = "name: {} ".format(name)
        list2 =  "weight: {}".format(weight)

    paragraph.append(space)
    paragraph.append(list)
    paragraph.append(list2)

print(paragraph)
if __name__ == "__main__":
  reports.generate_report(attachment_path,title,paragraph)
  sender="automation@example.com"
  recipient="student-02-6957bf8c40e2@example.com"
  subject="Upload Completed - Online Fruit Store"
  body="All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  message = emails.generate_email(sender,recipient,subject,body,attachment_path)
  emails.send_email(sender,message)
