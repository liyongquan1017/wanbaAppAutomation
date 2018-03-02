# coding = utf-8
import os
import time
import threading
import setting
import profile
import shoppingMalls
import icon
import logcat
def task():
    profile.profile()
    shoppingMalls.shop()
    icon.icon()
def outLogcat():
    logcat.logcat('/Users/wanba/Desktop/Logcat/')
threading.Thread(target= task).start()
threading.Thread(target= outLogcat).start()

