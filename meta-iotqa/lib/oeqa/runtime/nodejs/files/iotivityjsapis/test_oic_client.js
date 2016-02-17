var device = require('iotivity-node');

var OicClient = device.prototype;

module.exports = {

	setUp: function(callback) {
		callback();
	},	
	tearDown: function(callback) {
		callback();
	},

	testOicClientHasFindResourcesPromise: function(test) {
		test.ok('findResources' in OicClient);
		test.strictEqual(typeof(OicClient.findResources), 'function');
		test.done();
	},
	testOicClientHasFindDevicesPromise: function(test) {
		test.ok('findDevices' in OicClient);
		test.strictEqual(typeof(OicClient.findDevices), 'function');
		test.done();
	},

	testOicClientHasCreateResourcePromise: function(test) {
		test.ok('createResource' in OicClient);
		test.strictEqual(typeof(OicClient.createResource), 'function');
		test.done();
	},	
	testOicClientHasRetrieveResourcePromise: function(test) {
		test.ok('retrieveResource' in OicClient);
		test.strictEqual(typeof(OicClient.retrieveResource), 'function');
		test.done();
	},
	testOicClientHasUpdateResourcePromise: function(test) {
		test.ok('updateResource' in OicClient);
		test.strictEqual(typeof(OicClient.updateResource), 'function');
		test.done();
	},
	testOicClientHasDeleteResourcePromise: function(test) {
		test.ok('deleteResource' in OicClient);
		test.strictEqual(typeof(OicClient.deleteResource), 'function');
		test.done();
	}
}	