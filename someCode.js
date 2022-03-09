let timerId;
const sum = 0;
let arr = [1,2,3];
let result = getInt([1, 2, 3], [2, 3, 4], [4, 3, 2]);
let arrWithLetters = ['a', 'b', 'c'];
let numbs = [-1,2,3,4,-5, 7, 8,9];
let nums = [2,3,4,5,6]; 
let date = new Date();
let elem  = document.querySelector('#elem');
const divs = document.querySelectorAll('div');
const elem2 = document.querySelector('#elem2');
let eve = nums.every(elem => elem %  2 == 0);
const but = document.querySelector('#button');
const foc = document.querySelector('#focus');
const changeEvent = document.querySelector('#changeEvent');
const input = document.querySelector('#input');
const lii = document.querySelector('#checked');
const modBut = document.querySelector('#elem');
const div = document.querySelector('div');
const button = document.querySelector('button');
const list   = document.querySelector('ul');
const items  = list.querySelectorAll('li');
let start = document.querySelector('#start');
let stop  = document.querySelector('#stop');
let parent = document.querySelector('#parent');


function timer(){
	let i = 0;

	elem.addEventListener('click', function() {
		setInterval(function() {
			console.log(this.value); // будет выводится undefined
		}, 1000);
	});

	stop.addEventListener('click', () => {
		clearInterval(timerId);
	});

	elem.addEventListener('click', () => {
		setTimeout(() => {
			alert('!');
		}, 3000);
	})
}



function ParentFuncs(){
	console.log(this.value);

	let child = () => {
		console.log(this.value);
	}


	for (let i = 1; i <= 9; i++) {
		let p = document.createElement('p');
		p.innerHTML = '!';
		
		parent.appendChild(p);
	}

	child();
}

class handler {
	constructor() {
		this.innerHTML = this.innerHTML + '!';
	}
}


// 

function NewElem(){
	for (let item of items) {
		item.addEventListener('click', handler);
	}

	button.addEventListener('click', function() {
		let item = document.createElement('li');
		item.innerHTML = 'item';
		
		item.addEventListener('click', handler);
		
		list.appendChild(item);
	});
}


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
WorkWuithLists();
NewElem();
timer();
ParentFuncs();
