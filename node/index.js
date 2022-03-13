'use stric'
let date = new Date();

let i = 0;
let fs = require('fs');
let http = require('http');
let url = require('url');

setInterval(function(){
    console.log(+i);
}, 10000000);

let math = require('./math.js');
console.log(math.square(4));


fs.readFile('readme.txt', 'utf-8', function(err, data){

    let digits = data.split('');
    console.log(digits);
});

fs.mkdir('folder/test', err => {
    if (err) throw err;
})

fs.rename('readme.txt', 'new.txt', (err, files) => {
    if (err) throw err;
    console.log(files)
})



