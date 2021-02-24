import json
from time import sleep
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By


class Test_chat_cc():

    def setup_method(self):
        chrome_args = webdriver.ChromeOptions()
        chrome_args.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=chrome_args)
        self.driver.get('https://work.weixin.qq.com/')

    # def test_cookie_cc(self):
    #     cookies = self.driver.get_cookies()
    #     print(cookies)
    #     with open("cc_cookies.json","w") as f:
    #         json.dump(cookies,f)
    def test_cookies_cc1(self):
        with open("./cc_cookies.json","r") as f:
            cookies_cc = json.load(f)
        for cookie in cookies_cc:
            self.driver.add_cookie(cookie)
        # self.driver.get('https://work.weixin.qq.com/')
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(3)
        self.driver.find_element_by_css_selector('#menu_customer > span').click()
        self.driver.find_element(By.CSS_SELECTOR)


    # def test_wait_cc1(self):

        # driver.implicitly_wait(5)
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')

        # self.driver.find_element_by_xpath('//*[@id="menu_customer"]/span').click()
        # self.driver.quit()

