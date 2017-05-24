$(document).ready(function(){
	//Keeps page from navigating elsewhere upon submit
	$('#form1').submit(function(){
		return false;
	})
});

//Gets input field values and appends to the table
$(document).on('click', '.btn', function(){
	$firstName = $('#firstName').val();
	$lastName = $('#lastName').val();
	$email = $('#email').val();
	$contact = $('#contact').val();

	$('table').append("<tr><td>"+$firstName+"<td>"+$lastName+"</td>"+"<td>"+$email+"</td>"+"<td>"+$contact+"</td></tr>");
});