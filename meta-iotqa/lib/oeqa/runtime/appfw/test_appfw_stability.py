from oeqa.oetest import oeRuntimeTest
from oeqa.utils.decorators import tag
from test_appfw import App

class AppFWStbTest(oeRuntimeTest):

    node_app_name = 'iodine-nodetest'
    python_app_name = 'foodine-pythontest'

    def _test_appFW_stability_app_start_stop_many_times(self,name):
        '''start/stop for many times'''
        times = 500
        app = App(self.target)
        for _ in range(times):
            self.assertTrue(app.startApp(name))
            self.assertTrue(app.stopApp(name))

    def test_appFW_stability_node_app_start_stop(self):
        ''' start/stop node app for many times '''
        self._test_appFW_stability_app_start_stop_many_times(self.node_app_name)

    def test_appFW_stability_python_app_start_stop(self):
        ''' start/stop python app for many times '''
        self._test_appFW_stability_app_start_stop_many_times(self.python_app_name)
