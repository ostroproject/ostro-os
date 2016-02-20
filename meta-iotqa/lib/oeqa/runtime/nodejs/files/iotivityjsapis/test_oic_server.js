var device = require('iotivity-node');

var OicServer = device.prototype;

module.exports = {

	setUp: function(callback) {
		callback();
	},	
	tearDown: function(callback) {
		callback();
	},

	testOicServerHasRegisterResourcePromise: function(test) {
		test.ok('registerResource' in OicServer);
		test.strictEqual(typeof(OicServer.registerResource), 'function');
		test.done();
	},
	testOicServerHasUnregisterResourcePromise: function(test) {
		test.ok('unregisterResource' in OicServer);
		test.strictEqual(typeof(OicServer.unregisterResource), 'function');
		test.done();
	},
	testOicServerHasEnablePresencePromise: function(test) {
		test.ok('enablePresence' in OicServer);
		test.strictEqual(typeof(OicServer.enablePresence), 'function');
		test.done();
	},
	testOicServerHasDisablePresencePromise: function(test) {
		test.ok('disablePresence' in OicServer);
		test.strictEqual(typeof(OicServer.disablePresence), 'function');
		test.done();
	},
	testOicServerHasNotifyPromise: function(test) {
		test.ok('notify' in OicServer);
		test.strictEqual(typeof(OicServer.notify), 'function');
		test.done();
	}								
}
