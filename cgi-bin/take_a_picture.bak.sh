#!/bin/sh
filename=$(date +"%d-%m-%y_%H%M%S-")
sudo raspistill -n -rot 180 -o /home/pi/EISCAM/www/photos/$filename%04d.jpg

