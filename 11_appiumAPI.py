from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'PJQDU15923001421'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

'''
    appium的常用API方法
'''

# 安装app，安装应用到设备中去，需要apk包的路径
driver.install_app("")

# 卸载app，传入包名
driver.remove_app("")

# 关闭app,默认关闭当前打开的应用，所以不需要入参，这个方法并非真正的关闭应用，相当于按home键将应用置于后台，可以通过launchApp()再次启动
driver.close_app()

# 启动应用
driver.launch_app()

# 检查应用是否安装。需要传参应用包的名字。返回结果为Ture或False
driver.is_app_installed()

# 将当前活跃的应用程序发送到后台。这个方法需要入参，需要指定应用置于后台的时长。
driver.background_app()

# 重置当前被测程序到初始化状态。该方法不需要入参
driver.reset()

# 当前activity
driver.current_activity
print(str(driver.current_activity))


driver.quit()




