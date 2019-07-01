import pytest
from page.app import APP

class Test_Login(object):

    @classmethod
    def setup_class(cls):
        # cls.homepage = APP.app_home()
        cls.profilepage = APP.app_home().gotoProfile()

    def setup_method(self):
        # self.loginpage = Test_Login.homepage.gotoProfile().gotoLogin()
        self.loginpage = Test_Login.profilepage.gotoLogin()

    @pytest.mark.parametrize("phone,code",[
        ('18561616262','1234'),
        ('18561616263','1234')
    ])
    def test_loginwrongphone(self,phone,code):
        self.loginpage.login_phone(phone,code)
        msg = self.loginpage.getErrorMsg()
        assert "验证码" in msg


    # def test_loginwrongphone(self):
    #     self.loginpage.login_phone("186616969671","1234")
    #     msg = self.loginpage.getErrorMsg()
    #     assert "验证码" in msg


    @pytest.mark.parametrize("account,password",[
        ('186616969671','12345678'),
        ('18661696967','12345678')
    ])
    def test_loginwrongaccout(self,account,password):
        self.loginpage.login_account(account,password)
        assert "错误" in self.loginpage.getErrorMsg()


    # def test_loginwrongaccout(self,):
    #     self.loginpage.login_account("186616969671",'12345678')
    #     assert "错误" in self.loginpage.getErrorMsg()

    def teardown_method(self):
        # self.loginpage.backward().backward()
        self.loginpage.backward()




