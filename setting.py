# coding = utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
from time import sleep
def case(platformName,platformVersion,deviceName,appPackage,appActivity,userName,passWord):
        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.find_element_by_id('com.wodi.who:id/phone_login').click()
        driver.find_element_by_id('com.wodi.who:id/username_login').click()
        driver.find_element_by_id('com.wodi.who:id/input_username').click()
        driver.find_element_by_id('com.wodi.who:id/input_username').send_keys(userName)
        driver.hide_keyboard()
        driver.find_element_by_id('com.wodi.who:id/input_password').send_keys(passWord)
        driver.find_element_by_id('com.wodi.who:id/input_password').click()
        driver.find_element_by_id('com.wodi.who:id/input_username').click()
        driver.hide_keyboard()
        driver.find_element_by_id('com.wodi.who:id/complete').click()
        driver.implicitly_wait(10)
        return driver
driver = case('Android', '8.0.0', 'GWY0216B26002053', 'com.wodi.who', '.login.SplashActivity','10369','10369')
x = driver.get_window_size()['width']
y = driver.get_window_size()['height']
def swipDown(n):
        while n > 0:
                sleep(1)
                driver.swipe(x / 2, y * 8 / 10, x / 2, y * 3 / 10, 200)
                sleep(1)
                n = n - 1
def swipUp(n):
        while n > 0:
                sleep(2)
                driver.swipe(x / 2, y * 3 / 10, x / 2, y * 8 / 10, 200)
                sleep(2)
                n = n - 1










