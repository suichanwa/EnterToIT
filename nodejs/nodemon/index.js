const http = require('http');
const fs = require('fs');
const path = require('path');

const server = http.createServer((req, res) => {
    if(req.method === 'GET') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<form method="POST" action="/message">');
        res.write('<input type="text" name="message">');
        res.write('<input type="submit" value="Submit">');
        res.write('</form>');
    } if (req.method === 'POST') {
        res.writeHead(200, {'Content-Type': 'text/html'});
        res.write('<h1>Thanks for submitting your message!</h1>');
        let body = [];
        req.on('data', (chunk) => {
            body.push(chunk);
        }).on('end', () => {
            body = Buffer.concat(body).toString();
            let message = body.split('=')[1];
            res.write(`<h2>Your message: ${message}</h2>`);
            res.end();
        });
    }
    if(req.url === '/about') {
        fs.readFile(path.join(__dirname, 'about.html'), (err, data) => {
            if(err) throw err;
            res.write(data);
            res.end();
        });
    }
});

server.listen(3000, () => {console.log('Server is running...');})
