var OicServer = require('iotivity-node')('server');

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
	},
	testOicServerHasOnobserverequestEvent: function(test) {
		test.ok('onobserverequest' in OicServer);
		test.done();
	},
	testOicServerHasOnunobserverequestEvent: function(test) {
		test.ok('onunobserverequest' in OicServer);
		test.done();
	},
	testOicServerHasOnretrieverequestEvent: function(test) {
		test.ok('onretrieverequest' in OicServer);
		test.done();
	},
	testOicServerHasOndeleterequestEvent: function(test) {
		test.ok('ondeleterequest' in OicServer);
		test.done();
	},
	testOicServerHasOnupdaterequestEvent: function(test) {
		test.ok('onupdaterequest' in OicServer);
		test.done();
	},
	testOicServerHasOncreaterequestEvent: function(test) {
		test.ok('oncreaterequest' in OicServer);
		test.done();
	}
}
