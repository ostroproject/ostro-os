"""
@file iotivity_js_apis.py
"""

##
# @addtogroup nodejs nodejs
# @brief This is nodejs component
# @{
# @addtogroup iotivity_js_apis iotivity_js_apis
# @brief This is iotivity_js_apis module
# @{
##

import os
import subprocess

from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag


@tag(TestType='FVT', FeatureID='IOTOS-764')
class IotivityJSAPITest(oeRuntimeTest):
    '''
    The test suite checks whether the iotivity node binding APIs work well.
    @class IotivityJSAPITest
    '''

    iotivity_js_apis = 'iotivityjsapis'
    files_dir = os.path.join(os.path.dirname(__file__),
                            'files')
    iotivity_js_apis_dir = os.path.join(files_dir,
                            iotivity_js_apis
                            )
    nodeunit_zip = os.path.join(files_dir, 'master.zip')
    target_iotivity_js_apis_dir = '/tmp/%s' % iotivity_js_apis
    iotivity_js_apis_files = {
        'oic_device': 'test_oic_device.js',
        'oic_client': 'test_oic_client.js',
        'oic_server': 'test_oic_server.js',
        'oic_resource': 'test_oic_resource.js',
        'storage_handler': 'test_storage_handler.js'
    }


    @classmethod
    def all_files_exist(cls):
        '''
        Check if all the files exists.
        :return:
        @fn all_files_exist
        @param cls
        @return
        '''
        for test_file in cls.iotivity_js_apis_files.values():
            if not os.path.exists(os.path.join(os.path.dirname(__file__),
                                               'files',
                                               cls.iotivity_js_apis_dir,
                                               test_file)):
                return False
        return True


    @classmethod
    def setUpClass(cls):
        '''
        Copy all the JavaScript files to the target system.
        @fn setUpClass
        @param cls
        @return
        '''
        cls.tc.target.run('rm -fr %s' % cls.target_iotivity_js_apis_dir)
        cls.tc.target.run('rm -f %s.tar' % cls.target_iotivity_js_apis_dir)

        if os.path.exists('%s.tar' % cls.iotivity_js_apis_dir):
            os.remove('%s.tar' % cls.iotivity_js_apis_dir)

        # compress iotivity javascript api directory and copy it to target device.
        proc = None
        if cls.all_files_exist():
            proc = subprocess.Popen(
                ['tar', '-cf', '%s.tar' % cls.iotivity_js_apis, cls.iotivity_js_apis],
                cwd = cls.files_dir)
            proc.wait()

        if proc and proc.returncode == 0 and \
            os.path.exists('%s.tar' % cls.iotivity_js_apis_dir):
            cls.tc.target.copy_to(
                os.path.join(
                    os.path.dirname(__file__),
                                    'files',
                                    '%s.tar' % cls.iotivity_js_apis_dir),
                '%s.tar' % cls.target_iotivity_js_apis_dir)
            cls.tc.target.run('cd /tmp/; ' \
                            'tar -xf %s.tar -C %s/' % (
                                cls.target_iotivity_js_apis_dir,
                                os.path.dirname(cls.target_iotivity_js_apis_dir))
                            )


        if not os.path.exists('/tmp/master.zip'):
            proc = subprocess.Popen(['wget', 'https://github.com/caolan/nodeunit/archive/master.zip'],
                                cwd = cls.files_dir)
            proc.wait()
        else:
            os.system('cp -f /tmp/master.zip %s' % (cls.nodeunit_zip))

        if os.path.exists(cls.nodeunit_zip):
            #change nodeunit zip package to tar package
            os.chdir(cls.files_dir)
            os.system('unzip -oq %s; tar -cf master.tar nodeunit-master; rm -rf nodeunit-master' % cls.nodeunit_zip)
            cls.nodeunit_tar = os.path.join(cls.files_dir, 'master.tar')
            cls.tc.target.copy_to(cls.nodeunit_tar, '/tmp/master.tar')
            cls.tc.target.run('cd /tmp/; ' \
                            'tar -xf master.tar;' \
                            'chmod +x /tmp/nodeunit-master/bin/nodeunit'
                           )


    def test_oic_device_has_settings_attr(self):
        '''
        Test if OicDevice object has settings attribute.
        @fn test_oic_device_has_settings_attr
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testHasOicDeviceSettingsAttr' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_has_settings_attr
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_has_member_url(self):
        '''
        Test if OicDevice.settings has url member.
        @fn test_oic_device_settings_has_member_url
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceSettingsMemberUrl' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_has_member_url
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_has_member_info(self):
        '''
        Test if OicDevice.settings has info member.
        @fn test_oic_device_settings_has_member_info
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceSettingsMemberInfo' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_has_member_info
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_has_member_role(self):
        '''
        Test if OicDevice.settings has role member.
        @fn test_oic_device_settings_has_member_role
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceSettingsMemberRole' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_has_member_role
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_has_member_connectionMode(self):
        '''
        Test if OicDevice.settings has connectionMode member.
        @fn test_oic_device_settings_has_member_connectionMode
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceSettingsMemberConnectionMode' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_has_member_connectionMode
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_uuid(self):
        '''
        Test if OicDevice.settings.info has uuid member.
        @fn test_oic_device_settings_info_has_member_uuid
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberUuid' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_uuid
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_name(self):
        '''
        Test if OicDevice.settings.info has name member.
        @fn test_oic_device_settings_info_has_member_name
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberName' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_name
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_dataModels(self):
        '''
        Test if OicDevice.settings.info has dataModels member.
        @fn test_oic_device_settings_info_has_member_dataModels
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberDataModels' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_dataModels
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_coreSpecVersion(self):
        '''
        Test if OicDevice.settings.info has coreSpecVersion member.
        @fn test_oic_device_settings_info_has_member_coreSpecVersion
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberOsVersion' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_coreSpecVersion
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_osVersion(self):
        '''
        Test if OicDevice.settings.info has osVersion member.
        @fn test_oic_device_settings_info_has_member_osVersion
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberCoreSpecVersion' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_osVersion
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_model(self):
        '''
        Test if OicDevice.settings.info has model member.
        @fn test_oic_device_settings_info_has_member_model
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberModel' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_model
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_manufacturerName(self):
        '''
        Test if OicDevice.settings.info has manufacturerName member.
        @fn test_oic_device_settings_info_has_member_manufacturerName
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberManufacturerName' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_manufacturerName
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_manufacturerUrl(self):
        '''
        Test if OicDevice.settings.info has manufacturerUrl member.
        @fn test_oic_device_settings_info_has_member_manufacturerUrl
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberManufacturerUrl' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_manufacturerUrl
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_manufacturerDate(self):
        '''
        Test if OicDevice.settings.info has manufacturerDate member.
        @fn test_oic_device_settings_info_has_member_manufacturerDate
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberManufacturerDate' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_manufacturerDate
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_platformVersion(self):
        '''
        Test if OicDevice.settings.info has platformVersion member.
        @fn test_oic_device_settings_info_has_member_platformVersion
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberPlatformVersion' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_platformVersion
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_firmwareVersion(self):
        '''
        Test if OicDevice.settings.info has firmwareVersion member.
        @fn test_oic_device_settings_info_has_member_firmwareVersion
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberFirmwareVersion' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_firmwareVersion
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_settings_info_has_member_supportUrl(self):
        '''
        Test if OicDevice.settings.info has supportUrl member.
        @fn test_oic_device_settings_info_has_member_supportUrl
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceInfoMemberFirmwareVersion' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        ##
        # TESTPOINT: #1, test_oic_device_settings_info_has_member_supportUrl
        #
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_has_addEventListener(self):
        '''
        Test if OicDevice has addEventListener member.
        @fn test_oic_device_has_addEventListener
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceHasaddEventListener' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_has_configure_promise(self):
        '''
        Test if OicDevice has configure promise function.
        @fn test_oic_device_has_configure_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceHasConfigurePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_has_removeEventListener(self):
        '''
        Test if OicDevice has removeEventListener member.
        @fn test_oic_device_has_removeEventListener
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceHasremoveEventListener' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_device_has_dispatchEvent(self):
        '''
        Test if OicDevice has dispatchEvent member.
        @fn test_oic_device_has_dispatchEvent
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicDeviceHasdispatchEvent' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_device']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])

# OicClient
    def test_oic_client_has_findResources_promise(self):
        '''
        Test if OicClient has findResources promise function.
        @fn test_oic_client_has_findResources_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicClientHasFindResourcesPromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_client']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_client_has_findDevices_promise(self):
        '''
        Test if OicClient has findDevices promise function.
        @fn test_oic_client_has_findDevices_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicClientHasFindDevicesPromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_client']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_client_has_createResource_promise(self):
        '''
        Test if OicClient has createResource promise function.
        @fn test_oic_client_has_createResource_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicClientHasCreateResourcePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_client']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_client_has_retrieveResource_promise(self):
        '''
        Test if OicClient has retrieveResource promise function.
        @fn test_oic_client_has_retrieveResource_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicClientHasRetrieveResourcePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_client']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_client_has_updateResource_promise(self):
        '''
        Test if OicClient has updateResource promise function.
        @fn test_oic_client_has_updateResource_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicClientHasUpdateResourcePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_client']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_client_has_deleteResource_promise(self):
        '''
        Test if OicClient has deleteResource promise function.
        @fn test_oic_client_has_deleteResource_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicClientHasDeleteResourcePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_client']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])

# OicServer
    def test_oic_server_has_registerResource_promise(self):
        '''
        Test if OicClient has registerResource promise function.
        @fn test_oic_server_has_registerResource_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicServerHasRegisterResourcePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_server']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_server_has_unregisterResource_promise(self):
        '''
        Test if OicClient has unregisterResource promise function.
        @fn test_oic_server_has_unregisterResource_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicServerHasUnregisterResourcePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_server']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_server_has_enablePresence_promise(self):
        '''
        Test if OicClient has enablePresence promise function.
        @fn test_oic_server_has_enablePresence_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicServerHasEnablePresencePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_server']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_server_has_disablePresence_promise(self):
        '''
        Test if OicClient has disablePresence promise function.
        @fn test_oic_server_has_disablePresence_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicServerHasDisablePresencePromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_server']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_server_has_notify_promise(self):
        '''
        Test if OicClient has notify promise function.
        @fn test_oic_server_has_notify_promise
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicServerHasNotifyPromise' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_server']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])

# OicResource
    def test_oic_resource_has_addEventListener(self):
        '''
        Test if OicResource has addEventListener member.
        @fn test_oic_resource_has_addEventListener
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicResourceHasaddEventListener' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_resource']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_resource_has_removeEventListener(self):
        '''
        Test if OicResource has removeEventListener member.
        @fn test_oic_resource_has_removeEventListener
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicResourceHasremoveEventListener' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_resource']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_oic_resource_has_dispatchEvent(self):
        '''
        Test if OicResource has dispatchEvent member.
        @fn test_oic_resource_has_dispatchEvent
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testOicResourceHasdispatchEvent' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['oic_resource']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])

# StorageHandler
    def test_storage_handler_has_open(self):
        '''
        Test if StorageHandler has open member.
        @fn test_storage_handler_has_open
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testStorageHandleropen' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['storage_handler']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_storage_handler_has_close(self):
        '''
        Test if StorageHandler has close member.
        @fn test_storage_handler_has_close
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testStorageHandlerHasclose' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['storage_handler']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_storage_handler_has_read(self):
        '''
        Test if StorageHandler has read member.
        @fn test_storage_handler_has_read
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testStorageHandlerHasread' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['storage_handler']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    def test_storage_handler_has_write(self):
        '''
        Test if StorageHandler has write member.
        @fn test_storage_handler_has_write
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testStorageHandlerHaswrite' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['storage_handler']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])

    def test_storage_handler_has_unlink(self):
        '''
        Test if StorageHandler has unlink member.
        @fn test_storage_handler_has_unlink
        @param self
        @return
        '''
        (api_status, api_output) = self.target.run(
                'export NODE_PATH="/usr/lib/node_modules/"; cd %s/; /tmp/nodeunit-master/bin/nodeunit %s/%s -t testStorageHandlerHasunlink' % (
                    self.target_iotivity_js_apis_dir,
                    self.target_iotivity_js_apis_dir,
                    self.iotivity_js_apis_files['storage_handler']
                   )
        )
        self.assertTrue('OK:' in api_output.strip().splitlines()[-1])


    @classmethod
    def tearDownClass(cls):
        '''
        Clean work.
        Clean all the files and directories that the tests may be used on target.
        @fn tearDownClass
        @param cls
        @return
        '''
        if os.path.exists('%s.tar' % cls.iotivity_js_apis_dir):
            os.remove('%s.tar' % cls.iotivity_js_apis_dir)
        os.system('rm -rf %s' % cls.nodeunit_tar)
        if os.path.exists(cls.nodeunit_zip) and not os.path.exists('/tmp/master.zip'):
            os.system('mv -f %s /tmp/' % (cls.nodeunit_zip))

        cls.tc.target.run('rm -f %s.tar' % cls.target_iotivity_js_apis_dir)
        cls.tc.target.run('rm -fr %s/' % cls.target_iotivity_js_apis_dir)
        cls.tc.target.run('rm -fr /tmp/nodeunit-master')
        cls.tc.target.run('rm -f /tmp/master.zip')


##
# @}
# @}
##

