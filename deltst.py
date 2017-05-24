<?php
if(is_file('Frame/Photos/2012-10-14 14.50.30.jpg')){
	echo 'file exists!';
} else {
	echo 'you got bigger issues here, buddy!';
}
if(!unlink('Frame/Photos/2012-10-14 14.50.30.jpg')){
	echo'failed to delete file';
} else {
	echo 'file deleted';
}
?>
