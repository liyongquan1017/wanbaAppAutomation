# coding = utf-8
import os
import time
def logcat(testdir):
    now = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
    print(now)
    logcatname = testdir + now + '_' + 'logcat.log'
    print(logcatname)
    os.system('adb logcat -v time > ' + logcatname)