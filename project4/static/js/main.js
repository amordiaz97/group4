function matchingSong(){
	alert('you clicked submit');
	window.location.replace("/matching_song");
}

function setup(){
	$("#submit").click(matchingSong);
}


$(document).ready(setup);