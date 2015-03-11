#!/bin/bash
#http://developer-blog.net/en/hardware-2/get-temperature-of-your-raspberry-pi/
tm=`/opt/vc/bin/vcgencmd measure_temp`
tc=`echo $tm| cut -d '=' -f2 | sed 's/..$//'`
#tf=$(echo "scale=2;((9/5) * $tc) + 32" |bc)
#echo temp = $tc\°C \($tf\°F\)
echo $tc
