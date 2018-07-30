import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.ganzhou.home_page import HomePage

class AddProductionArchves(unittest.TestCase):

    def setUp(self):
        brower = BrowerEngine(self)
        self.driver = brower.open_browser(self)

    def tearDown(self):
        self.driver.quit()

    def test_click_add(self):
        homepage = HomePage(self.driver)
        homepage.click_btn(homepage.business_archives_manage)
        homepage.click_btn(homepage.producte_archives_manage)
        homepage.change_frame(homepage.iframe_2)
        homepage.click_btn(homepage.add)