<html>
	<head>
		<title></title>
	</head>
	<body>
		<?php 
		$trtrack = 0;
		$directory = 'Frame/Photos';
		$total = count(scandir($directory));
		$images_per_page = 25;
		$pages = ceil($total/$images_per_page);
		if(!intval($_GET['page']) || intval($_GET['page']) > $pages){
			$page = 0;
		} else {
			$page = intval($_GET['page']) - 1;
			}
		$start = $page * $images_per_page + 2;
		if ($page == 0){
			$start = 2;
		}
		$end = $start + $images_per_page;
		if ($end > $total){
			$end = $total;
		}
		$counter = $start;
		#echo $start.'<br>';
		#print_r(scandir($directory));
		echo '<table style="width:100%">';
		$imgtrck = 0;
		while($counter!=$end){
			$imgtrck ++;
			if($imgtrck >= $start && $imgtrck < $end){
				$tmp_fle = $directory.'/'.scandir($directory)[$counter];
				#$counter ++;
				$ImgInfo = getimagesize($tmp_fle);
				$width = $ImgInfo[0]*.05;
				$height = $ImgInfo[1]*.05;
				$index = $counter-1;
				echo '<tr>';
				echo '<td>'.$index.'</td>';
				echo '<td><img src= "'.$tmp_fle.'" height= "'.$height.'" width= "'.$width.'" /></td>';
				echo '<td> Height: '.$height.'<br>Width: '.$width.'</td>';
				echo '<td><input type="button" value="Delete Photo" onclick="foo(\''.$tmp_fle.'\')" /></td>';
				echo '</tr>';
				$counter ++;
			}
		}
		echo '</table>';
		#if(intval($_GET['page']) == 1){
		echo '<a href="">>>></a>';
		#} else if (intval($_GET['page']) == 1) || (intval($_GET['page']) !=$pages)
		#<a href=""><<</a>
		#<a href=""><<</a>
		?>
	</body>
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
	<script>
	function foo(x){
		alert(x);
	$.ajax({
		url:"photodelete.php",
		type: "POST",
		data: {file: x},
		success:function(result){
			alert(result);
			window.location.reload();
		}
	});
}
</script>
</html>
