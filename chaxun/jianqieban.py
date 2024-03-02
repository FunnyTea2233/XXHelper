import time
import tkinter as tk
import yaml
from tkinter import *
import pyperclip
import threading
import re





# pyperclip.copy("hello") #写入剪切板

with open('xxhelper/config.yaml',encoding='utf-8') as file1:
    data = yaml.load(file1,Loader=yaml.FullLoader)#读取yaml文件

root = tk.Tk()
root.title(data[0]['ms0'])

root.wm_attributes("-alpha", 0.4)        # 透明度(0.0~1.0)
root.wm_attributes("-toolwindow", True)  # 置为工具窗口(没有最大最小按钮)
root.wm_attributes("-topmost", True)     # 永远处于顶层
root.geometry("200x500")

# 去除窗口边框
# root.overrideredirect(True)

chk_state0 = BooleanVar()



# 13357913112      19525106420     17312721651  

def long_running_task0():
    print(1)
    jq = 'error'
    try:
        jq = str(re.findall('(1[0-9]{10})', pyperclip.paste())[0])
    except Exception as e:
        jq = 'error'
    current_clipboard = jq
    try:
        while chk_state0.get() == True:
            # sjh = re.findall('(13\d{9}|14[5|7]\d{8}|15\d{9}|166{\d{8}|17[3|6|7]{\d{8}|18\d{9})', pyperclip.paste())
            sjh = re.findall('(1[0-9]{10})', pyperclip.paste())
            try:
                lbl.configure(text=sjh[0])
                jq = sjh[0]
            except Exception as e:
                lbl.configure(text='error')
            time.sleep(1)
            try:
                if jq != current_clipboard:
                    current_clipboard = jq
                    print('剪贴板内容已更改:', current_clipboard)
                    thread2 = threading.Thread(target=long_running_task2)
                    thread2.start()
                    
                    
            except Exception as e:
                lbl.configure(text='error')
    except Exception as e:
        print('stop')     
    # 执行耗时的任务
    
def long_running_task1():
    from cxxt import jqbcx
    jqbcx()
    
def long_running_task2():
    from cxxt import startcx
    startcx()
    print(1111)

def jqb():
    thread0 = threading.Thread(target=long_running_task0)
    thread0.start()
    thread1 = threading.Thread(target=long_running_task1)
    thread1.start()
    

btn = Checkbutton(root, text="获取剪切板中号码",var=chk_state0, command=jqb)
btn.grid(column=0, row=1)

lbl = Label(root, text="Hello")
lbl.grid(column=0, row=0)

root.mainloop()

