let sum = 0;
let arr = [1,2,3];
let result = getInt([1, 2, 3], [2, 3, 4], [4, 3, 2]);
let arrWithLetters = ['a', 'b', 'c'];
let numbs = [-1,2,3,4,-5, 7, 8,9];
let nums = [2,3,4,5,6]; 
let date = new Date();
let elem  = document.querySelector('#elem');
let divs = document.querySelectorAll('div');
let elem2 = document.querySelector('#elem2');
let eve = nums.every(elem => elem %  2 == 0);
let but = document.querySelector('#button');
let foc = document.querySelector('#focus');
let changeEvent = document.querySelector('#changeEvent');
let input = document.querySelector('#input');
let lii = document.querySelector('#checked');
let modBut = document.querySelector('#elem');
let div = document.querySelector('div');


//clickInThisDiv


div.addEventListener('click', function(event) {
	if (event.target.matches('div')) {
		alert('clicked on div');
	}
	if (event.target.matches('p')) {
		alert('click on p');
	}
});

function modButtons(){
	modBut.addEventListener('click', function(event) {
		if (event.ctrlKey) {
			console.log('нажат Ctrl');
		}
		
		if (event.altKey) {
			console.log('нажат Alt');
		}
		
		if (event.shiftKey) {
			console.log('нажат Shift');
		}
	});
}

function WorkWuithLists(){

	lii.addEventListener('click', function(event){
		console.log(event.target); // выведет наш абзац
		console.log(this);   
	});

	elem.addEventListener('click', function(event) {
		console.log(event.target); // выведет наш абзац
		console.log(this);         // выведет наш див
	});

	document.addEventListener('mousemove', function(event) {
		elem.innerHTML = event.clientX + ' : ' + event.clientY;
	});

	input.addEventListener('input', function(){
		console.log(this.value);
	});
}

//event change

changeEvent.addEventListener('changeEvent', function(){
	console.log(this.value);
})

//radioButtons

function radioButs(){
	let radios = document.querySelectorAll('input[type="radio"]');
	let button = document.querySelector('#button');

	button.addEventListener('click', function(){
		for(let radio of radios){
			if(radio.checked){
				console.log(radio.value);
			}
		}
	})
}


//disableEnable
function disEnbl(){
	let elem = document.querySelector('#elem');
	let button = document.querySelector('#button');

	button.addEventListener('click', function(){
		elem.disable = !elem.disabled;
	})
}


//remove affter first tap 

function Remove(){
	let elems = document.querySelectorAll('p');

	for(elem of elems){
		elem.addEventListener('click', function func(){
			alert(this.innerHTML);
			this.removeEventListener('click', func);
		});
	}
}


function func() {
	alert('!!!');
	this.removeEventListener('click', func);
}

for (let div of divs) {
	div.addEventListener('click', function(){
		this.innerHTML++;
	});
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

function consoleLogs(){
    console.log(['a', ['b', 'c', 'd'], ['e', 'f', ['g', ['j', 'k']]]]);  
    console.log(sum);  
    console.log(numbs.filter(elem => elem > 0));
    console.log(eve);
	console.log(date.getFullYear());
	console.log(result);
}

//functions_source

consoleLogs();
Remove();
disEnbl();
radioButs();
modButtons();
WorkWuithLists()
