from framework.base_page import BasePage


class HomePage(BasePage):
    # 左边导航栏企业档案管理
    business_archives_manage = 'xpath=>//*[@id="side-menu"]/li[4]/a/span[1]'
    # 生产企业档案管理
    producte_archives_manage = 'link_text=>生产企业档案管理'
    # 流通企业档案管理
    liutong_archives_manage = 'link_text=>流通企业档案管理'
    # 餐饮企业档案管理
    canyin_archives_manage = 'link_text=>餐饮企业档案管理'
    # 小作坊企业档案管理
    xiaozuofang_archives_manage = 'link_text=>小作坊档案管理'
    # 小餐饮企业档案管理
    xiaocanyin_archives_manage = 'link_text=>小餐饮档案管理'
    # 小作坊企业档案管理
    xiaoshiza_archives_manage = 'link_text=>小食杂档案管理'

    # 添加按钮,在iframe句柄里，点击要先切换句柄
    # add = 'xpath=>//*[@id="btnadd"]/span/span[1]'
    add = 'xpath=>//*[@id="btnadd"]/span/span[2]'
    iframe_production = 'name=>iframe15'
    iframe_liutong = 'name=>iframe16'

    # 点击事件
    def click_btn(self, selector):
        self.click(selector)

    # 进入frame
    def change_frame(self, selector):
        self.to_frame(selector)

    # 退出frame
    def back_to_defualt_page(self):
        self.back_from_frame()