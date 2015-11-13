var oicDevice = require('iotivity-node');

var device = new oicDevice();
var OicClient = device.client;

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
	},		
	testOicClientHasStartObservingPromise: function(test) {
		test.ok('startObserving' in OicClient);
		test.strictEqual(typeof(OicClient.startObserving), 'function');
		test.done();
	},
	testOicClientHasCancelObservingPromise: function(test) {
		test.ok('cancelObserving' in OicClient);
		test.strictEqual(typeof(OicClient.cancelObserving), 'function');
		test.done();
	},	

	testOicClientHasOnresourcechange: function(test) {
		test.ok('onresourcechange' in OicClient);
		test.done();
	},		
	testOicClientHasStartOnresourcefound: function(test) {
		test.ok('onresourcefound' in OicClient);
		test.done();
	},
	testOicClientHasCancelOndevicefound: function(test) {
		test.ok('ondevicefound' in OicClient);
		test.done();
	},		
}	