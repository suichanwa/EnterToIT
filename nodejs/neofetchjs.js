const os = require('os');

//i gotta write an neofetch clone in nodejs that will run on windows and linux
//i will call it nodefetch

const main = () => {
    console.log(os.userInfo());
    console.log(os.platform());
    console.log(os.release());
    console.log(os.type());
    console.log(os.arch());
    console.log(os.hostname());
    console.log(os.uptime());
    console.log(os.totalmem().toExponential());
    console.log(os.freemem().toLocaleString());
    console.log(os.cpus());
    console.log(os.networkInterfaces());
}

main()