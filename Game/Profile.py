# coding = utf-8
from appium import webdriver
from time import sleep
import time
import setting
# profile 页
def profile():
    driver = setting.case('Android', '8.0.0', 'GWY0216B26002053', 'com.wodi.who', '.login.SplashActivity','10369','10369')
    try:
        # 点击首页个人头像
        driver.find_element_by_id('com.wodi.who:id/iv_user_icon').click()
        # 点击profile页 编辑按钮
        driver.find_element_by_id('com.wodi.who:id/setting_btn').click()
        # 返回
        driver.keyevent(4)
        # 进入守护profile页
        driver.find_element_by_id('com.wodi.who:id/protect_avatar').click()
        driver.keyevent(4)
        # 进入后宫（由于后宫是通过android fragment布局，目前一些元素无法获取，暂无法操作 ）
        # driver.find_element_by_id('com.wodi.who:id/tv_slave_count').click()
        # driver.keyevent(4)
        # 进入相册
        driver.find_element_by_id('com.wodi.who:id/album').click()
        driver.keyevent(4)
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        sleep(1)
        driver.swipe(x / 2, y * 8 / 10, x / 2, y * 3 / 10, 200)
        # 进入徽章
        driver.find_element_by_id('com.wodi.who:id/honors_layout').click()
        driver.keyevent(4)
        # 进入礼物
        driver.find_element_by_id('com.wodi.who:id/gift_layout').click()
        driver.find_element_by_android_uiautomator("text(\"收到礼物\")").click()
        driver.find_element_by_android_uiautomator("text(\"月贡献榜\")").click()
        driver.keyevent(4)
        driver.quit()
    except Exception as e:
        print(e)
        shootFile = '/Users/wanba/Desktop/screeShoot'
        now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        shootScreemFile = shootFile +'/' + '失败'+ now + '_' + 'profile.png'
        driver.get_screenshot_as_file(shootScreemFile)
        driver.quit()
        print('profile 失败')
        return False
    print('profile 成功')
    return True
if __name__=='__main__':
    if(profile()==True):
        print("该条用例执行成功")
    else:
        print("该条用例执行失败")

