<!DOCTYPE HTML>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>EISCAM Status Menu</title>
		<link rel="stylesheet" href="/css/Zstyle1.css" type="text/css" />
	</head>
	<body>
		<header>
			<h1>EISCam Status</h1>
			<hr>
		</header>
		<table>
			<tr>
				<td>
					<form method="get" action="/Main.html">
						<input class="regularbutton" type="submit" value="Return to Main Menu" />
					</form>
				</td>
			</tr>
		</table>
		<p>
		</p>
		
		<table class="status">
			<CAPTION>EISCam Status Readings</CAPTION>
			<tr class="column-header">
				<td>ITEM</td><td>VALUE</td><td>UNIT</td>
			</tr>
			<tr>
			   <TH>Internal SoC Temperature:</th><TD><?php echo exec('sudo /home/pi/EISCAM/cgi-bin/get_temperature.sh');?></TD><td>&#176;C</td>
			</tr>
			<tr>
			   <TH>Relative Sky Irradiance:</th><TD>30</TD><td>%</td>
			</tr>
			<tr>
			   <TH>Supply Voltage: </th><TD><?php echo exec('sudo /home/pi/EISCAM/cgi-bin/get_temperature.sh');?></TD><td>Volts</td>
			</tr>
			<tr>
			   <TH>Core Voltage: </th><TD><?php echo exec('sudo /home/pi/EISCAM/cgi-bin/get_voltage.sh');?></TD><td>Volts</td>
			</tr>
			<tr>
			   <TH>IP Address: </th><TD><?php echo exec('/home/pi/EISCAM/cgi-bin/get_ip.sh');?></TD>
			</tr>
		</table>
	</body>
</html>
