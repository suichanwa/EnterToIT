const express = require('express')
      app = express();
      port = 3000;
const moment = require('moment');

app.use(express.static('public'))
app.use('/css', express.static(__dirname + 'public/css'))
app.use('/js', express.static(__dirname + 'public/js'))

app.get('*', (req, res) => {
    res.sendFile(__dirname +'public/index.html');
}) 

app.listen(port, () => console.info('liseting to http://localhost:3000/'));

var jsdom = require('jsdom');
$ = require('jquery')(new jsdom.JSDOM().window);

$(function() {
    $('button').bind('click', function(){
        alert("hi from js file");
    })
})

function showallthatshit(){
    $('ul#langs').append(function(index,html){
        return $('<li>JavaScript</li>');
    });
    $('<li>C#</li>').prependTo('#langs');
}

showallthatshit();