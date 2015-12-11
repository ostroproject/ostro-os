var http = require('http');
var express = require('express');

var app = express();

app.get('/', function(req, res) {
    res.send('Hello World!');
});

var server = app.listen(3000, function() {    
    var reqURL = 'http://127.0.0.1:3000/'; 
       
    http.get(reqURL, function(res) {                
        res.setEncoding('utf8');        
        res.on('data', function(data) {        
            console.log(data);
        });        
       server.close();
    });    
});
