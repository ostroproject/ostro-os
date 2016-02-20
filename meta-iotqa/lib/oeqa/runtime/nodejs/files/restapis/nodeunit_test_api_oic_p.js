var http = require('http');
var fs = require('fs');

var options = {
    host: '127.0.0.1',
    port: 8000,
    path: '/api/oic/p',
    method: 'GET',
    headers: {
        'Accept': 'text/json'    
    }    
};

var apiOicP = {};
var responseJson = 'api_oic_p.json';

function sendHttpRequest(opts) {
    var req = http.request(opts, function(res) {    
        apiOicP.statusCode = res.statusCode;
        res.setEncoding('utf8');
        
        res.on('data', function(data) {
            apiOicP.apiResponse = JSON.parse(data);
               fs.writeFileSync(responseJson, JSON.stringify(apiOicP)); 
        });
    });
    req.end();
}

// First generate HTTP response file. Only node script will generate the
// json format response.
if (process.argv[1] == __filename) {
    sendHttpRequest(options);
}

module.exports = {
    setUp: function(callback) {
        var content = fs.readFileSync(responseJson);
        this.apiOicP = JSON.parse(content.toString());
            
        callback();
    },
    tearDown: function(callback) {        
        callback();        
    },
    
    // statue code
    testApiOicPStatusCode: function(test) {
        test.strictEqual(this.apiOicP.statusCode, 200, 
                        'Response is not OK!');
        test.done();            
    },        
    
    // required properties
    // pi
    testApiOicPRequiredPiNotNull: function(test) {
        test.ok('pi' in this.apiOicP.apiResponse, 
                    'pi is not a property in the response of /api/oic/p while it is required!');
        test.done();
    },
    testApiOicPRequiredPiType: function(test) {
        test.strictEqual(typeof this.apiOicP.apiResponse['pi'], 'string',                         
                        'pi property is not a string!');
        test.done();
    },
    
    // mnmn
    testApiOicPRequiredMnmnNotNull: function(test) {
        test.ok('mnmn' in this.apiOicP.apiResponse, 
                    'mnmn is not a property in the response of /api/oic/p while it is required!');
        test.done();
    },
    testApiOicPRequiredMnmnType: function(test) {
        test.strictEqual(typeof this.apiOicP.apiResponse['mnmn'], 'string',                         
                        'mnmn property is not a string!');
        test.done();
    },
    
    // optional properties
    // mnml
    testApiOicPOptionalMnmlType: function(test) {
        if ('mnml' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnml'], 'string',
                            'mnml property is not a string!');            
        }
        test.done();
    },
    // mnmo
    testApiOicPOptionalMnmoType: function(test) {
        if ('mnmo' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnmo'], 'string',
                            'mnmo property is not a string!');            
        }
        test.done();
    },    
    // mndt
    testApiOicPOptionalMndtType: function(test) {
        if ('mndt' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mndt'], 'string',
                            'mndt property is not a string!');            
        }
        test.done();
    },    
    // mnpv
    testApiOicPOptionalMnpvType: function(test) {
        if ('mnpv' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnpv'], 'string',
                            'mnpv property is not a string!');            
        }
        test.done();
    },
    // mnos
    testApiOicPOptionalMnosType: function(test) {
        if ('mnos' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnos'], 'string',
                            'mnos property is not a string!');            
        }
        test.done();
    },    
    // mnhw
    testApiOicPOptionalMnhwType: function(test) {
        if ('mnhw' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnhw'], 'string',
                            'mnhw property is not a string!');            
        }
        test.done();
    },  
    // mnfv
    testApiOicPOptionalMnfvType: function(test) {
        if ('mnfv' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnfv'], 'string',
                            'mnfv property is not a string!');            
        }
        test.done();
    },       
    // mnsl
    testApiOicPOptionalMnslType: function(test) {
        if ('mnsl' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['mnsl'], 'string',
                            'mnsl property is not a string!');            
        }
        test.done();
    },      
    // st
    testApiOicPOptionalStType: function(test) {
        if ('st' in this.apiOicP.apiResponse) {
            test.strictEqual(typeof this.apiOicP.apiResponse['st'], 'string',
                            'st property is not a string!');            
        }
        test.done();
    },          
}