<?php
$partyItems = $_POST['party_items'];

$publicIpcmd = escapeshellcmd("ec2-metadata -v");
$publicIp = shell_exec($publicIpcmd);

$partyItemCsv = implode(",", $partyItems);
$command = escapeshellcmd("python3 party_planner.py $partyItemCsv");

$output = shell_exec($command);
$host = escapeShellarg($_SERVER['HTTP_HOST']);

echo "$output";
?>

<h2>This result was processed on my EC2 instance with Public IP: <?php echo $publicIp; ?></h2>
<h2>Access the application via Load Balancer URL: http://<?php echo $host; ?>/party_form.php</h2>
