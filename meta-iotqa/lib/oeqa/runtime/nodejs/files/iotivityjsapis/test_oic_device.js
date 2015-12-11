var oicDevice = require('iotivity-node');

var settings = {
	role: "intermediary",
	connectionMode: "acked"
};

var OicDevice = new oicDevice(settings);


module.exports = {

	setUp: function(callback) {
		callback();
	},	
	tearDown: function(callback) {
		callback();
	},

	testHasOicDeviceSettingsAttr: function(test) {
		test.ok('settings' in OicDevice);
		test.strictEqual(typeof(OicDevice.settings), 'object');		
		test.done();
	},

	testOicDeviceSettingsMemberUrl: function(test) {
		if ('url' in OicDevice.settings) {
			test.strictEqual(typeof(OicDevice.settings.url), 'string');
			test.ok(':' in OicDevice.settings.url);
		}
		test.done();		
	},

	testOicDeviceSettingsMemberInfo: function(test) {
		if ('info' in OicDevice.settings) {
			test.strictEqual(typeof(OicDevice.settings.info), 'object');
		}
		test.done();
	},

	testOicDeviceSettingsMemberRole: function(test) {
		if ('role' in OicDevice.settings) {
			test.strictEqual(typeof(OicDevice.settings.role), 'string');

			test.ok((OicDevice.settings.role === 'client') || 
					(OicDevice.settings.role === 'server') ||
					(OicDevice.settings.role === 'intermediary'));
		}
		test.done();
	},	

	testOicDeviceSettingsMemberConnectionMode: function(test) {
		if ('connectionMode' in OicDevice.settings) {
			test.strictEqual(typeof(OicDevice.settings.connectionMode), 'string');

			test.ok((OicDevice.settings.connectionMode === 'acked') || 
					(OicDevice.settings.role === 'non-acked') ||
					(OicDevice.settings.role === 'default'));
		}
		test.done();
	},

	testOicDeviceInfoMemberUuid: function(test) {
		var checkUuidFormat = function (str) {
			var uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
    		return uuidPattern.test(str);
		};

		if ('info' in OicDevice.settings) {
			if ('uuid' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.uuid), 'string');
				test.ok(checkUuidFormat(OicDevice.settings.info.uuid));
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberName: function(test) {
		if ('info' in OicDevice.settings) {
			if ('name' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.name), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberDataModels: function(test) {
		if ('info' in OicDevice.settings) {
			if ('dataModels' in OicDevice.settings.info) {
				test.strictEqual(OicDevice.settings.info.dataModels instanceof Array);

				for (var i = 0; i < OicDevice.settings.info.dataModels.length; i++) {
					test.ok(typeof(OicDevice.settings.info.dataModels[i]), 'string');
				}
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberCoreSpecVersion: function(test) {
		if ('info' in OicDevice.settings) {
			if ('coreSpecVersion' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.coreSpecVersion), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberOsVersion: function(test) {
		if ('info' in OicDevice.settings) {
			if ('osVersion' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.osVersion), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberModel: function(test) {
		if ('info' in OicDevice.settings) {
			if ('model' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.model), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberManufacturerName: function(test) {
		if ('info' in OicDevice.settings) {
			if ('manufacturerName' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.manufacturerName), 'string');
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberManufacturerUrl: function(test) {
		if ('info' in OicDevice.settings) {
			if ('manufacturerUrl' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.manufacturerUrl), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberManufacturerDate: function(test) {
		if ('info' in OicDevice.settings) {
			if ('manufacturerDate' in OicDevice.settings.info) {
				test.strictEqual(OicDevice.settings.info.manufacturerDate instanceof Date);
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberPlatformVersion: function(test) {
		if ('info' in OicDevice.settings) {
			if ('platformVersion' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.platformVersion), 'string');
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberFirmwareVersion: function(test) {
		if ('info' in OicDevice.settings) {
			if ('firmwareVersion' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.firmwareVersion), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberSupportUrl: function(test) {
		if ('info' in OicDevice.settings) {
			if ('supportUrl' in OicDevice.settings.info) {
				test.strictEqual(typeof(OicDevice.settings.info.supportUrl), 'string');
			}
		}
		test.done();
	},

	testOicDeviceHasMemberClient: function(test) {
		test.ok('client' in OicDevice);
		test.done();
	},

	testOicDeviceHasMemberServer: function(test) {
		test.ok('server' in OicDevice);
		test.done();
	},	

	testOicDeviceHasConfigurePromise: function(test) {
		test.ok('configure' in OicDevice);
		test.strictEqual(typeof OicDevice.configure, 'function');
		test.done();
	},	

	testOicDeviceHasFactoryResetPromise: function(test) {
		test.ok('factoryReset' in OicDevice);
		if ('factoryReset' in OicDevice) {
			test.strictEqual(typeof OicDevice.factoryReset, 'function');
		}
		test.done();
	},

	testOicDeviceHasRebootPromise: function(test) {
		test.ok('reboot' in OicDevice);
		if ('reboot' in OicDevice) {
			test.strictEqual(typeof OicDevice.reboot, 'function');
		}		
		test.done();
	},
}