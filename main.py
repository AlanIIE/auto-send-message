
import win32con
import win32gui, win32api
import win32clipboard as w
import time
from random import choice
from PyQt5 import QtCore,QtWidgets
from datetime import datetime

class sendMsg():
    def __init__(self,receiver,msg):
        self.receiver=receiver
        self.msg=msg

    def winUpLoadFile(self):
        # 将文件复制到剪切板
        app = QtWidgets.QApplication([])
        data = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(self.msg)
        data.setUrls([url])
        app.clipboard().setMimeData(data)
        clipboard = QtWidgets.QApplication.clipboard()
        
        self.sendmsg()
    
    def sendText(self):
        #设置剪贴版内容
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        w.CloseClipboard()

		self.sendmsg()
    #发送消息
    def sendmsg(self):
        qq=win32gui.FindWindow(None,self.receiver)
        win32gui.GetClassName(qq)  # 获取窗口classname
        title = win32gui.GetWindowText(qq)  # 获取窗口标题
        win32gui.GetDlgCtrlID(qq)
        win32gui.SetForegroundWindow(qq)  # 激活窗口

		#粘贴内容
        win32api.keybd_event(17, 0, 0, 0)  # ctrl键位码是17
        win32api.keybd_event(86, 0, 0, 0)  # v键位码是86
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

		#发送内容
        win32api.keybd_event(18, 0, 0, 0)  # Alt
        win32api.keybd_event(83, 0, 0, 0)  # s
        win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
        win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)

        print("sucessfuly send",self.msg)

# 从文件中读取文字
def getmessage(fileName):
    f=open(fileName,'r',encoding='utf-8')
    lines=f.readlines()
    f.close()
    return choice(lines)

def main():
    receiver='测试群聊'#这里填入接收者的备注名 
    date_sche = 17 # 17日
    time_sche = 15 # 15时。需要更精确的时间可以调整后面的if条件以及sleep时间
    while True:
        date_now = datetime.now()
        if date_now.day == date_sche and date_now.hour == time_sche:
        	filename = 'G:\\Users\\1\\Desktop\\英语作业.docx' # 设置文件
            qq=sendMsg(receiver, filename) # 初始化
            qq.winUpLoadFile() # 发送文件
            # msg = getmessage('message.txt') # 设置消息
            # qq=sendMsg(receiver, msg) # 初始化
            # qq.sendText() # 发送消息
        time.sleep(3600)

if __name__ == '__main__':
    main()
