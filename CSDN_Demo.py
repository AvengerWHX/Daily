from selenium import webdriver

def gethtml(url):
    loginurl='https://www.douban.com/'  #登录页面

    brower = webdriver.PhantomJS()
    brower.get(loginurl)    #请求登录页面
    brower.find_element_by_name('from_email').clear()   #获取用户名输入框，并清空里边的数据
    brower.find_element_by_name('from_email').send_keys(u'你的用户名')   #输入用户名
    brower.find_element_by_name('from_password').clear()    #获取密码框，并清空
    brower.find_element_by_name('from_password').send_keys(u'你的密码') #输入密码

    # 验证码手动处理,输入后，需要将图片关闭才能继续执行下一步
    captcha_link = brower.find_element_by_n