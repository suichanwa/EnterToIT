'use strict'

let http = require('http');
let url = require('url');

console.log('start');

http.createServer(function(request, response){
    if(request.url != '/suisei.jpg') {
        response.writeHead(200, {'Content-Type' : 'text/html'});
        
        let statusCode = 200;

        if(request.url == '/index'){
            response.write('<b> page index </b>');
        }
        else if (request.url == '/about') {
            response.write('<b> about page</b>');
        }
        else if (request.url == '/another') {
            response.write('<b> about page</b>');
        } else {
            statusCode = 404;
            response.write('<b> 404 page</b>');
        }
        response.statusCode = statusCode;
        response.end();
    }

}).listen(8888);
