//given a str 'aabbbaa' return a2b3a2

function encode(str) {
	var temp = str[0]
	var count = 0
	var result = ''
	for(var i = 0; i <= str.length; i++) {
		// console.log('temp: '+temp+' str[i] '+str[i]+ ' i: '+i+ 'count: '+ count)
		if(str[i] != temp) {
			result += temp + count.toString()
			temp = str[i];
			count = 1;
		} else {
			count++;
		}
	}
	return result
}

var str = 'aabbbaa'
console.log(encode(str))