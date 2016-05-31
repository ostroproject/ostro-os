var oic = require('iotivity-node')('client'),
    OicPlatform = oic.platform;

module.exports = {

    setUp: function(callback) {
        callback();
    },
    tearDown: function(callback) {
        callback();
    },

    testOicPlatformAttrId: function(testOicPlatform) {
        testOicPlatform.ok('id' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.id), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrOsVersion: function(testOicPlatform) {
        testOicPlatform.ok('osVersion' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.osVersion), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrModel: function(testOicPlatform) {
        testOicPlatform.ok('model' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.model), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrManufacturerName: function(testOicPlatform) {
        testOicPlatform.ok('manufacturerName' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.manufacturerName), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrManufacturerUrl: function(testOicPlatform) {
        testOicPlatform.ok('manufacturerUrl' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.manufacturerUrl), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrManufactureDate: function(testOicPlatform) {
        testOicPlatform.ok('manufactureDate' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.manufactureDate), 'date');
        testOicPlatform.done();
    },

    testOicPlatformAttrPlatformVersion: function(testOicPlatform) {
        testOicPlatform.ok('platformVersion' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.platformVersion), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrFirmwareVersion: function(testOicPlatform) {
        testOicPlatform.ok('firmwareVersion' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.firmwareVersion), 'string');
        testOicPlatform.done();
    },

    testOicPlatformAttrSupportUrl: function(testOicPlatform) {
        testOicPlatform.ok('supportUrl' in OicPlatform);
        testOicPlatform.strictEqual(typeof(OicPlatform.supportUrl), 'string');
        testOicPlatform.done();
    }
}