import time

from page.app import APP

profile = APP.app_home().gotoProfile()
print(profile)
login = profile.gotoLogin()
login.login_phone("1234678901","1234")
print(login.getErrorMsg())
profile = login.backward()
time.sleep(10)
profile.gotoLogin().login_phone("1234678901","1234")