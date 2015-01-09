#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#use the htmltemplate.py
import htmltemplate as ht
import time
timeStr = time.strftime("%c") # obtains current time

print(ht.head+ht.title+ht.header)

print("<body>")

#form = cgi.FieldStorage()
#if "Submit1" in form:
#    button = 1
#elif "Submit2" in form:
#    button = 2
#else:
#    print "Couldn't determine which button was pressed."

#print('<input type="submit" value="Submit" name="Submit1" />')
#print('<input type="submit" value="Submit" name="Submit2" />')

#print(ht.body.substitute(dict(body_text="le body text?")))

print("<p>The current Central date and time is:  "+timeStr+"<br></p>")

print("</body>")

#print("").join(ht.body)

print(ht.footer)
