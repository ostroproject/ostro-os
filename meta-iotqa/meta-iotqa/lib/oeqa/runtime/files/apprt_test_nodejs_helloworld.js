var http = require('http');
var exec = require('child_process').exec;

var body = 'Hello World!';
var port = 12346;

var server = http.createServer(function(req, res) {
    res.writeHead(200, {'content-type': 'text/plain'});
    res.end(body);
});

server.listen(port, function() {
    var cmd = 'curl http://127.0.0.1:' + port + '/';
    exec(cmd, function(err, stdout, stderr) {
        if (err) throw err;
        server.close();
    });
});

process.on('exit', function() {
    console.log(body);
});

