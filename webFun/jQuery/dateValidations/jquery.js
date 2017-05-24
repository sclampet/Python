$(document).ready(function(){
	console.log('Working');

	$('#fromDate').datepicker();
	$('#toDate').datepicker();

	$('form').submit(function(e){
		e.preventDefault();
		var fields = {
			"fromDate": $("#fromDate").val(),
			"toDate": $("#toDate").val(),
			"name": $("#name").val()
		}
		if($('#fromDate').val() && $('#toDate').val() && $("#name").val()){
			alert("Thanks "+fields.name+"! Your Cruise leaves on "+fields.fromDate+" and returns "+fields.toDate+"!")
		} else {
			alert('You must complete all fields before confirming.');
		}
	})
})