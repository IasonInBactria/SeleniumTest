# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import lxml
import time

driver = webdriver.Firefox()
driver.maximize_window()
# driver.get("http://www.bjguahao.gov.cn/index.htm")

# 直接跳转到北医三院页面
puh3_page = driver.get('http://www.bjguahao.gov.cn/hp/appoint/142.htm')
# 选择医院（北医三院）
# haidian_click = driver.find_element_by_xpath('//li[@class="index_c_ks_rb" and a/text()="海淀区"]')
# # 不能直接点击，需要执行JS脚本
# driver.execute_script('arguments[0].click();', haidian_click)
# time.sleep(1)
# # 页面中有多个北医三院，必须从浏览器中利用网页查看工具拷贝完整的XPath路径
# driver.find_element_by_xpath('//div[@id="index_c_left"]/div/div[2]/div[1]/div[2]/div[7]/dl[1]/dd/h2/a').click()
# # 选择口腔治疗号
# print driver.page_source
# 填写用户名密码，自动登录
login_btn = driver.find_element_by_xpath('//a[@class="db_denglu"]')
login_btn.click()
phone_no = driver.find_element_by_id('mobileQuickLogin')
phone_no.send_keys('15810538816')
password = driver.find_element_by_id('pwQuickLogin')
password.send_keys('gyang0205006')
send_login_btn = driver.find_element_by_id('quick_login')
send_login_btn.click()
time.sleep(1)
oral_dep = driver.find_element_by_xpath('//div[@class="kfyuks"]/div[@class="kfyuks_left"]/div[4]/div[2]/div/ul/li[5]/a')
oral_dep.click()
time.sleep(5)

# 选择可预约号源
while True:
    cur_element = driver.find_elements_by_xpath('//td[@class="ksorder_kyy"]')
    if len(cur_element) <= 0:
        # 没有号源，刷新页面
        driver.refresh()
        time.sleep(1)
    else:
        cur_element[0].click()
        time.sleep(1)
        driver.find_elements_by_xpath('//a[@class="ksorder_dr1_syhy"]')[0].click()
        time.sleep(1)
        driver.find_element_by_id('btnSendCodeOrder').click()
        time.sleep(1)
        driver.switch_to.alert.accept()
        break




