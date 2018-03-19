# coding = utf-8
from appium import webdriver
from time import sleep
import time
import setting
# profile 页
driver = setting.driver
def profile():
    try:
        # 点击钻石进入商城
        driver.find_element_by_id('com.wodi.who:id/tv_diamond').click()
        driver.keyevent(4)
        # 点击金币进入商城
        driver.find_element_by_id('com.wodi.who:id/tv_coin').click()
        driver.keyevent(4)
        # 进入商城购买钻石
        driver.find_element_by_id('com.wodi.who:id/tv_coin').click()
        driver.find_element_by_android_uiautomator("text(\"购买钻石\")").click()
        driver.find_element_by_android_uiautomator("text(\"¥6\")").click()
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"¥18\")").click()
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"¥88\")").click()
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"¥388\")").click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/vip').click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/vip').click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/speak').click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/speak').click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/comment').click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/comment').click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/message').click()
        driver.find_element_by_id('com.wodi.who:id/message').send_keys('Hell0,World')
        driver.hide_keyboard()
        driver.find_element_by_android_uiautomator("text(\"确认购买\")").click()
        driver.keyevent(4)
        sleep(1)
        driver.find_element_by_android_uiautomator("text(\"¥388\")").click()
        driver.find_element_by_android_uiautomator("text(\"取消\")").click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/button_cancel').click()
        sleep(1)
        driver.keyevent(4)
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/button_accept').click()
        sleep(1)
        driver.find_element_by_android_uiautomator("text(\"兑换\")").click()
        driver.find_element_by_android_uiautomator("text(\"400\")").click()
        driver.find_element_by_id('com.wodi.who:id/cancel_excahnge').click()
        driver.find_element_by_android_uiautomator("text(\"400\")").click()
        driver.find_element_by_id('com.wodi.who:id/sure_excahnge').click()
        driver.keyevent(4)
        driver.find_element_by_id('com.wodi.who:id/tv_coin').click()
        driver.find_element_by_id('com.wodi.who:id/backpack_layout_icon').click()
        driver.keyevent(4)
        driver.keyevent(4)
        driver.quit()
    except Exception as e:
        print(e)
        shootFile = '/Users/wanba/Desktop/screeShoot'
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        shootScreemFile = shootFile + '/' + '失败' + now + '_' + 'profile.png'
        driver.get_screenshot_as_file(shootScreemFile)
        driver.quit()
        print('profile 失败')
        return False
    print('profile 成功')
    return True


if __name__ == '__main__':
    if (profile() == True):
        print("该条用例执行成功")
    else:
        print("该条用例执行失败")