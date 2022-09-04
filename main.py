
import win32con
import win32gui, win32api
import win32clipboard as w
import time
from random import choice
from PyQt5 import QtCore,QtWidgets
from datetime import datetime
from PIL import Image
from io import BytesIO
import numpy as np

class sendMsg():
    def __init__(self,receiver,msg):
        self.receiver=receiver
        self.msg=msg

    def winUpLoadFile(self):
        # copy file to clipboard
        app = QtWidgets.QApplication([])
        data = QtCore.QMimeData()
        url = QtCore.QUrl.fromLocalFile(self.msg)
        data.setUrls([url])
        app.clipboard().setMimeData(data)
        clipboard = QtWidgets.QApplication.clipboard()
        
        self.sendmsg()
    
    def sendText(self):
        # set text in clipboard
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_UNICODETEXT, self.msg)
        w.CloseClipboard()
        self.sendmsg()


    def sendImage(self):
        # load image as Byte data
        output = BytesIO()
        self.msg.save(output, 'BMP')
        data = output.getvalue()[14:]
        output.close()
        # set text in clipboard
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(w.CF_DIB, data)
        w.CloseClipboard()

        self.sendmsg()
    # send message
    def sendmsg(self):
        qq=win32gui.FindWindow(None,self.receiver)
        win32gui.GetClassName(qq)  # get window classname
        title = win32gui.GetWindowText(qq)  # get window title
        win32gui.GetDlgCtrlID(qq)
        win32gui.SetForegroundWindow(qq)  # activate window

        # ctrl+v
        win32api.keybd_event(17, 0, 0, 0)  # ctrl = 17
        win32api.keybd_event(86, 0, 0, 0)  # v = 86
        win32api.keybd_event(86, 0, win32con.KEYEVENTF_KEYUP, 0)  # release key
        win32api.keybd_event(17, 0, win32con.KEYEVENTF_KEYUP, 0)

        # send message
        win32api.keybd_event(18, 0, 0, 0)  # Alt
        win32api.keybd_event(83, 0, 0, 0)  # s
        win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # release key
        win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)

        print("sucessfuly send",self.msg)

# load text frome file
def getmessage(fileName):
    f=open(fileName,'r',encoding='utf-8')
    lines=f.readlines()
    f.close()
    return choice(lines)

def main():
    receiver='测试群聊'# fill the receiver's nickname
    date_sche = 17 # 17th
    time_sche = 15 # 15:00. More acurrate time can be set in 'time.sleep()' later
    while True:
        date_now = datetime.now()
        if date_now.day == date_sche and date_now.hour == time_sche:
            filename = r'D:\Users\liang\Desktop\英语作业.docx' # set path for file
            qq=sendMsg(receiver, filename) # init
            qq.winUpLoadFile() # sent file
            
            # msg = getmessage('message.txt') # set text
            # qq=sendMsg(receiver, msg) # init
            # qq.sendText() # send text
	
            # load image file with PIL.
            # better for sending calculated images, no need to save it in HDD
            # if send file in disk, try qq.winUpLoadFile()
            img = np.random.randint(0, 255, [1800,3200,3], dtype=np.uint8)
            pil_img = Image.fromarray(img)
            qq=sendMsg(receiver, msg=pil_img)
            qq.sendImage() # send image
        time.sleep(3600)

if __name__ == '__main__':
    main()
