// given a2b3a2 return 'aabbbaa'

function decode(str) {
	var temp = str[0];
	var count = 0;
	var result = '';
	for(var i = 0; i < str.length; i++) {
		if(str[i] != temp) {
			count = parseInt(str[i])
			while(count) {
				result += temp
				count--;
			}
			temp = str[i + 1]	
		} else {
			continue;
			console.log(temp)
		}
	}
	return result
}

var str = 'a2b3a2c6'

console.log(decode(str))
