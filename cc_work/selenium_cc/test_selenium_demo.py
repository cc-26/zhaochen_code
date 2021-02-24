from time import sleep
from selenium import webdriver


# class Test_cc_selenium():
#
#     def setup(self):
#         self.driver = webdriver.Chrome()
#
#     def teardown(self):
#         self.driver.quit()
#
#     def test_selenium_cc1(self):
#         self.driver.get('https://www.baidu.com/')
#         sleep(3)
#         self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('忱')
#         sleep(3)
#         self.driver.find_element_by_xpath('//*[@value="百度一下"]').click()
#         sleep(3)
#         self.driver.close()


#
def cookie_cc():
    chrome_args = webdriver.ChromeOptions()
    chrome_args.debugger_address = "127.0.0.1:9222"
    driver = webdriver.Chrome(options=chrome_args)
    cookies = driver.get_cookies()
    print(cookies)
