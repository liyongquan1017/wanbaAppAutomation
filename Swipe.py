import time
from time import sleep
import setting
def profile():
    driver = setting.case('Android', '8.0.0', 'GWY0216B26002053', 'com.wodi.who', '.login.SplashActivity','10300','10300')
    try:
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        i = 1
        print("1")
        sleep(3)
        while i < 10000:
            sleep(0.5)
            driver.swipe(x / 2, y * 8 / 10, x / 2, y * 3 / 10, 200)
            sleep(0.5)
            driver.swipe(x / 2, y * 8 / 10, x / 2, y * 3 / 10, 200)
            sleep(0.5)
            driver.swipe(x / 2, y * 8 / 10, x / 2, y * 3 / 10, 200)
            sleep(0.5)
            driver.swipe(x / 2, y * 3 / 10, x / 2, y * 8 / 10, 200)
            sleep(0.5)
            driver.swipe(x / 2, y * 3 / 10, x / 2, y * 8 / 10, 200)
            sleep(0.5)
            driver.swipe(x / 2, y * 3 / 10, x / 2, y * 8 / 10, 200)
            # driver.swipe(x / 2, y * 8 / 10, x / 2, y * 7 / 10, 500)
            # driver.swipe(x / 2, y * 8 / 10, x / 2, y * 7 / 10, 500)
            # driver.swipe(x / 2, y * 8 / 10, x / 2, y * 7 / 10, 500)
            # driver.swipe(x / 2, y * 7 / 10, x / 2, y * 8 / 10, 500)
            # driver.swipe(x / 2, y * 7 / 10, x / 2, y * 8 / 10, 500)
            # driver.swipe(x / 2, y * 7 / 10, x / 2, y * 8 / 10, 500)
            # driver.swipe(x / 2, y * 3 / 10, x / 2, y * 8 / 10, 500)
            i += 1
            print(i)
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