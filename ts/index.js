"use strict";
exports.__esModule = true;
var hello_js_1 = require("./hello.js");
(0, hello_js_1["default"])();
var test = 'it works';
var anotherUser = ['some', 23];
var user = { name: 'john', age: 30 };
var arr = ['a', 'b', 'c', 'd', 'e'];
console.log(anotherUser[0]);
console.log(anotherUser[1]);
var time = [12, 59, 59];
time[0] = 1;
console.log(time);
user[0] = 'another';
console.log(user);
function func(test) {
    alert(test);
}
