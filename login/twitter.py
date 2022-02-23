"""
‎Created on Tue Feb 22 ‏‎00:08:28 2022

@author: yiabatay

For "chromedriver.exe", check and install the current version here "https://chromedriver.chromium.org/"
"""

from twitterUserInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Twitter:
    def __init__(self, username, password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'en,en_US'})
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://twitter.com/i/flow/login")
        time.sleep(2)

        #username
        usernameInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[5]/label/div/div[2]/div/input")
        usernameInput.send_keys(self.username)

        #next
        btnNext = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[6]/div")
        btnNext.click()
        time.sleep(2)

        #password
        passwordInput = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[3]/div/label/div/div[2]/div[1]/input")        
        passwordInput.send_keys(self.password)

        #submit
        btnSubmit = self.browser.find_element_by_xpath("//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div")
        btnSubmit.click()
        time.sleep(2)

"""
ans = input("want to use another account (y/n): ")
if(ans == 'y'):
    username = input("username: ")
    password = input("password: ")
"""

twitter = Twitter(username, password)
#login
twitter.signIn()
