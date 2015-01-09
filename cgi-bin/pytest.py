#!/usr/bin/env python
import subprocess, cgitb	#, os
cgitb.enable()
#cmd = 'echo "python cgi win">/home/pi/EISCAM/www/hello.txt'

#subprocess.call(cmd, shell=True)
header="<header> <h1>EISCam Control</h1> </header>"
print( "Content-type: text/html\n\n")
print("<!DOCTYPE HTML>\n<title>EISCAM v-0.0.0.25</title>\n\n<html>")
print(header)
print("<p>456\n\n Python test.<br> Hello.<br></p>")
ppp=subprocess.check_output('date')
print(ppp+"<br>")
ppp2=subprocess.check_output(["python", "--version"])
print (ppp2)
print("Done.<br>")
print("</body>\n</html>")
