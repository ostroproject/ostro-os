var http = require('http');
var express = require('express');

var app = express();

// will match request to the root
app.get('/', function (req, res) {
    res.send('root');
});

// will match requests to /about
app.get('/about', function (req, res) {
    res.send('about');
});

// will match request to /random.text
app.get('/random.text', function (req, res) {
    res.send('random.text');
});

var server = app.listen(3000, function() {    

    var reqUrlRoot = 'http://127.0.0.1:3000/';
    var reqUrlAbout = 'http://127.0.0.1:3000/about';
    var reqUrlRandom = 'http://127.0.0.1:3000/random.text';
    
    http.get(reqUrlRoot, function(res) {                
        res.setEncoding('utf8');        
        res.on('data', function(data) {        
            console.log(data);
        });                
    });

    http.get(reqUrlAbout, function(res) {                
        res.setEncoding('utf8');        
        res.on('data', function(data) {        
            console.log(data);
        });     
    });
        
    http.get(reqUrlRandom, function(res) {                
        res.setEncoding('utf8');        
        res.on('data', function(data) {        
            console.log(data);
        });
            
        server.close();                             
    });               
});    