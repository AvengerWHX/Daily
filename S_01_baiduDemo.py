from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC



driver = webdriver.Chrome()
try:
    driver.get('http://www.baidu.com')
    '''
       获取搜索框
       <input id="kw" name="wd" class="s_ipt" value="" maxlength="255" autocomplete="off">
    '''
    # 1. id定位
    input = driver.find_element_by_id('kw')
    # 2. name定位
    # input = driver.find_element_by_name('wd')
    # 3. class定位
    # input = driver.find_element_by_class_name('s_ipt')
    # 4. tag定位，每一个元素本质是一个tag，一个tag往往用来定义一类功能，所以通过tag识别某个元素的概率很低
    # 通过tag name定位百度的输入框与百度按钮会发现它们完全相同
    # input = driver.find_element_by_tag_name('input')
    # 7. XPath定位,xpath是一种在XML文档中定位元素的语言看做XML的一种实现，所以可以在web应用中定位元素
    # 7.1 XPath绝对路径定位
    # input = driver.find_element_by_xpath('html/body/div/div/div/div/div/form/span/input')
    # 7.2 XPath利用元素属性定位，//表示当前页面某个目录下，input表示定位元素的标签名，[@id='kw']表示这个元素的id属性值等于kw。
    # input = driver.find_element_by_xpath("//input[@id='kw']")
    # search_btn = driver.find_element_by_xpath("//input[@id='su']")
    # camera_btn = driver.find_element_by_xpath("//span[@class='soutu-btn']")
    # camera_btn.click()
    # 若不想指定标签名，则可以用星号代替
    # driver.find_element_by_xpath("//*[@class='bg s_btn']")
    # 7.3 层级与属性结合，如果一个元素本身没有可以唯一标识的属性值，可以找其上一级元素，若父元素没有可以利用的属性值，可以继续向上找父元素的父元素
    # driver.find_element_by_xpath(("//span[@class='bg s_ipt_wr']/input"))
    # driver.find_element_by_xpath("//form[@id='form']/span[2]/input")
    # 7.4 使用逻辑运算符，如果一个属性不能唯一的区分一个元素，可以使用逻辑运算符同时查找多个属性
    # driver.find_element_by_xpath("//input[@id='kw' and @class='su']/span/input")

    # 8. CSS定位



    '''
        获取搜索按钮
        <input type="submit" id="su" value="百度一下" class="bg s_btn">
    '''

    # search_btn = driver.find_element_by_id('su')
    # 报错InvalidSelectorException: Message: invalid selector: Compound class names not permitted，是因为包含多个相同class name的元素
    # search_btn = driver.find_element_by_class_name('bg s_btn')
    # 每一个元素本质是一个tag，一个tag往往用来定义一类功能，所以通过tag识别某个元素的概率很低
    # 通过tag name定位百度的输入框与百度按钮会发现它们完全相同
    # input = driver.find_element_by_tag_name('input')
    # 搜索框键入关键字
    input.send_keys('Heyson')


    # 点击“百度一下”按钮
    # search_btn.click()
    # enter键
    input.send_keys(Keys.ENTER)


    '''
        5.link定位：专门用来定位文本链接

        <a href="http://news.baidu.com" name="tj_trnews" class="mnav">新闻</a>
        <a href="https://www.hao123.com" name="tj_trhao123" class="mnav">hao123</a>
        <a href="http://map.baidu.com" name="tj_trmap" class="mnav">地图</a>
        <a href="http://v.baidu.com" name="tj_trvideo" class="mnav">视频</a>
        <a href="http://tieba.baidu.com" name="tj_trtieba" class="mnav">贴吧</a>
        <a href="http://xueshu.baidu.com" name="tj_trxueshu" class="mnav">学术</a>
    '''
    # a1 = driver.find_element_by_link_text("新闻")
    # 6. partial link定位，partial_link定位是对link定位的补充，有些文本链接会比较长，此时可以取文本链接的一部分定位
    # a1 = driver.find_element_by_partial_link_text('地图')
    # a1.click()

    wait=WebDriverWait(driver,10)
    wait.until(EC.presence_of_element_located((By.ID,"content_left")))
    # print(driver.current_url)
    # print(driver.get_cookies())
    print(driver.page_source)

finally:
    driver.close()

