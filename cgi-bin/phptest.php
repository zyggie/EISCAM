<html>
<head>
	<title>PHP Status Page</title>
	<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
</head>
<body>
	<h1>PHP Status Page</h1>
	<p>
	<b></b><br />
		<?php echo "The Current Date and Time is: ";
			echo date("g:i A l, F j Y.");?>;<br>
		<?php echo "Uptime: ";
			echo `uptime`;?><br>
		<?php echo "test: ";  
                        echo $EISCAM_STARBOARD;?><br>

	</p>

	<h2>PHP Information</h2>
	<p>
		<?php phpinfo(); ?>
	</p>
</body>
</html>

