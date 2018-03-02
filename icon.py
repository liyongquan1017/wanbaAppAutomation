# coding = utf-8
from appium import webdriver
from time import sleep
import time
import setting
import os
def icon():
    driver = setting.case('Android', '8.0.0', 'GWY0216B26002053', 'com.wodi.who', '.login.SplashActivity','10300','10300')
    try:
        driver.find_element_by_android_uiautomator("text(\"福利社\")").click()
        driver.find_element_by_id('com.wodi.who:id/tv_honner').click()
        driver.keyevent(4)
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"福利社\")").click()
        driver.find_element_by_android_uiautomator("text(\"成长任务\")").click()
        driver.find_element_by_android_uiautomator("text(\"日常任务\")").click()
        driver.keyevent(4)
        # driver.find_element_by_android_uiautomator("text(\"后宫\")").click()
        # sleep(3)
        # driver.find_element_by_id('com.wodi.who:id/slave_not_intrinsting').click()
        # driver.find_element_by_android_uiautomator("text(\"后宫秘籍\")").click()
        driver.find_element_by_android_uiautomator("text(\"熟人房\")").click()
        driver.find_element_by_id('com.wodi.who:id/wb_right_action').click()
        driver.keyevent(4)
        driver.find_element_by_id('com.wodi.who:id/create_room_bg_iv').click()
        driver.keyevent(4)
        driver.find_element_by_id('com.wodi.who:id/search_room_bg_iv').click()
        driver.keyevent(4)
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"好友在玩\")").click()
        driver.keyevent(4)
        driver.quit()
    except Exception as e:
        print(e)
        shootFile = '/Users/wanba/Desktop/screeShoot'
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        shootScreemFile = shootFile + '/' + '失败' + now + '_' + 'icon.png'
        driver.get_screenshot_as_file(shootScreemFile)
        driver.quit()
        return False
    return True
if __name__ == '__main__':
    if (icon() == True):
        print("该条用例执行成功")
    else:
        print("该条用例执行失败")