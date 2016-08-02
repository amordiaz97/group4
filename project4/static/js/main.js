function matchingSong(){
	alert('Click ok to reveal your song: ');
	window.location.replace("/matching_song");
}

function songReplace(){
	window.location.replace('/song_quiz');
}

function goHome(){
	window.location.replace('/');
}

function setup(){
	$("#submit").click(matchingSong);
	$("#songm").click(songReplace);
	$('#home').click(goHome);
}

$(document).ready(setup);

