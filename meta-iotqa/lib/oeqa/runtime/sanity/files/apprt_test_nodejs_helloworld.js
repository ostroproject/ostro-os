var http = require('http');

var body = 'Hello World!';
var port = 12346;

var server = http.createServer(function(req, res) {
    res.writeHead(200, {'content-type': 'text/plain'});
    res.end(body);
});

server.listen(port, function() {
    var options = {
        host: '127.0.0.1',
        port: port,
        path: '/',
        method: 'GET',
        headers: {
            accept: 'text/plain'
        }
    };

    var req = http.request(options, function(res) {
        res.setEncoding('UTF8');

        res.on('data', function(data) {
            console.log(data);
        });

        server.close();
    });
    req.end();    
});

