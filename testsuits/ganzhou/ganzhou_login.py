import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.ganzhou.login_page import LoginPage

import time

class GanzhouLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        brower = BrowerEngine(cls)
        cls.driver = brower.open_browser(cls)

    def tearDown(self):
        self.driver.quit()


    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.login_input("admin",'111111')
        loginpage.send_submit()

        return self.driver



if __name__ == '__main__':
    unittest.main()