const fs = require('fs');
const path = require('path');

fs.mkdir(path.join(__dirname, 'test'), err => {
    if (err) throw err;
    console.log('Folder created...');
});

fs.writeFile(path.join(__dirname, 'notes', 'hello.txt'), 'Hello World!', err => {
    if (err) throw err;
    console.log('File written to...');

    fs.appendFile(path.join(__dirname, 'notes', 'hello2.txt'), ' I love Node.js', err => {
        if (err) throw err;
        console.log('File written to...');
    });
});

fs.readFile(path.join(__dirname, '', 'userinfo.json'), (err,data) => {
    if (err) throw err;
    console.log(data);
})

fs.rename(path.join(__dirname, 'notes', 'hello.txt'), path.join(__dirname, 'notes', 'helloworld.txt'), err => {
    if (err) throw err;
    console.log('File renamed...');
});