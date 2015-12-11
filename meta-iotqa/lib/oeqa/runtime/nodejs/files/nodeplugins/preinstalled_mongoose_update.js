var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/test');

var Cat = mongoose.model('Cat', { name: String });

var kitty = new Cat({ name: 'Tom' });
kitty.save(function (err) {
    if (err) throw err;
        
    kitty.update({name: 'Jerry'}, function(err) {
        if (err) throw err;
              
        Cat.find({name: /Jerry/}, function(err, myCats) {
            if (err) throw err;
            console.log(myCats[0].name);
            
            Cat.remove({name: /Jerry/}, function(err) {
                if (err) throw err;
        
                mongoose.disconnect();    
            });
        });         
    });
});

