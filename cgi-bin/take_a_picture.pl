#!/usr/bin/perl
#filename=$(date +"%d-%m-%y_%H%M%S-")
#sudo raspistill -n -rot 180 -o /home/pi/EISCAM/www/photos/$filename%04d.jpg
#cp /home/pi/EISCAM/www/photos/$filename%04d.jpg /home/pi/EISCAM/www/test.jpg
print "Content-type: text/html\n\n"

print "<!DOCTYPE html>"
print "<head>    <meta charset="utf-8" />    <title>Put Page Title Here</title>    <link rel="stylesheet" href="css/SampleStyle.css" /><link rel="shortcut icon" href="/favicon.ico" /></head>"
print "<body><FORM METHOD="POST" ACTION="cgi-bin/take_a_picture.sh"> <button type="submit" name="Snap" value="Snap_btn_was_clicked" action="cgi-bin/take_a_picture.py" method="post">        <p>  Snap a New Photo</p> 	<img src="/test.jpg" width="600em" height="450em" id="Snap" />        </button>        </FORM></body>"
print "</html>"

