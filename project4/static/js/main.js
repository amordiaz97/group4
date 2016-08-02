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

function goToGoogle(){
	var result = str.link('https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwi-1djwv6POAhVKez4KHVRwAaAQPAgD');
	window.location.replace(result);
}

function setup(){
	$("#submit").click(matchingSong);
	$("#songm").click(songReplace);
	$('#home').click(goHome);
	$("#disney").click(goToDisney);
	$('#food').click(goToFood);
	$('#google').click(goToGoogle);
}

$(document).ready(setup);

