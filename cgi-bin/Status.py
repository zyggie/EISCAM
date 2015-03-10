#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import os
# enable debugging
import cgitb
cgitb.enable()

print ("Content-Type: text/plain;charset=utf-8")

#print ("Hello World!")
rpi_temp = 'sudo /opt/vc/bin/vcgencmd measure_temp'
line = os.popen(rpi_temp).readline().strip()

rpi_volts = '/opt/vc/bin/vcgencmd measure_volts core'
rpi_clock = '/opt/vc/bin/vcgencmd measure_clock arm'

#frequency(45)=700074000

if "error" in line:
    print "Error ... is your firmware up-to-date? Run rpi-update"
else:
  # line now contains something like: temp=41.2'C
  # to get the temperature, split on =, and then on '


    temp = line.split('=')[1].split("'")[0]

temperature_html = "<TH>Internal Temperature:</th><TD>"+ str(temp)+"</TD><td>&#176;C</td>"


if __name__=='__main__':
    print(temperature_html)
