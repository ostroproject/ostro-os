var oicPresence = require('iotivity-node')('client');

module.exports = {

    setUp: function(callback) {
        callback();
    },
    tearDown: function(callback) {
        callback();
    },
    testOicPresenceAttrSubscribe: function(testOicPresence) {
        testOicPresence.ok('subscribe' in oicPresence);
        testOicPresence.strictEqual(typeof(oicPresence.subscribe), 'function');
        testOicPresence.done();
    },
    testOicDiscoveryAttrUnsubscribe: function(testOicPresence) {
        testOicPresence.ok('unsubscribe' in oicPresence);
        testOicPresence.strictEqual(typeof(oicPresence.unsubscribe), 'function');
        testOicPresence.done();
    },
    testOicDiscoveryAttrOndevicechange: function(testOicPresence) {
        testOicPresence.ok('ondevicechange' in oicPresence);
        testOicPresence.done();
    }
}