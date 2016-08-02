function matchingSong(){
	alert('Click ok to reveal your song: ');
	window.location.replace("/matching_song");
}

function songReplace(){
	window.location.replace('/song_quiz');
}

function setup(){
	$("#submit").click(matchingSong);
	$("#songm").click(songReplace);
}

$(document).ready(setup);

