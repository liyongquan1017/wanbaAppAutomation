# coding = utf-8
from appium import webdriver
from time import sleep
import time
import setting
def profile():
    driver = setting.case('Android', '8.0.0', 'GWY0216B26002053', 'com.wodi.who', '.login.SplashActivity')
    try:
        driver.find_element_by_id('com.wodi.who:id/phone_login').click()
        sleep(3)
        driver.find_element_by_id('com.wodi.who:id/username_login').click()
        sleep(3)
        driver.find_element_by_id('com.wodi.who:id/input_username').send_keys('10300')
        sleep(3)
        driver.find_element_by_id('com.wodi.who:id/input_password').send_keys('10300')
        sleep(3)
        driver.find_element_by_id('com.wodi.who:id/complete').click()
        if (driver.find_element_by_id('com.wodi.who:id/complete')):
            print("2")
        else:
            print('1')
    except Exception as e:
        print(e)
        shootFile = '/Users/wanba/Desktop/screeShoot'
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        shootScreemFile = shootFile + '/' + '失败' + now + '_' + 'profile.png'
        driver.get_screenshot_as_file(shootScreemFile)
        driver.quit()
        return False
    return True
if __name__ == '__main__':
    if (profile() == True):
        print("该条用例执行成功")
    else:
        print("该条用例执行失败")