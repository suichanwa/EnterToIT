let sum = 0;
let arr = [1,2,3];
let arrWithLetters = ['a', 'b', 'c'];
let numbs = [-1,2,3,4,-5, 7, 8,9];
let nums = [2,3,4,5,6]; 
let date = new Date();
let elem   = document.querySelector('#elem');
//хуйня 
let eve = nums.every(elem => elem %  2 == 0);
let but = document.querySelector('#button');
but.addEventListener('click', function(){
	console.log('go fuck off');
})
but.addEventListener('click', function() {
	elem.innerHTML = '!!!';
});
console.log(but);


function consoleLogs(){
    console.log(['a', ['b', 'c', 'd'], ['e', 'f', ['g', ['j', 'k']]]]);  
    console.log(sum);  
    console.log(numbs.filter(elem => elem > 0));
    console.log(eve);
	console.log(date.getFullYear());
}


function func(){
    let sum = 0;
    
    for(let elem of arr){
        if(typeof arr == 'object'){
            sum += func(elem);
        } else {
            sum += elem;
        }
    }
    return sum;
}

let res = arr.map(function(elem){
    console.log(elem);
})

//foreach для перебора массива

arrWithLetters.forEach(function(elem){
    document.write(elem);
})

arrWithLetters.forEach(function(elem) {
	sum += elem;
});




function func(num1, num2, num3, num4, num5) {
	return num1 + num2 + num3 + num4 + num5;
}

func(...[1,2,3,4,5]);


//func that take fixed value from arrays


function getInt(...arrs){
	let result = [];
	
	let arr0 = arrs.shift();
	
	for (let elem of arr0) {
		if (inArrays(elem, arrs)) {
			result.push(elem);
		}
	}
	return result;
}

function inArrays(elem, arrs){
	for (let arr of arrs) {
		if (!inArray(elem, arr)) {
			return false;
		}
	}
	return true;
}

function inArray(elem, arr) {
	return arr.indexOf(elem) !== -1;
}

// Проверим работу:
let result = getInt([1, 2, 3], [2, 3, 4], [4, 3, 2]);
console.log(result); 

//date



consoleLogs();
