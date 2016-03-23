<?php
$con = mysql_connect("172.40.0.3","icesi","12345");
if (!$con)
  {
  die('Could not connect: ' . mysql_error());
  }

mysql_select_db("database1", $con);

$result = mysql_query("SELECT * FROM example");

while($row = mysql_fetch_array($result))
  {
  echo $row['name'] . " " . $row['age'];
  echo "<br />";
  }

mysql_close($con);
?>
