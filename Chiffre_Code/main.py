import sys
from PyQt5.QtWidgets import *
from homepage import homePage




class Interface:
    def __init__(self):
     Chiffra = QApplication(sys.argv)
     mainPage = homePage()
     sys.exit(Chiffra.exec_())



obj = Interface()