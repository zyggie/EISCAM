#!/usr/bin/env python
# -*- coding: UTF-8 -*-
from string import Template		#https://docs.python.org/2/howto/webservers.html
#body = Template("<body>${name}</body>")
#>>> print template.substitute(dict(name='Dinsdale'))
#<html><body><h1>Hello Dinsdale!</h1></body></html>

#Content-Type: text/plain;charset=utf-8
head = "Content-type: text/html\n\n<!DOCTYPE HTML>\n\n"
header = "<header>This is a header<br></header>\n"
footer = "<footer>This is a footer<br></footer>\n"
body = Template("<body>${body_text}</body>")

#body = ["<body>","This is the body<br>","</body>\n"]
#print("").join(ht.body) #this syntax works but is too ugly

title = "<title>EISCAM pythonified test title EISCAM v-0.0.0.25<br></title>\n"

