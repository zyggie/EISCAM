#!/usr/bin/env python
import cgi
import cgitb
import sys, os, time, datetime
import subprocess
import signal
from time import sleep
#import picamera
#camera = picamera.PiCamera()
#camera.capture('/home/pi/EISCAM/www/test.jpg')

# enable tracebacks of exceptions
cgitb.enable()

# print an HTTP header
#
def printHTTPheader():
    print "Content-type: text/html"
    print ""
    print ""


def main():

#    cmd = ('raspistill -t ' + str(tltime) + " -tl " + str(tlfreq) + " -o " + dir + "/photo_%04d.jpg")
#http://www.pythoneye.com/652_18842787/
#    cmd='sudo raspistill -t 2 -o /home/pi/EISCAM/www/test.jpg'
#    cmd='echo "hello">/home/pi/EISCAM/www/hello.txt'
#     subprocess.call(cmd, shell=True)
    subprocess.call("sudo /home/pi/EISCAM/cgi-bin/take_a_picture.sh", shell=True)
    printHTTPheader()

    # this string contains the web page that will be served
    page_str=""" <DOCTYPE html>
    <head>    
    <meta charset="utf-8" />
    <title>EISCAM Test - Snapshot</title>
    <link rel="shortcut icon" href="/favicon.ico" />
    <link rel="stylesheet" type="text/css" href="/css/SampleStyle.css">
    </head>"
    <body>
    <FORM METHOD="POST" ACTION="chart.py"> 
    <button type="submit" name="Snap" value="Snap_btn_was_clicked" action="chart.py" method="post"> 
    <img src="/test.jpg" width="800em" height="600em" id="Snap"
    <p> <br><br>Snap a New Photo</p>
    </button>
    </FORM>
    <br>
    <a href="/index.html"> EISCAM Test - Home</a>
    </body>
    </html>
    """ 
    # serve the page with the data table embedded in it
    print page_str

if __name__=="__main__":
    main()
