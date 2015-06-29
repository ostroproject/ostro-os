var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test');

var Cat = mongoose.model('Cat', { name: String });

var kitty = new Cat({ name: 'HelloKitty' });
kitty.save(function (err) {
    if (err) throw err;
    //console.log('meow');
    
    Cat.find({name: 'HelloKitty'}, function(err, myCats){
        if (err) throw err;
        if (myCats.length == 1 && myCats[0].name == 'HelloKitty') {
            console.log('meow');        
        }
        Cat.remove({ name: 'HelloKitty' }, function(err) {
            if (err) throw err;
            
            mongoose.disconnect();    
        });                
    });
    
});