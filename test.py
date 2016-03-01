from autologin.autologin import AutoLogin

#url = 'http://w363zoq3ylux5rf5.onion/'
#username = 'handsomeshit'
#password = 'qq123456'
url = 'http://www.renren.com'
username = ''
password = ''
proxy_type = ''
proxy = ''
al = AutoLogin()
#cookies = al.auth_cookies_from_url(url, username, password)
cookies = al.auth_cookies_from_url(url, username, password,proxy_type,proxy)
print cookies
