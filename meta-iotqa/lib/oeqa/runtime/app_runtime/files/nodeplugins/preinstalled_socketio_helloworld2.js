var path = require('path');
var http = require('http');
var socketio = require('socket.io');

var socketio_client_path = path.join(

    path.dirname(require.resolve('socket.io')),
    'node_modules',
    'socket.io-client'
);
var client = require(socketio_client_path);

var app = http.createServer();
var io = socketio(app);

app.listen(3000);

io.on('connection', function (socket) {
    socket.emit('news', {hello: 'Hello'});
    socket.on('my other event', function (data) {
        console.log(data);
            
        io.close();
    });
});   

var socket = client('http://127.0.0.1:3000/');
socket.on('news', function(data) {
    socket.emit('my other event', data['hello'] + ' World!');    
    socket.disconnect();
}); 