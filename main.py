from tkinter import *
from tkinter.ttk import *
import os
import threading
import subprocess
import time
import yaml

with open('xxhelper/config.yaml',encoding='utf-8') as file1:
    data = yaml.load(file1,Loader=yaml.FullLoader)#读取yaml文件
    print(data[0]['appname'])
    
argument = '...'

appname = data[0]['appname']
ms0 = data[0]['ms0']
ms1 = data[0]['ms1']
ms2 = data[0]['ms2']
zddj = data[0]['zddj']


window = Tk()
window.title(appname)
window.geometry("350x200")
chk_state0 = BooleanVar()
chk_state1 = BooleanVar()
chk_state2 = BooleanVar()
chk_state3 = BooleanVar()

# chk_state0.set(True)  # Set check state

def long_running_task0():
    global proc0
    if chk_state0.get() == True:
        proc0 = subprocess.Popen(['python', 'xxhelper/chaxun/jianqieban.py'], shell=True)
    else:
        subprocess.Popen("taskkill /F /T /PID " + str(proc0.pid) , shell=True)
    # 执行耗时的任务

    
def clicked0():
    print(ms0)
    thread0 = threading.Thread(target=long_running_task0)
    thread0.start()

def clicked1():
    print(ms1)
    
def clicked2():
    print(ms2)
    
def clicked3():
    print(zddj)

def cx0():
    proc1 = subprocess.Popen(['python', 'xxhelper/chaxun/cxxt.py'], shell=True)
    



chk0 = Checkbutton(window, text=ms0, var=chk_state0, command=clicked0)
chk1 = Checkbutton(window, text=ms1, var=chk_state1, command=clicked1)
chk2 = Checkbutton(window, text=ms2, var=chk_state2, command=clicked2)
chk3 = Checkbutton(window, text=zddj, var=chk_state3, command=clicked3)

btn0 = Button(window, text="一键启动查询系统", command=cx0)

chk0.grid(column=0, row=0)
chk1.grid(column=1, row=0)
chk2.grid(column=2, row=0)
chk3.grid(column=0, row=1)

btn0.grid(column=0, row=2)

window.mainloop()
