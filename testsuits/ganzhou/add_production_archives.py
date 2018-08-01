import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.ganzhou.home_page import HomePage
from testsuits.ganzhou.ganzhou_login import GanzhouLogin
from pageobjects.ganzhou.jiandangpucha_page import JanDangPuCha
import time

class AddProduction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        brower = BrowerEngine(cls)
        cls.driver = brower.open_browser(cls)
        GanzhouLogin.test_login(cls)


    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    def test_product_add_1(self):
        homePage = HomePage(self.driver)
        time.sleep(2)
        homePage.click_btn(homePage.business_archives_manage)
        time.sleep(1)
        homePage.click_btn(homePage.producte_archives_manage)
        time.sleep(1)
        homePage.change_frame(homePage.iframe_production)
        time.sleep(2)
        homePage.click_btn(homePage.add)
        homePage.back_from_frame()
        jandangpucha = JanDangPuCha(self.driver)
        time.sleep(2)
        #填入企业信息
        jandangpucha.to_frame(jandangpucha.frame_1)
        time.sleep(1)
        jandangpucha.change_frame(jandangpucha.frame_2)
        time.sleep(1)
        jandangpucha.input(jandangpucha.business_name,'用例测试')
        jandangpucha.input(jandangpucha.business_addr,'贵阳市观山湖')
        jandangpucha.input(jandangpucha.principal,'田野')
        jandangpucha.choose_select(jandangpucha.own_addrs_city,5)
        jandangpucha.choose_select(jandangpucha.own_addrs_area, 0)
        jandangpucha.input(jandangpucha.product_addr,'用例测试')
        jandangpucha.input(jandangpucha.linkman,'田野')
        jandangpucha.click(jandangpucha.save)
        time.sleep(2)
        homePage.back_from_frame()
        time.sleep(3)
        #填入相关证照
        jandangpucha.to_frame(jandangpucha.frame_1)
        time.sleep(1)
        jandangpucha.change_frame(jandangpucha.frame_2)
        time.sleep(1)
        jandangpucha.input(jandangpucha.credit_code,'111111111111')
        jandangpucha.input(jandangpucha.production_permit,'1234567891011')
        jandangpucha.input(jandangpucha.certify_authority,'赣州市工商局')
        jandangpucha.input(jandangpucha.certify_date,'2018-08-01 ')
        jandangpucha.input(jandangpucha.valid_until,'2022-08-01')
        jandangpucha.click(jandangpucha.save2)






    def test_liutong_add_2(self):
        homePage = HomePage(self.driver)
        time.sleep(2)
        homePage.click_btn(homePage.business_archives_manage)
        time.sleep(1)
        homePage.click_btn(homePage.liutong_archives_manage)
        time.sleep(1)
        homePage.change_frame(homePage.iframe_liutong)
        time.sleep(2)
        homePage.click_btn(homePage.add)

if __name__ == '__main__':
    unittest.main()