import unittest
from framework.browser_engine import BrowerEngine
from pageobjects.ganzhou.home_page import HomePage
from testsuits.ganzhou.ganzhou_login import GanzhouLogin
from pageobjects.ganzhou.jiandangpucha_page import JanDangPuCha
import time
from framework.logger import Logger

class AddProduction(unittest.TestCase):
    logger = Logger(logger="AddProduction").getlog()
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
        self.logger.info("开始填入企业信息")
        #填入企业信息
        jandangpucha = JanDangPuCha(self.driver)
        self.driver = self.add_business_info(jandangpucha,'用例测试','赣州章贡区','田野'
                               ,5,1,'赣州市章贡区长岭南路','田野')
        time.sleep(1)
        self.logger.info('填入企业信息完毕，开始填入相关证照')
        # 填入相关证照
        self.driver = self.add_relation_license(self.driver,'11111111','12345678910','赣州市工商局','2018-08-02','2022-08-2')
        self.logger.info('填写相关证照完毕，已保存')
        self.driver.sleep(1)
        self.driver.click(HomePage.producte_archives_manage)
        self.driver.to_frame(HomePage.iframe_production)
        self.driver.sleep(1)
        self.logger.info('判断是否添加成功')
        producte_name = self.driver.find_element(JanDangPuCha.testrusult).text
        self.assertEqual(producte_name,'用例测试','添加失败')

    #填入企业信息
    def add_business_info(self,driver,business_name,business_addr,principal,
                         own_addrs_city_index,own_addrs_area_index,product_addr,
                         linkman):
        time.sleep(2)
        driver.to_frame(JanDangPuCha.frame_1)
        time.sleep(1)
        driver.change_frame(JanDangPuCha.frame_2)
        time.sleep(2)
        driver.input(JanDangPuCha.business_name,business_name)
        driver.input(JanDangPuCha.business_addr,business_addr)
        driver.input(JanDangPuCha.principal,principal)
        driver.choose_select(JanDangPuCha.own_addrs_city,own_addrs_city_index)
        driver.choose_select(JanDangPuCha.own_addrs_area, own_addrs_area_index)
        driver.input(JanDangPuCha.product_addr,product_addr)
        driver.input(JanDangPuCha.linkman,linkman)
        driver.click(JanDangPuCha.save)
        time.sleep(1)
        driver.back_from_frame()
        return driver

    #填入相关证照
    def add_relation_license(self,driver,credit_code,production_permit,
                             certify_authority,certify_date,valid_until
                             ):
        driver.to_frame(JanDangPuCha.frame_1)
        time.sleep(1)
        driver.change_frame(JanDangPuCha.frame_2)
        time.sleep(2)
        driver.input(JanDangPuCha.credit_code, credit_code)
        driver.input(JanDangPuCha.production_permit, production_permit)
       # driver.click(JanDangPuCha.certify_authority)
        driver.sleep(1)
        driver.input(JanDangPuCha.certify_authority, certify_authority)
        # driver.input(JanDangPuCha.certify_authority, certify_authority) #操作的元素鼠标点击变更样式，导致代码不能看见，通过js操作Dom适应场景
        #js = "document.getElementsByName(\"a4fzdw\")[0].value=\"赣州工商局\";"
        #  driver.execute_js(js)
        # js = "document.getElementById('txtBeginDate').removeAttribute('readonly')"  # 1.原生js，移除属性
        # js1 = "$('input[name=a4fzrq]').removeAttr('readonly')"
        js1 = "var setDate=document.getElementsByName(\"a4fzrq\")[0];setDate.removeAttribute(\"readonly\");"
        # js2 = "$('input[name=a4yxqz]').removeAttr('readonly')"  # 2.jQuery，移除属性
        js2 = "document.getElementsByName(\"a4yxqz\")[0].value=\"2018-08-04\";"
        # js = "$('input[id=txtBeginDate]').attr('readonly',false)"  # 3.jQuery，设置为false
        # js = "$('input[id=txtBeginDate]').attr('readonly','')"  # 4.jQuery，设置为空（同3）
        driver.execute_js(js1)
        time.sleep(1)
        driver.execute_js(js2)
        time.sleep(1)
       # driver.input(JanDangPuCha.certify_date, certify_date)
        #driver.input(JanDangPuCha.valid_until, valid_until)
        driver.click(JanDangPuCha.save2)
        driver.back_from_frame()
        #self.assertEqual()
        return driver

    #设置品种明细
    def add_variety_info(self,driver):
        pass
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