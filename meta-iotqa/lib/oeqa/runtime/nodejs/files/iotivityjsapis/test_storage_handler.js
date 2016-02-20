var handler = require('iotivity-node/lib/StorageHandler');

var StorageHandler = handler.prototype;

module.exports = {

	setUp: function(callback) {
		callback();
	},	
	tearDown: function(callback) {
		callback();
	},

	testStorageHandleropen: function(test) {
		test.ok('open' in StorageHandler);
		test.strictEqual(typeof(StorageHandler.open), 'function');
		test.done();
	},
	testStorageHandlerHasclose: function(test) {
		test.ok('close' in StorageHandler);
		test.strictEqual(typeof(StorageHandler.close), 'function');
		test.done();
	},

	testStorageHandlerHasread: function(test) {
		test.ok('read' in StorageHandler);
		test.strictEqual(typeof(StorageHandler.read), 'function');
		test.done();
	},
	testStorageHandlerHaswrite: function(test) {
		test.ok('write' in StorageHandler);
		test.strictEqual(typeof(StorageHandler.write), 'function');
		test.done();
	},

	testStorageHandlerHasunlink: function(test) {
		test.ok('unlink' in StorageHandler);
		test.strictEqual(typeof(StorageHandler.unlink), 'function');
		test.done();
	}
}	