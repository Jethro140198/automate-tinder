from selenium import webdriver
from time import sleep
from particulars import username, pw
import random

class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Jethro Leeroy\OneDrive\Desktop\chromedriver_win32\chromedriver.exe")
        self.likeStatus = 1

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(5)

        login_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/div/div[3]/span/div[1]/div/button')
        login_button.click()
        
        # Refer to note
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        mail_box = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        mail_box.send_keys(username)

        enter_button = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
        enter_button.click()

        sleep(3)

        pw_box = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw_box.send_keys(pw)

        log = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button')
        log.click()

        sleep(5)
        
        # Refer to note
        self.driver.switch_to.window(base_window)

        allow_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        allow_button.click()

        enable_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        enable_button.click()

        accept_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button')
        accept_button.click()

    def like(self):
        like_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    def dislike(self):
        dislike_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        dislike_button.click()

    def auto(self):
        while True:
            sleep(1)
            try:
                self.likeStatus = random.randint(0,1)
                if self.likeStatus == 1:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_pop()
                except Exception:
                    self.close_out()

    def close_pop(self):
        pop_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        pop_button.click()

    def close_out(self):
        out_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        out_button.click()

bot = TinderBot()
bot.login()
sleep(3)
bot.auto()
