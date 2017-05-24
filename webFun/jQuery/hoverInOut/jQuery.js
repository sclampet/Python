$(document).ready(function(){
	$('img').hover(function() {
		$(this).attr('src', './images/avatarstate.jpg');
	}, function() {
		$(this).attr('src', './images/aang.png');
	});
});