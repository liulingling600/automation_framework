from framework.base_page import BasePage

class LoginPage(BasePage):
    username = 'id=>j_username'
    password = 'id=>j_password'
    submit_btn = 'class_name=>b_login'

    def login_input(self,user,word):
        self.input(self.username,user)
        self.input(self.password,word)

    def send_submit(self):
        self.click(self.submit_btn)
