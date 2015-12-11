var path = require('path');
var server = require('socket.io');

var socketio_client_path = path.join(
    path.dirname(require.resolve('socket.io')),
    'node_modules',
    'socket.io-client'
);

var client = require(socketio_client_path);


var io = server(3000);
io.on('connection', function(socket) {
    socket.emit('msg', 'Hello');
    socket.on('msg', function(data) {
        console.log(data);
        
        io.close();      
    });    
});

var socket = client('http://127.0.0.1:3000/');
socket.on('msg', function(data) {
    socket.emit('msg', data + ' World!');
    
    socket.disconnect();
});