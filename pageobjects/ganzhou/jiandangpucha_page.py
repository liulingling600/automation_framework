from framework.base_page import BasePage
from selenium.webdriver.support.ui import Select

class JanDangPuCha(BasePage):
    testrusult = 'xpath=>//*[@id="datagrid-row-r2-2-0"]/td[2]/div'
    '''------------------企业信息----------------------'''
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
    #经营状态
    statu = 'id=>status'
    #企业联系人
    linkman = 'name=>a16lxr'
    linkman_phone = 'name=>a16sj'
    linkman_email = 'name=>a16dzyj'
    #保存
    save = 'xpath=>//*[@id="Btn"]/button[1]'
    #一级frame
    frame_1 = 'name=>iframe16'
    #二级frame
    frame_2 = 'name=>editFrame'
    #----------------------相关证件--------------------------
    credit_code = 'id=>zzbh0' #社会信用代码
    production_permit = 'xpath=>//*[@id="tabA1"]/tbody/tr[2]/td[2]/input[1]' #生产许可
    certify_authority = 'xpath=>//*[@id="tabA1"]/tbody/tr[2]/td[4]/input' #发证单位
    certify_date = 'name=>a4fzrq' #发证日期
    valid_until = 'name=>a4yxqz' # 有效期至
    save2 = 'xpath=>//*[@id="editBtn"]/button[1]'




    def choose_select(self,select,index):
        Select(self.find_element(select)).select_by_index(index)

    # 进入frame
    def change_frame(self, selector):
        self.to_frame(selector)