
function goToSong(){
	window.location.replace('/song_quiz');
}

function goHome(){
	window.location.replace('/home');
}

function goToDisney(){

	window.location.replace('/disney');
}

function goToFood(){
	window.location.replace('/food');
}



function setup(){
	$("#songm").click(goToSong);
	$('#home').click(goHome);
	$("#disney").click(goToDisney);
	$('#food').click(goToFood);
}

$(document).ready(setup);

