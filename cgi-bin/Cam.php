
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
<script>
		var newImage = new Image();
newImage.src = "/image.jpg";

function updateImage()
{
if(newImage.complete) {
    document.getElementById("theText").src = newImage.src;
    newImage = new Image();
    number++;
    newImage.src = "http://localhost/image/id/image.jpg?time=" + new Date();
}

    setTimeout(updateImage, 1000);
}
</script>
		<table class="status">
			<CAPTION>EISCam Camera Settings</CAPTION>
			<tr class="column-header">
				<td>ITEM</td><td>VALUE</td><td>UNIT</td><td>SET TO</td>
			</tr>
			<tr>
			   <TH>Photo Interval:</th><TD>?</TD><td>milliseconds</td><td><input id="photo_interval" type="number" min="3000" max="30000" /></td>
			</tr>
			<tr>
			   <TH>Run Time</th><TD>?</TD><td>milliseconds</td><td><input id="run_time" type="number" min="0" max="60000000" /></td>
			   <!-- Maximum run time 48 hours or max possible with memory -->
			   <!-- values changed to milliseconds for easy programming, change to reasonable units later -CN -->
			   <!-- TODO: Does it make sense to limit these? -CN -->
			</tr>
			<tr>
				<Th>Time Remaining</th><td>?</td><td>Minutes</td><td>____</td>
				<!-- Display warning when time < 60 minutes -->
                        <tr>
                           <TH>Exposure: </th><TD>?</TD><td>EV</td><td>____</td>
                        </tr>

 			<tr>
			   <TH>shutter_speed: </th><TD>fixme</TD><td>&mu;s</td><td><input id="shutter_speed" type="number" min="0" max="20" /></td><td>*note set this to 0 for automatic.</td>

			</tr>
			<tr>
			   <TH>Auto Exposure:</th><TD>?</TD><td>On/Off</td><td>____</td>
				<!-- TODO: Decide whether to manage this through setting the "shutter_speed" to zero -->
			</tr>
			<tr>
                           <TH><a href="#" onclick="alert('Hi')">Click Me</a> </th><TD>?</TD><td>ON/OFF</td><td><input type="checkbox" name="camera_settings" value="LED_status" />LED ON</td>
                        </tr>
                        <tr>
                           <TH>Include GPS? </th><TD>?</TD><td>Yes/No</td><td><input type="checkbox" name="include_GPS" value="LED_status" /></td>

                        </tr>
                          <tr>
                           <td><input type="submit" value="Snapshot test" formaction="Cam.php" class="regularbutton"  /> test</td>
                        </tr>
                       <tr>
                           <td><input type="submit" value="Start Sequence" formaction="Cam.php" class="regularbutton"  /> test</td>
                        </tr>




		</table>
	</body>
</html>

