var _ = require('underscore');

var users = [
    { 'user': 'barney',  'age': 36 },
    { 'user': 'fred',    'age': 40 },
    { 'user': 'pebbles', 'age': 18 }
];

console.log(_.map(users, function(user) {
    return user.user;    
}).join(', ').toString());

