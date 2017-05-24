$(document).ready(function(){
	var world = [
			[2,2,2,2,2,2,2,2,2,2],
			[2,3,1,1,1,1,1,1,3,2],
			[2,1,1,1,1,1,1,1,1,2],
			[2,1,1,1,1,1,1,1,1,2],
			[2,1,1,1,1,1,1,1,1,2],
			[2,1,1,1,1,1,1,1,1,2],
			[2,1,1,1,1,1,1,1,1,2],
			[2,1,1,1,1,1,1,1,1,2],
			[2,3,1,1,1,1,1,1,3,2],
			[2,2,2,2,2,2,2,2,2,2]
		];
	var pacman = {
		x: 1,
		y: 1
	};
	var ghost1 = {
		x: 0,
		y: 0
	};
	var score = 0;

	function displayWorld(){
		var output = '';

		for(var i = 0; i < world.length; i++){
			output += "\n<div class='row'>\n";
			for(var j = 0; j < world[i].length; j++){
				if(world[i][j] == 2)
					output += "<div class='brick'></div>";
				else if (world[i][j] == 1)
					output += "<div class='coin'></div>";
				else if(world[i][j] == 0)
					output += "<div class='empty'></div>";
				else if(world[i][j] == 3)
					output += "<div class='cherry'></div>";
			}
			output += "\n</div>";
		}
		// console.log(output);
		document.getElementById('world').innerHTML = output;
	}
	function displayPacman(){
		document.getElementById('pacman').style.top = pacman.y*20+"px"
		document.getElementById('pacman').style.left = pacman.x*20+"px"
	}
	function displayGhost1(){
		document.getElementById('ghost1').style.top = ghost1.y*20+"px"
		document.getElementById('ghost1').style.left = ghost1.x*20+"px"
	}
	function moveGhost1(){
		var random = Math.floor(Math.random() * 4) * 37;

		
	}
	function displayScore(){
		document.getElementById('score').innerHTML = score
	}

	displayPacman();
	displayWorld();
	displayScore();

	document.onkeydown = function(e){
		if(e.keyCode == 37 && world[pacman.y][pacman.x-1] !== 2){
			pacman.x--;
		}
		else if (e.keyCode == 39 && world[pacman.y][pacman.x+1] !== 2){
			pacman.x++;
		}
		else if (e.keyCode == 38 && world[pacman.y-1][pacman.x] !== 2){
			pacman.y--;
		}
		else if (e.keyCode == 40 && world[pacman.y+1][pacman.x] !== 2){
			pacman.y++;
		}

		if(world[pacman.y][pacman.x] == 1){
			world[pacman.y][pacman.x] = 0;
			score += 10;
		} 
		else if (world[pacman.y][pacman.x] == 3){
			world[pacman.y][pacman.x] = 0;
			score += 500;
		}
			displayScore();
			displayScore();
			displayGhost1();
			displayPacman();
	}
})	