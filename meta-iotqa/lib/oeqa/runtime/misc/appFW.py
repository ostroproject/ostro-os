from oeqa.oetest import oeRuntimeTest

class AppFwTest(oeRuntimeTest):

    """ App Framework testing """

    def test_sqlite_integration(self):

        """ test sqlite is integrated in image """

        (status,output) = self.target.run("rpm -qa | grep sqlite")
        self.assertEqual(status, 0, output)
