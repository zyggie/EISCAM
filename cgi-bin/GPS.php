<!DOCTYPE HTML>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<title>EISCAM Camera Menu</title>
		<link rel="stylesheet" href="/css/Zstyle1.css" type="text/css" />
	</head>
	<body>
		<header>
			<h1>EISCam Camera</h1>
			<hr>
		</header>
		<table class="fixed">
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
			<CAPTION>EISCam GPS & Inclinometer Status</CAPTION>
			<tr class="column-header">
				<td>ITEM</td><td>VALUE</td><td>UNIT</td><td>SET TO</td>
			</tr>
			<tr>
			   <TH>Photo Interval:</th><TD>?</TD><td>Seconds</td><td><input id="photo_interval" type="number" min="3" max="30" /></td>
			</tr>
			<tr>
			   <TH>Run Time</th><TD>?</TD><td>Minutes</td><td><input id="run_time" type="number" min="0" max="1440" /></td>
			   <!-- Maximum run time 48 hours or max possible with memory -->
			   <!-- values 0 and 1440 are chosen arbitrarily -CN -->
			   <!-- TODO: Does it make sense to limit these? -CN -->
			</tr>
			<tr>
				<Th>Time Remaining</th><td>?</td><td>Minutes</td><td>____</td>
				<!-- Display warning when time < 60 minutes -->
                        <tr>
                           <TH>Exposure: </th><TD>?</TD><td>EV</td><td>____</td>
                        </tr>

 			<tr>
			   <TH>Starboard? </th><TD><?php getenv ( string 'EISCAM_STARBOARD' )?></TD><td>&mu;s</td><td></td><td></td>

			</tr>
			<tr>
			   <TH>Auto Exposure:</th><TD>?</TD><td>On/Off</td><td>____</td>
				<!-- TODO: Decide whether to manage this through setting the "shutter_speed" to zero -->
			</tr>
			<tr>
                           <TH>LED: </th><TD>?</TD><td>ON/OFF</td><td><input type="checkbox" name="camera_settings" value="LED_status" />LED ON</td>
                        </tr>


		</table>
	</body>
</html>
