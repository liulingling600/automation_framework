from framework.base_page import BasePage
from selenium.webdriver.support.ui import Select

class JanDangPuCha(BasePage):
    business_name = 'id=>aqymc'
    business_addr = 'id=>azs'
    #日常监督管理机构
    supervision ='id=>deptId_name'
    #法定负责人
    principal = 'id=>a3xm'
    #所属区域
    own_addrs_city = 'id=>acity' #市
    own_addrs_area = 'id=>aarea' #区、县
    #生产地址
    product_addr ='id=>axxdz'
    #企业电话
    business_phone = 'id=>alxdh'