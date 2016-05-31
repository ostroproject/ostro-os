var oic = require('iotivity-node')('client'),
    OicDevice = oic.device;

module.exports = {

    setUp: function(callback) {
        callback();
    },
    tearDown: function(callback) {
        callback();
    },

    testOicDeviceAttrUuid: function(testOicDevice) {
        testOicDevice.ok('uuid' in OicDevice);
        testOicDevice.strictEqual(typeof(OicDevice.uuid), 'string');
        testOicDevice.done();
    },

    testOicDeviceAttrUrl: function(testOicDevice) {
        testOicDevice.ok('url' in OicDevice);
        testOicDevice.strictEqual(typeof(OicDevice.url), 'string');
        testOicDevice.ok(':' in OicDevice.url);
        testOicDevice.done();
    },

    testOicDeviceAttrName: function(testOicDevice) {
        testOicDevice.ok('name' in OicDevice);
        testOicDevice.strictEqual(typeof(OicDevice.name), 'string');
        testOicDevice.done();
    },

    testOicDeviceAttrDataModels: function(testOicDevice) {
        testOicDevice.ok('dataModels' in OicDevice);
        testOicDevice.strictEqual(typeof(OicDevice.dataModels), 'string');
        testOicDevice.done();
    },

    testOicDeviceAttrCoreSpecVersion: function(testOicDevice) {
        testOicDevice.ok('coreSpecVersion' in OicDevice);
        testOicDevice.strictEqual(typeof(OicDevice.coreSpecVersion), 'string');
        testOicDevice.done();
    },

    testOicDeviceAttrRole: function(testOicDevice) {
        testOicDevice.ok('role' in OicDevice);
        testOicDevice.strictEqual(typeof(OicDevice.role), 'string');
        testOicDevice.done();
    }
}