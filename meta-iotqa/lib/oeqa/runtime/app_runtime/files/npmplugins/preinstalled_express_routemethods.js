var http = require('http');
var express = require('express');

var app = express();

app.get('/', function(req, res) {
    res.send('GET request to the homepage');
});

app.post('/', function(req, res) { 
    res.send('POST request to the homepage');
});

var server = app.listen(3000, function() {    
    var reqURL = 'http://127.0.0.1:3000/'; 
       
    http.get(reqURL, function(res) {                
        res.setEncoding('utf8');        
        res.on('data', function(data) {        
            console.log(data);
        });        
       //server.close();
    });
    
    var postOptions = {
        host: '127.0.0.1',
        port: 3000,
        path: '/',
        method: 'POST'   
    };
    var req = http.request(postOptions, function (res) {
        res.setEncoding('utf8');
        res.on('data', function(data) {
            console.log(data);        
        });    
        
        server.close();
    }); 
    
    req.end();
});
