#!/bin/sh
filename=$(date +"%d-%m-%y_%H%M%S-")
sudo raspistill -n -rot 180 -t 1 -o /home/pi/EISCAM/www/test.jpg
cp /home/pi/EISCAM/www/test.jpg /home/pi/EISCAM/www/photos/$filename.jpg

