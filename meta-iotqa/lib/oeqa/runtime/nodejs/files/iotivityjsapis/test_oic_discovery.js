var oicDiscovery = require('iotivity-node')('client');

module.exports = {

    setUp: function(callback) {
        callback();
    },
    tearDown: function(callback) {
        callback();
    },

    testOicDiscoveryAttrFindResources: function(testOicDiscovery) {
        testOicDiscovery.ok('findResources' in oicDiscovery);
        testOicDiscovery.strictEqual(typeof(oicDiscovery.findResources), 'function');
        testOicDiscovery.done();
    },
    testOicDiscoveryAttrGetDeviceInfo: function(testOicDiscovery) {
        testOicDiscovery.ok('getDeviceInfo' in oicDiscovery);
        testOicDiscovery.strictEqual(typeof(oicDiscovery.getDeviceInfo), 'function');
        testOicDiscovery.done();
    },
    testOicDiscoveryAttrGetPlatformInfo: function(testOicDiscovery) {
        testOicDiscovery.ok('getPlatformInfo' in oicDiscovery);
        testOicDiscovery.strictEqual(typeof(oicDiscovery.getPlatformInfo), 'function');
        testOicDiscovery.done();
    },
    testOicDiscoveryAttrFindDevices: function(testOicDiscovery) {
        testOicDiscovery.ok('findDevices' in oicDiscovery);
        testOicDiscovery.strictEqual(typeof(oicDiscovery.findDevices), 'function');
        testOicDiscovery.done();
    },
    testOicDiscoveryAttrOnresourcefound: function(testOicDiscovery) {
        testOicDiscovery.ok('onresourcefound' in oicDiscovery);
        testOicDiscovery.done();
    },
    testOicDiscoveryAttrOndevicefound: function(testOicDiscovery) {
        testOicDiscovery.ok('ondevicefound' in oicDiscovery);
        testOicDiscovery.done();
    },
    testOicDiscoveryAttrOndiscoveryerror: function(testOicDiscovery) {
        testOicDiscovery.ok('ondiscoveryerror' in oicDiscovery);
        testOicDiscovery.done();
    }
}