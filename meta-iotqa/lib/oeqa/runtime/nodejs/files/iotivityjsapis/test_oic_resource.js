var resource = require('iotivity-node/lib/OicResource');

var OicResource = resource.prototype;

module.exports = {

	setUp: function(callback) {
		callback();
	},	
	tearDown: function(callback) {
		callback();
	},

	testOicResourceHasaddEventListener: function(test) {
		test.ok('addEventListener' in OicResource);
		test.strictEqual(typeof(OicResource.addEventListener), 'function');
		test.done();
	},
	testOicResourceHasremoveEventListener: function(test) {
		test.ok('removeEventListener' in OicResource);
		test.strictEqual(typeof(OicResource.removeEventListener), 'function');
		test.done();
	},

	testOicResourceHasdispatchEvent: function(test) {
		test.ok('dispatchEvent' in OicResource);
		test.strictEqual(typeof(OicResource.dispatchEvent), 'function');
		test.done();
	}
}	