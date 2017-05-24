<?php
$file = $_POST['file'];
if (file_exists($file)){
unlink($file);
echo 'File '.$file.' has been deleted';
} else {
echo 'ERROR: Could not delete '.$file. '.';
}
?>
