<?php
$localIp = $_SERVER['SERVER_ADDR'];
$publicIpCmd = escapeshellcmd("ec2-metadata -v");
$publicIp = shell_exec($publicIpCmd);
?>

<!DOCTYPE html>
<html>
<head>
    <title>CCTB Digital Party Planner</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f8fb;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .checkbox-list {
            background-color: #fff;
            border: 1px solid #ddd;
            padding: 20px;
            width: fit-content;
            border-radius: 10px;
        }
        .checkbox-list label {
            display: block;
            margin-bottom: 8px;
            font-size: 16px;
        }
        .submit-btn {
            margin-top: 15px;
            padding: 10px 20px;
            font-size: 16px;
        }
    </style>
</head>
<body>

<h1>🎈 CCTB Digital Party Planner - Server 1 🎈</h1>
<h2>This server is hosted at: <?php echo $publicIp; ?></h2>
<p>Select your essential party items:</p>

<form action="process.php" method="post" class="checkbox-list">
    <label><input type="checkbox" name="party_items[]" value="20"> 0: Cake 🎂</label>
    <label><input type="checkbox" name="party_items[]" value="21"> 1: Balloons 🎈</label>
    <label><input type="checkbox" name="party_items[]" value="10"> 2: Music System 🎶</label>
    <label><input type="checkbox" name="party_items[]" value="5"> 3: Lights 💡</label>
    <label><input type="checkbox" name="party_items[]" value="8"> 4: Catering Service 🍕</label>
    <label><input type="checkbox" name="party_items[]" value="3"> 5: DJ 🎧</label>
    <label><input type="checkbox" name="party_items[]" value="15"> 6: Photo Booth 📸</label>
    <label><input type="checkbox" name="party_items[]" value="7"> 7: Tables 🪑</label>
    <label><input type="checkbox" name="party_items[]" value="12"> 8: Chairs 🪑</label>
    <label><input type="checkbox" name="party_items[]" value="6"> 9: Drinks 🥤</label>
    <label><input type="checkbox" name="party_items[]" value="9"> 10: Party Hats 🎩</label>
    <label><input type="checkbox" name="party_items[]" value="18"> 11: Streamers 🎊</label>
    <label><input type="checkbox" name="party_items[]" value="4"> 12: Invitation Cards ✉️</label>
    <label><input type="checkbox" name="party_items[]" value="2"> 13: Party Games 🎲</label>
    <label><input type="checkbox" name="party_items[]" value="11"> 14: Cleaning Service 🧼</label>

    <input class="submit-btn" type="submit" value="Plan My Party 🎉">
</form>

</body>
</html>