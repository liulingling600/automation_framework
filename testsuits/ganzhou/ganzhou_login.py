import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.ganzhou.login_page import LoginPage

class GanzhouLogin(unittest.TestCase):
    def setUp(self):
        brower = BrowerEngine(self)
        self.driver = brower.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        loginpage = LoginPage(self.driver)
        loginpage.login_input("admin",'111111')
        loginpage.send_submit()


if __name__ == '__main__':
    unittest.main()