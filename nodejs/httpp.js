const http = require('http');

const server = http.createServer((req, res) => {
    res.write('Hello World!');
    res.end();
});

server.listen(5000, () => console.log('Server running...on localhost:5000'));