#!/usr/bin/env python
import cgi
import cgitb
cgitb.enable()
cgitb.enable(display=0, logdir="~/EISCAM/www/logs/")
print ("Content-type: text/html\n\n")
print ("<h1>Hello World from Python</h1>")
print(exec('python --version')) 
