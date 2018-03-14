# coding = utf-8
import setting
import time
from time import sleep
# profile 页
driver = setting.driver
sleep(2)
def profile():
    try:
        #任务签到
        driver.find_element_by_android_uiautomator("text(\"任务签到\")").click()
        driver.find_element_by_id('com.wodi.who:id/tv_honner').click()
        sleep(1)
        setting.swipUp(2)
        setting.swipDown(1)
        driver.keyevent(4)
        sleep(1)
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"任务签到\")").click()
        driver.find_element_by_id('com.wodi.who:id/btn_enter').click()
        driver.keyevent(4)
        driver.keyevent(4)
        #打卡
        driver.find_element_by_android_uiautomator("text(\"打卡\")").click()
        sleep(1)
        setting.swipRight(1)
        sleep(1)
        setting.swipLeft(1)
        sleep(1)
        driver.keyevent(4)
        driver.keyevent(4)
        driver.find_element_by_android_uiautomator("text(\"好友在玩\")").click()
        sleep(2)
        driver.keyevent(4)
        sleep(1)
        driver.find_element_by_android_uiautomator("text(\"熟人房\")").click()
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/create_room_bg_iv').click()
        driver.keyevent(4)
        sleep(2)
        driver.find_element_by_id('com.wodi.who:id/search_room_bg_iv').click()
        driver.keyevent(4)
        sleep(3)
        driver.find_element_by_id('com.wodi.who:id/wb_right_action').click()
        driver.find_element_by_android_uiautomator("text(\"1个月产权(428钻石)\")").click()
        driver.find_element_by_id('com.wodi.who:id/input').send_keys('我的包间')
        driver.find_element_by_id('com.wodi.who:id/button_accept').click()
        sleep(2)
        setting.swipUp(3)
        setting.swipDown(3)
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