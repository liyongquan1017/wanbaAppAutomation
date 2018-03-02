# coding = utf-8
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os
def case(platformName,platformVersion,deviceName,appPackage,appActivity,userName,passWord):
        desired_caps = {}
        desired_caps['platformName'] = platformName
        desired_caps['platformVersion'] = platformVersion
        desired_caps['deviceName'] = deviceName
        desired_caps['appPackage'] = appPackage
        desired_caps['appActivity'] = appActivity
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.wodi.who:id/phone_login').click()
        driver.find_element_by_id('com.wodi.who:id/username_login').click()
        driver.find_element_by_id('com.wodi.who:id/input_username').click()
        driver.find_element_by_id('com.wodi.who:id/input_username').send_keys(userName)
        driver.hide_keyboard()
        driver.find_element_by_id('com.wodi.who:id/input_password').send_keys(passWord)
        driver.find_element_by_id('com.wodi.who:id/complete').click()
        return driver



