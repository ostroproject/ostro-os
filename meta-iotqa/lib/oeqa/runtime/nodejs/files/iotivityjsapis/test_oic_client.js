var OicClient = require('iotivity-node')('client');

module.exports = {

	setUp: function(callback) {
		callback();
	},
	tearDown: function(callback) {
		callback();
	},

	testOicClientCreatePromise: function(test) {
		test.ok('create' in OicClient);
		test.strictEqual(typeof(OicClient.create), 'function');
		test.done();
	},
	testOicClientRetrievePromise: function(test) {
		test.ok('retrieve' in OicClient);
		test.strictEqual(typeof(OicClient.retrieve), 'function');
		test.done();
	},
	testOicClientUpdatePromise: function(test) {
		test.ok('update' in OicClient);
		test.strictEqual(typeof(OicClient.update), 'function');
		test.done();
	},
	testOicClientDeletePromise: function(test) {
		test.ok('delete' in OicClient);
		test.strictEqual(typeof(OicClient.delete), 'function');
		test.done();
	}
}