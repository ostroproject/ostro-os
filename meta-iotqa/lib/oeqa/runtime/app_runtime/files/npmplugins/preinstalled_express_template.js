var fs = require('fs');
var http = require('http');
var express = require('express');

var app = express();

app.engine('ntl', function (filePath, options, callback) { // define the template engine
    fs.readFile(filePath, function (err, content) {
        if (err) return callback(new Error(err));
        // this is an extremely simple template engine
        var rendered = content.toString().replace('#title#', '<title>'+ options.title +'</title>')
            .replace('#message#', '<h1>'+ options.message +'</h1>');
        
        return callback(null, rendered);
    });  
});

app.set('views', './views'); // specify the views directory
app.set('view engine', 'ntl'); // register the template engine

app.get('/', function (req, res) {
    res.render('index', { title: 'Hey', message: 'Hello there!'});
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