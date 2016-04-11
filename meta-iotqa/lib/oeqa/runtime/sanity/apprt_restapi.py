"""
@file apprt_restapi.py
"""

##
# @addtogroup sanity sanity
# @brief This is sanity component
# @{
# @addtogroup apprt_restapi apprt_restapi
# @brief This is apprt_restapi module
# @{
##

import subprocess
from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag

@tag(TestType='FVT', FeatureID='IOTOS-343')
class SanityTestRestApi(oeRuntimeTest):
    """
    @class SanityTestRestApi
    """

    def _run_curl_cmd(self):

        curl_cmd = ''.join([
                   'unset http_proxy; curl --noproxy "*" -s -o',
                   ' /dev/null -w %{http_code}',
                   ' --no-buffer http://%s:8000/api/oic/d' % (self.target.ip)])
        p = subprocess.Popen(curl_cmd,
            stdout = subprocess.PIPE,
            stderr = subprocess.STDOUT, shell=True)
        p.wait()
        ret = p.returncode
        output = p.stdout.read()
        return (ret, output)


    def test_restapi_available_by_remote(self):
        '''
        Send a HTTP request to the REST API server and see if 200 is returned.
        '''
        (returncode, output) = self._run_curl_cmd()
        self.assertEqual(output.strip(), '200')

##
# @}
# @}
##

