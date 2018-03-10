# coding = utf-8
import os
import time
import threading
import setting
import profile
import shoppingMalls
import icon
import logcat

is_task_finished = False

def task():
    profile.profile()
    shoppingMalls.shop()
    icon.icon()

def outLogcat():
    is_task_finished
    logcat.logcat('/Users/wanba/Desktop/Logcat/')
threading.Thread(target= task).start()
threading.Thread(target= outLogcat).start()

