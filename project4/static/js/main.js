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

function goToDisney(){

	window.location.replace('/disney');
}

function goToFood(){
	window.location.replace('/food');
}

function matchingDisney(){
	alert('Click ok to reveal your Disney character ');
	window.location.replace('/matching_disney');

}
function setup(){
	$("#submit").click(matchingSong);
	$("#songm").click(songReplace);
	$('#home').click(goHome);
	$("#disney").click(goToDisney);
	$('#food').click(goToFood);
	$("#submit_disney").click(matchingDisney);
}

$(document).ready(setup);

