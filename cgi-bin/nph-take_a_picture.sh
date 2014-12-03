#!/bin/sh
filename=$(date +"%d-%m-%y_%H%M%S-")
echo -e "Content-type: text/html\n\n"
echo "<h1>Taking photo...</h1>"
sudo raspistill -n -rot 180 -o /home/pi/EISCAM/www/photos/$filename%04d.jpg
cp /home/pi/EISCAM/www/photos/$filename%04d.jpg /home/pi/EISCAM/www/test.jpg
echo "Location: response.html"



