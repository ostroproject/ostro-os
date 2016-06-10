from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag


@tag(TestType = 'FVT', FeatureID = 'IOTOS-1546')
class Test_Intel_Graphics_lib(oeRuntimeTest):
   ''' Test Intel Graphics lib integrated '''
   lib_info = {
                 "libDRM" : ["/usr/lib/libdrm.so"],
                 "xf86-video-intel" : ["/usr/lib/xorg/modules/drivers/intel_drv.so"],
                 "Mesa 3D" : [
                               "/usr/lib/libGL.so",
                               "/usr/lib/libGLESv2.so"
                             ],
                 "VAAPI" : [
                              "/usr/lib/libva.so",
                           ],

              }
   def _test_integration(self,lib_path_list):       
       ''' Check library integration '''
       for lib_path in lib_path_list:
           (status,output) = self.target.run("ls %s" % lib_path)
           self.assertTrue(status == 0 , "%s is not in image: %s" 
                                           % (lib_path, output))
   def test_libDRM_integration(self):
       ''' Check libDRM integration '''
       self._test_integration(self.lib_info["libDRM"])

   def test_xf86_video_intel_integration(self):
       ''' Check xf86-video-intel integration '''
       self._test_integration(self.lib_info["xf86-video-intel"])

   def test_Mesa_3D_integration(self):
       ''' Check Mesa 3D integration '''
       self._test_integration(self.lib_info["Mesa 3D"])

   def test_VAAPI_integration(self):
       ''' Check VAAPI integration '''
       self._test_integration(self.lib_info["VAAPI"])
