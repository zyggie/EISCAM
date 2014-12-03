#!/usr/bin/env python
import subprocess
cmd = 'echo "python cgi win">/home/pi/EISCAM/www/hello.txt'
subprocess.call(cmd, shell=True)
print "Content-type: text/html"
print ""
print ""

