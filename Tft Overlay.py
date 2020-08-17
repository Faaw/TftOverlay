from PyQt5 import QtCore, QtGui, QtWidgets
import win32api, win32con, win32gui, win32ui
import cv2
import numpy as np
import pyautogui
i=0
j=0

class Worker(QtCore.QRunnable):

    def run(self):
        um = 0
        dois = 0
        tres = 0
        quatro = 0
        cinco = 0
        tup = list()
        choice = 1
        champs = ['Leona', 'Poppy', 'Ziggs', 'Zoe', 'Graves', 'Twisted Fate', 'Malphite', 'Caitlyn', 'Nocturne', 'Fiora', 'Illaoi', 'Xayah', 'Jarvan IV', 'Ahri', 'Darius', 'Mordekaiser', 'Rakan', 'Shen', 'Xin Zhao', 'Kog`Maw', 'Lucian', 'Yasuo', 'Blitzcrank', 'Nautilus', 'Zed', 'Annie', 'Vi', 'Karma', 'Bardo', 'Neeko', 'Rumble', 'Ezreal', 'Syndra', 'Cassiopeia', 'Master Yi', 'Shaco', 'Ashe', 'Vayne', 'Jayce', 'Viktor', 'Jhin', 'Riven', 'Gnar', 'Soraka', 'Wukong', 'Irelia', 'Fizz', 'Teemo', 'Jinx', 'Janna', 'Ekko', 'Gangplank', 'Xerath', 'Urgot', 'Lulu', 'Thresh', 'Aurelion Sol']
        champ = []
        print("Select the champions, type 69 to continue after finishing the list. Type 1 per line. Champions code below: \n0-Leona 1-Poppy 2-Ziggs 3-Zoe 4-Graves 5-Twisted Fate 6-Malphite 7-Caitlyn 8-Nocturne 9-Fiora\n10-Illaoi 11-Xayah 12-Jarvan IV 13-Ahri 14-Darius 15-Mordekaiser 16-Rakan 17-Shen 18-Xin Zhao\n19-Kog`Maw 20-lucian 21-Yasuo 22-Blitzcrank 23-Nautilus 24-Zed 25-Annie 26-Vi 27-Karma\n28-Bardo 29-Neeko 30-Rumble 31-Ezreal 32-Syndra 33-Cassiopeia 34-Master Yi 35-Shaco 36-Ashe\n37-Vayne 38-Jayce 39-Viktor 40-Jhin 41-Riven 42-Gnar 43-Soraka 44-Wukong 45-Irelia\n46-Fizz 47-Teemo 48-Jinx 49-Janna 50-Ekko 51-Gangplank 52-Xerath 53-Urgot 54-Lulu\n55-Thresh 56-Aurelion Sol")
        while choice == 1:
            k=input()
            if k !='69':
                tup.append(k)
                k = int(k)
                champ.append(champs[k])
                print(champ)
            else:
                choice = 0
                break
        tup = [int(i) for i in tup]
        #tup = (3, 12, 13, 29, 32, 43, 49, 52, 54) # star guardian sorc
        #tup = (25, 30 ,33, 39, 43, 46, 50, 51, 55) #mecha meta
        #tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,13 ,14 ,15 ,16 ,17 ,18 ,19 ,20, 21 ,22 ,23 ,24 ,25 ,26 ,27 ,28 ,29 ,30 ,31 ,32 ,33, 34, 35, 36, 37, 38, 39, 40)
        print("Thread start") 
        while 1==1:
            #print("começou while")
            i=0
            if um != 1:
                front1.setWindowOpacity(0)
                #print("limpou tudo que for 1 e ", um)
            if dois !=2:
                front2.setWindowOpacity(0)
                #print("limpou tudo que for 2 e ", dois)
            if tres !=3:
                front3.setWindowOpacity(0)
                #print("limpou tudo que for 3 e ", tres)
            if quatro !=4:
                front4.setWindowOpacity(0)
                #print("limpou tudo que for 4 e ", quatro)
            if cinco !=5:
                front5.setWindowOpacity(0)
                #print("limpou tudo que for 5 e ", cinco)
            #print("limpou tudo que for 0")
            um = 0
            dois = 0
            tres = 0
            quatro = 0
            cinco = 0
            #print("setou tudo em 0 e ", tres)
            img_rgb = pyautogui.screenshot(region=(470, 925, 1010, 150))
            img_rgb = cv2.cvtColor(np.array(img_rgb), cv2.COLOR_RGB2BGR)
            for x in tup:
                #print(x)
                #img_rgb = cv2.imread(r"C:\Tft\TFTOverlay by reds\Buy\{}.png".format(i))
                template = cv2.imread(r"C:\Tft\TFTOverlay by reds\Buy\{}.png".format(x))
                w, h = template.shape[:-1]
                res = cv2.matchTemplate(img_rgb, template, cv2.TM_CCOEFF_NORMED)
                threshold = .8
                loc = np.where(res >= threshold)
                aaaaa = loc[0]
                if len(aaaaa) > 0:
                    for pt in zip(*loc[::-1]):  # Switch collumns and rows
                        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
                        if (0 < pt[0] < 200) and (um != 1):
                            #print("entre 0 e 200")
                            front1.setWindowOpacity(1)
                            um = 1

                        if (200 < pt[0] < 400)  and (dois != 2):
                            #print("entre 200 e 400")
                            front2.setWindowOpacity(1)
                            dois = 2

                        if (400 < pt[0] < 600)  and (tres != 3):
                            #print("entre 400 e 600")
                            front3.setWindowOpacity(1)
                            tres = 3

                        if (600 < pt[0] < 800)  and (quatro != 4):
                            #print("entre 600 e 800")
                            front4.setWindowOpacity(1)
                            quatro = 4

                        if (800 < pt[0] < 1000)  and (cinco != 5):
                            #print("entre 800 e 1000")
                            front5.setWindowOpacity(1)
                            cinco = 5

                i+=1
        i=0
        print("Thread complete")

#class Overlay(QtWidgets.QMainWindow):
    #def __init__(self, left, top, height, width, whndl=None, *args, **kwargs):
        #super(Overlay,self).__init__(*args, **kwargs) 
        #self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint)
        #self.setGeometry(left, top, height, width)

        #self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        
        #layout = QtWidgets.QVBoxLayout()
        
        #b1 = QtWidgets.QPushButton("Build")
        #b1.pressed.connect(self.b1F)
        #b1.setMaximumWidth(50)
        #b1.setMaximumHeight(50)
        #layout.addWidget(b1)
        #layout.setContentsMargins(125, 26, 125, 26)
        #w = QtWidgets.QWidget()
        #w.setLayout(layout)
        #self.setCentralWidget(w)
        
        #self.setStyleSheet("""
            #QWidget{
                #background: transparent;
                #background-image: url("C:/Users/rafae/Desktop/TFTOverlay by reds/menu.png");
                #}
            #""")      
        #b1.setStyleSheet("""
            #QWidget{
                #background: transparent;
                #background-image: url("C:/Users/rafae/Desktop/TFTOverlay by reds/bt.png")
                #}
            #""")
        #self.show()
        
    #def b1F(self):
        #print('yey')

class Front(QtWidgets.QPushButton):
    def __init__(self, left, top, height, width, j, whndl=None):
        self.threadpool = QtCore.QThreadPool()
        #print("Multithreading with maximum %d threads" % self.threadpool.maxThreadCount())        
        super(Front,self).__init__()
        #self.setWindowOpacity(0.1)
        self.setStyleSheet("""
            QWidget{
                background: transparent;
                background-image: url("C:/Tft/TFTOverlay by reds/border.png");     
                }
            """)
        self.setAutoFillBackground(True)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.FramelessWindowHint | QtCore.Qt.WindowTransparentForInput | QtCore.Qt.Tool)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground, True)
        self.setGeometry(left, top, height, width)
        self.show()
        #self.setWindowOpacity(0)
        if j == 4:
            self.compare()
    def compare(self):
        worker = Worker()
        self.threadpool.start(worker)


a = QtWidgets.QApplication([])

screen = pyautogui.size()
if screen == (1920, 1080):
    front1 = Front(475, 921, 205, 157, 0)
    front2 = Front(676, 921, 205, 157, 0)
    front3 = Front(877, 921, 205, 157, 0)
    front4 = Front(1078, 921, 205, 157, 0)
    front5 = Front(1279, 921, 205, 157, 4)
    
a.exec_()
