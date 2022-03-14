import helloWorld from "./hello.js";
import { pi, phi, absolute } from "./math.js";

console.log(pi);
const absPhi = absolute(phi);


let test: string = 'it works';
let anotherUser : [string, number] = ['some', 23];
let user = {name : 'john',age:30};
let arr: string[] = ['a', 'b', 'c', 'd', 'e'];


console.log(anotherUser[0]);
console.log(anotherUser[1])

let time: [number, number, number] = [12, 59, 59];
time[0] = 1;
console.log(time);

user[0] = 'another';
console.log(user);

function func(test: string): void {
	alert(test);
}
