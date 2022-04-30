function printingInConsole() {
    console.log("printSometing");
}

var intervalID = setInterval(printingInConsole, 1000); // Will alert every second.
// clearInterval(intervalID); // Will clear the timer.

setTimeout(printingInConsole, 1000); // Will alert once, after a second.
setInterval(function(){ 
	console.log("Oooo Yeaaa!");
}, 2000);//run this thang every 2 seconds