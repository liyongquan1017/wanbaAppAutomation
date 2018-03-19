# coding = utf-8
from appium import webdriver
from time import sleep
import time
import setting
# profile 页
driver = setting.driver
def profile():
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
        sleep(1)
        #滑动页面
        setting.swipUp(3)
        setting.swipDown(2)
        #进入照片墙
        driver.find_element_by_android_uiautomator("text(\"照片墙\")").click()
        # 滑动页面
        setting.swipUp(3)
        setting.swipDown(2)
        driver.keyevent(4)
        sleep(2)
        driver.keyevent(4)
        sleep(2)
        setting.swipUp(1)
        # 进入徽章
        driver.find_element_by_id('com.wodi.who:id/honors_layout').click()
        driver.keyevent(4)
        driver.keyevent(4)
        # 点击首页个人头像
        driver.find_element_by_id('com.wodi.who:id/iv_user_icon').click()
        # 进入礼物
        sleep(2)
        setting.swipUp(1)
        sleep(1)
        driver.find_element_by_id('com.wodi.who:id/gift_cover').click()
        driver.find_element_by_android_uiautomator("text(\"收到礼物\")").click()
        # 滑动页面
        sleep(2)
        setting.swipUp(3)
        setting.swipDown(2)
        sleep(1)
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

