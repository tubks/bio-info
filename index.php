<!DOCTYPE html>
<html>
	<head>
		<title></title>
		<link rel="stylesheet" href="">
</head>
<body>
	<div class="container" style="max-width: 50%;">
	<div class="text-center">
		<h2>Search by accession number</h2>
	</div>
	<input type="text" class="form-control" id="accession-search"' autocomplete="off"
		placeholder="Insert accession..."></input>
	<!---<button onclick="config.php">SERCZ</button>--->
	</div>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function(){
			$("#accession-search").keyup(function(){
				var input = $(this).val();
				//alert(input);
				if(input != ""){
					$.ajax({
						url:"search_acc.php",
						method:"post",
						data:{input:input},

						success:function(data){
							$("#searchresult").html(data);
						}
					});
				}
				else {
					$("#searchresult").css("display", "none");
				}
			});
		});
	</script>

</body>
</html>