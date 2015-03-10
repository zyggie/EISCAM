#!/usr/bin/env python
import subprocess, cgitb, os
cgitb.enable()
#cmd = 'echo "python cgi win">/home/pi/EISCAM/www/hello.txt'

#subprocess.call(cmd, shell=True)
header="<header> <h1>EISCam Control</h1> </header>"
print( "Content-type: text/html\n\n")
print("<!DOCTYPE HTML>\n<title>EISCAM v-0.0.0.25</title>\n\n<html>")
print(header)
print("<p>456\n\n Python test.<br> Hello.<br></p>")

rpi_temp = 'sudo /opt/vc/bin/vcgencmd measure_temp'
#line = subprocess.check_output(rpi_temp).readline().strip()
line = os.popen(rpi_temp).readline().strip()

if "error" in line:
    print "Error ... is your firmware up-to-date? Run rpi-update"
else:
  # line now contains something like: temp=41.2'C
  # to get the temperature, split on =, and then on '

    print line
#    temp = line.split('=')[1].split("'")[0]
#    print type( temp)
    temperature_html = "<TH>Internal Temperature:</th><TD>"+ line.split("=")[1].split("'")[0] + "</TD><td>&#176;C</td>"

print(temperature_html)

print("Done.<br>")
print("</body>\n</html>")
