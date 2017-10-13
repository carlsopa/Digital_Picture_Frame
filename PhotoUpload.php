<html>
  <head>
    <title></title>
  </head>
  <body>
    <form method = "post" enctype="multipart/form-data">
      <input type="file" name="my_file[]" multiple>
      <input type="submit" value="upload">
      <input type="button" value="Cancel" onclick="window.open('index.html')">
    </form>
    <?php
      $tmp_name_array = $_FILES['my_file']['tmp_name'];
      $target_dir = "uploads/";
      if (isset($_FILES['my_file'])) {
        $myFile = $_FILES['my_file'];
        $fileCount = count($myFile["name"]);
        echo "Total files: " . $fileCount + 1 . "<br>";
        for ($i = 0; $i < $fileCount; $i++) {
        $Name = $myFile["name"][$i];
    ?>
    <p>File #<?= $i + 1 ?>:</p>
    <p>
    Name: <?= $Name ?><br>
    Type: <?= $myFile["type"][$i] ?><br>
    Size: <?= $myFile["size"][$i] ?><br>
    Temp Name: <?= $tmp_name_array[$i]?><br>
    Location: <?= $target_dir ?><br>
    <?php $target_file = $target_dir . $myFile["name"][$i]; ?>
    Target: <?= $target_file ?><br>
    <?php
      if (move_uploaded_file($tmp_name_array[$i], $target_file)) {
        echo "the file: " . $myFile["name"][$i] . " has been uploaded.<br>";
        } else {
          echo "This is a failure<br>";
        }
    ?>        
    </p>
    <?php    
      }
    } 
    ?>
  </body>
</html>
