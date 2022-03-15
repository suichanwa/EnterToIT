make(function() {
	console.log('2');
});

function make(num, callback) {
	setTimeout(function() {
		let arr = [1, 2, 3, 4, 5];
		
		let err;
		if (arr[num] === undefined) {
			err = 'elem not exists'; 
		} else {
			err = null;
		}
		
		callback(arr[num], err);
	}, 3000);
}


make(3, function(res) {
	console.log(res);
});


