#!/bin/bash
echo -e "Content-type: text/html\n\n"
echo '<!DOCTYPE HTML>'
echo '<html lang="en">'
echo "<h1>Hello World from a shell script</h1>"
echo "<head><meta charset=\"utf-8\"><title>EISCAM Status Menu</title><link rel=\"stylesheet\" href=\"/css/Zstyle1.css\" type=\"text/css\" /></head>"
echo '<body><header><h1>EISCam Status</h1><hr></header>'
echo '		<table>'
echo '			<tr>'
echo '				<td>'
echo '					<form method="get" action="Main.html">'
echo '						<input class="regularbutton" type="submit" value="Return to Main Menu" />'
echo '					</form>'
echo '				</td>'
echo '			</tr>'
echo '		</table>'
echo '		<p>'
echo '		</p>'
echo '		<table class="status">'
echo '			<CAPTION>EISCam Status Readings</CAPTION>'
echo '			<tr class="column-header">'
echo '				<td>ITEM</td><td>VALUE</td><td>UNIT</td>'
echo '			</tr>'
echo '			<tr>'
echo '			   <TH>Internal Temperature:</th><TD>'
echo `/home/pi/bin/get_temperature.sh`
echo '			</TD><td>&#176;C</td>'
echo '			</tr>'
echo '			<tr>'
echo '			   <TH>Relative Sky Irradiance:</th><TD>30</TD><td>%</td>'
echo '			</tr>'
echo '			<tr>'
echo '			   <TH>Supply Voltage: </th><TD>42</TD><td>Volts</td>'
echo '			</tr>'
echo '			<tr>'
echo '			   <TH>Regulated Voltage: </th><TD>5.02</TD><td>Volts</td>'
echo '			</tr>'
echo '			<tr>'
echo '			   <TH>IP Address: </th>'
echo `/home/pi/EISCAM/cgi-bin/get_ip.sh`
echo '				</TD>'
echo '			</tr>'
echo '		</table>'
echo '	</body>'
echo '</html>'

