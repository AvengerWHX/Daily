from appium import webdriver
import time

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'PJQDU15923001421'
# desired_caps['appPackage'] = 'com.cleanmaster.mguard_cn'
# desired_caps['appActivity'] = 'com.keniu.security.main.MainActivity'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
desired_caps['autoLaunch'] = 'false'



driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

'''
    其实上下文的操作主要针对于混合应用。混合应用简单来说就是APP用里面嵌入网页。Android上的浏览器就属于混合应用。
'''
# driver.context()
# print(driver.context())

# driver.start_activity('com.cleanmaster.mguard_cn','com.cleanmaster.meplugin.settings.ui.SettingsActivity')
driver.remove_app('com.cleanmaster.mguard_cn')
driver.install_app(r"C:\Users\Administrator\Desktop\插件\CleanMaster-v60931007-bd2-100005-uL.apk")
driver.launch_app()

driver.current_activity
print('当前的activity为：'+str(driver.current_activity))

time.sleep(10)

driver.quit()




