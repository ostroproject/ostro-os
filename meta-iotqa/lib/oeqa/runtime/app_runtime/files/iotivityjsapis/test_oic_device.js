var oicDevice = require('iotivity');

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
		test.ok('_settings' in OicDevice);
		test.strictEqual(typeof(OicDevice._settings), 'object');		
		test.done();
	},

	testOicDeviceSettingsMemberUrl: function(test) {
		if ('url' in OicDevice._settings) {
			test.strictEqual(typeof(OicDevice._settings.url), 'string');
			test.ok(':' in OicDevice._settings.url);
		}
		test.done();		
	},

	testOicDeviceSettingsMemberInfo: function(test) {
		if ('info' in OicDevice._settings) {
			test.strictEqual(typeof(OicDevice._settings.info), 'object');
		}
		test.done();
	},

	testOicDeviceSettingsMemberRole: function(test) {
		if ('role' in OicDevice._settings) {
			test.strictEqual(typeof(OicDevice._settings.role), 'string');

			test.ok((OicDevice._settings.role === 'client') || 
					(OicDevice._settings.role === 'server') ||
					(OicDevice._settings.role === 'intermediary'));
		}
		test.done();
	},	

	testOicDeviceSettingsMemberConnectionMode: function(test) {
		if ('connectionMode' in OicDevice._settings) {
			test.strictEqual(typeof(OicDevice._settings.connectionMode), 'string');

			test.ok((OicDevice._settings.connectionMode === 'acked') || 
					(OicDevice._settings.role === 'non-acked') ||
					(OicDevice._settings.role === 'default'));
		}
		test.done();
	},

	testOicDeviceInfoMemberUuid: function(test) {
		var checkUuidFormat = function (str) {
			var uuidPattern = /^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$/i;
    		return uuidPattern.test(str);
		};

		if ('info' in OicDevice._settings) {
			if ('uuid' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.uuid), 'string');
				test.ok(checkUuidFormat(OicDevice._settings.info.uuid));
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberName: function(test) {
		if ('info' in OicDevice._settings) {
			if ('name' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.name), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberDataModels: function(test) {
		if ('info' in OicDevice._settings) {
			if ('dataModels' in OicDevice._settings.info) {
				test.strictEqual(OicDevice._settings.info.dataModels instanceof Array);

				for (var i = 0; i < OicDevice._settings.info.dataModels.length; i++) {
					test.ok(typeof(OicDevice._settings.info.dataModels[i]), 'string');
				}
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberCoreSpecVersion: function(test) {
		if ('info' in OicDevice._settings) {
			if ('coreSpecVersion' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.coreSpecVersion), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberOsVersion: function(test) {
		if ('info' in OicDevice._settings) {
			if ('osVersion' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.osVersion), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberModel: function(test) {
		if ('info' in OicDevice._settings) {
			if ('model' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.model), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberManufacturerName: function(test) {
		if ('info' in OicDevice._settings) {
			if ('manufacturerName' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.manufacturerName), 'string');
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberManufacturerUrl: function(test) {
		if ('info' in OicDevice._settings) {
			if ('manufacturerUrl' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.manufacturerUrl), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberManufacturerDate: function(test) {
		if ('info' in OicDevice._settings) {
			if ('manufacturerDate' in OicDevice._settings.info) {
				test.strictEqual(OicDevice._settings.info.manufacturerDate instanceof Date);
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberPlatformVersion: function(test) {
		if ('info' in OicDevice._settings) {
			if ('platformVersion' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.platformVersion), 'string');
			}
		}
		test.done();
	},

	testOicDeviceInfoMemberFirmwareVersion: function(test) {
		if ('info' in OicDevice._settings) {
			if ('firmwareVersion' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.firmwareVersion), 'string');
			}
		}
		test.done();
	},	

	testOicDeviceInfoMemberSupportUrl: function(test) {
		if ('info' in OicDevice._settings) {
			if ('supportUrl' in OicDevice._settings.info) {
				test.strictEqual(typeof(OicDevice._settings.info.supportUrl), 'string');
			}
		}
		test.done();
	},

	testOicDeviceHasMemberClient: function(test) {
		test.ok('_client' in OicDevice);
		test.done();
	},

	testOicDeviceHasMemberServer: function(test) {
		test.ok('_server' in OicDevice);
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