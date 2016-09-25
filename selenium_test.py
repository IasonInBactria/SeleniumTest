# -*- coding: UTF-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('D:/WebDrivers/chromedriver.exe')
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
print driver.page_source

import requests
from lxml import html


# class CrawlerFor114:
#
#     __doc__ = '''爬取114网站信息，完成模拟登录，预约挂号等功能'''
#
#     def __init__(self, url, option = 'print_data_out', src_tag=False):
#
#
#         self.option = option
#         self.url = url
#         self.header = {}
#         self.header['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
#         self.header['Host'] = 'www.bjguahao.gov.cn'
#         self.header['Refer'] = 'http://www.bjguahao.gov.cn/hp/appoint/142.htm'
#         self.cookie = {'Hm_lvt_bc7eaca5ef5a22b54dd6ca44a23988fa': '1473298353,1473298975,1473300406,1473314010',
#                        'JSESSIONID': 'FC1151C1B1410FA437166E183B0654FB',
#                        'SESSION_COOKIE': '3cab1829cea36cdbceb37f7e',
#                        'Hm_lpvt_bc7eaca5ef5a22b54dd6ca44a23988fa': '1473314034'
#                         }
#
#     def send_request(self):
#
#         start_url = self.url
#         try:
#             ret = requests.get(start_url, cookies=self.cookie, headers=self.header)
#         except requests.RequestException, e:
#             print 'chaxunshibai '
#             print e.strerror
#             print ret.status_code
#
#         if ret.status_code == 200:
#             print 'success!'
#         else:
#             print('login failed! status code:%d\n' % ret.status_code)
#             return
#
#         html_content = ret.text
        # print html_content + '\n'
        # self.process_xpath_source(html_content)

    # def process_xpath_source(self, source):
    #     if len(source) <= 0:

    #         return
    #     else:
    #         xpath_tree = html.fromstring(source)

    #         print '*' * 20
    #         self.user_name = xpath_tree.xpath('//a[@class="name"]/text()')[0].encode('utf-8')

    #         try:
    #             self.user_location = xpath_tree.xpath('//span[@class="location item"]/@title')[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_gender = xpath_tree.xpath('//span[@class="item gender"]/i/@class')[0].encode('utf-8')
    #             if 'female' in self.user_gender:
    #                 self.user_gender = 'female'
    #             else:
    #                 self.user_gender = 'male'

    #         except:
    #             pass
    #         try:
    #             self.user_employment = xpath_tree.xpath('//span[@class="employment item"]/@title')[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_profession = xpath_tree.xpath('//span[@class="education-extra item"]/@title')[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_school = xpath_tree.xpath('//span[@class="education item"]/@title')[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_major = xpath_tree.xpath('//span[@class="education-extra item"]/@title')[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_info = xpath_tree.xpath("//span[@class='bio']/@title")[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_introduction = xpath_tree.xpath('//span[@class="content"]/text()')[0].encode('utf-8')

    #         except:
    #             pass
    #         try:
    #             self.user_weibo_addr = xpath_tree.xpath('//a[@class="zm-profile-header-user-weibo"]/@href')[0].encode('utf-8')

    #         except:
    #             pass
    #

    #
    #         try:
    #             self.user_followees_num = int(xpath_tree.xpath('//a[@href="/people/' + self.user_id +'/followees"]/strong/text()')[0].encode('utf-8'))

    #         except:
    #             pass
    #         try:
    #             self.user_followers_num = int(xpath_tree.xpath('//a[@href="/people/' + self.user_id +'/followers"]/strong/text()')[0].encode('utf-8'))

    #         except:
    #             pass
    #         try:
    #             self.user_agree_num = int(xpath_tree.xpath('//span[@class="zm-profile-header-user-agree"]/strong/text()')[0].encode('utf-8'))

    #         except:
    #             pass
    #         try:
    #             self.user_thank_num = int(xpath_tree.xpath('//span[@class="zm-profile-header-user-thanks"]/strong/text()')[0].encode('utf-8'))

    #         except:
    #             pass
    #         print '*' * 25

    #
    #         if self.src_tag is True:
    #             user_followee_list = xpath_tree.xpath('//div[@class="zm-profile-card zm-profile-section-item zg-clear no-hovercard"]/a/@title')
    #             print len(user_followee_list)

# if __name__ == '__main__':
#     department_dict = {'口腔治疗号':'142-200001644', '泌尿外科':'142-200039550'}
#     htm_suffix = ''
#
#     while True:
#         print '请输入预约科室：'
#         department_input = raw_input()
#         for item in department_dict.keys():
#             if item == department_input:
#                 htm_suffix = department_dict[item]
#         if len(htm_suffix) <= 0:
#             print '未查询到相关科室，请重新输入！'
#         else:
#             start_url = 'http://www.bjguahao.gov.cn/dpt/appoint/' + htm_suffix + '.htm'
#             crawler = CrawlerFor114(start_url)
#             crawler.send_request()
#             break
