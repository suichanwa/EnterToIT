function runCode(){
    const w = range(11,1000);
    console.log(w); 
}


function randomInt(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

function asynckit(func) {
    setTimeout(func, randomInt(0, 1000));
}

// create function that do server request
function doServerRequest(url, callback) {
    asynckit(() => {
        callback(url);
    });
}


function getAllKeys(obj) {
    return Object.keys(obj);
}

//function that get current day
function getCurrentDay() {
    const date = new Date();
    const day = date.getDay();
    return day;
}

const gd = getCurrentDay();

//console.log(gd);


//create array of 5 namespace
const namespaces = ['github', 'google', 'facebook', 'twitter', 'instagram'];

//function that convert celsios to fahrenheit
function convertCelsiosToFahrenheit(celsius) {
    return celsius * 9 / 5 + 32;
}

//create an array of 5 objects with name and age
const users = [
    { name: 'John', age: 25 },
    { name: 'Bill', age: 30 },
    { name: 'Alex', age: 28 },
    { name: 'Nick', age: 32 },
    { name: 'Jack', age: 26 }
];

//create an array of 100 objects with name and age
const users2 = [];

//create function that print users array
function printUsers(users) {
    users.forEach(user => {
        console.log(user.name, user.age);
    });
}


//create function that range number from 1 to 10
function range(start, end) {
    let arr = [];
    for (let i = start; i <= end; i++) {
        arr.push(i);
    }
    return arr;
}
