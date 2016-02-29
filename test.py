from autologin.autologin import AutoLogin

#url = 'http://w363zoq3ylux5rf5.onion/'
#username = 'handsomeshit'
#password = 'qq123456'
url = 'http://www.renren.com'
username = '15251769398'
password = 'nuaalk930826'
proxy_type = 'http'
proxy = 'http://47.88.6.231:9398'
al = AutoLogin()
cookies = al.auth_cookies_from_url(url, username, password,proxy_type,proxy)
print cookies
