from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'
# desired_caps['appWaitActivity'] = 'com.android.calculator2'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

# 在模拟器上，根据元素text进行元素定位
driver.find_element_by_name("1").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("delete").click()
driver.find_element_by_name("9").click()
driver.find_element_by_name("5").click()
driver.find_element_by_name("+").click()
driver.find_element_by_name("6").click()
driver.find_element_by_name("=").click()

# 在模拟器上，根据元素的id进行元素定位
# driver.find_element_by_id("com.android.calculator2:id/digit_1").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
# driver.find_element_by_id("com.android.calculator2:id/del").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_9").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_5").click()
# driver.find_element_by_id("com.android.calculator2:id/op_add").click()
# driver.find_element_by_id("com.android.calculator2:id/digit_6").click()
# driver.find_element_by_id("com.android.calculator2:id/eq").click()

driver.quit()

# 华为Rio真机测试，安卓配置中不要添加任何配置，只在desired_caps中设置配置项即可

# from appium import webdriver
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0'
# desired_caps['deviceName'] = 'PJQDU15923001421'
# desired_caps['appPackage'] = 'com.android.calculator2'
# desired_caps['appActivity'] = '.Calculator'
#
# driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
#
# driver.find_element_by_id("com.android.calculator2:id/digit1").click()
# driver.find_element_by_id("com.android.calculator2:id/digit5").click()
# driver.find_element_by_id("com.android.calculator2:id/digit9").click()
# driver.find_element_by_id("com.android.calculator2:id/del").click()
# driver.find_element_by_id("com.android.calculator2:id/digit9").click()
# driver.find_element_by_id("com.android.calculator2:id/digit5").click()
# driver.find_element_by_id("com.android.calculator2:id/plus").click()
# driver.find_element_by_id("com.android.calculator2:id/digit6").click()
# driver.find_element_by_id("com.android.calculator2:id/equal").click()
#
# driver.quit()
