$(document).ready(function(){
	$('form').submit(function(e){
		e.preventDefault()
		var fields = {
			"firstName": $('#firstName').val(),
			"lastName": $('#lastName').val(),
			"description": $('#description').val()
		}
		var $ele  = $('<div></div>')
		$ele.html('<h2>'+fields.firstName+' '+fields.lastName+'</h2><p>'+fields.description+'</p>	');
		$('.cards').append($ele);
		$('input:first-child, input:nth-child(2), textarea').val(null);

	})
	$("div.cards").on("click", "h2", function(){
		$(this).siblings().toggle("slow")
	})
})