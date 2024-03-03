import os
import sys
import typing
from datetime import time
from queue import Queue
from threading import Thread
from multiprocessing.pool import ThreadPool
import time

import cv2
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtSvg, QtGui, QtCore
import projet

"""                                    CONTACT PAGE                                                 """


def create_buttonContact(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(141)
    button.setFixedHeight(18)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 20px;"
                         "font-size: 18px;"
                         "text-align: left;"
                         "font-family: Roboto;"
                         "font-weight: Medium;"
                         "background-color : #003BA3;"
                         "color: 'white';"
                         "}"
                         "QPushButton::pressed"
                         "{"
                         "background-color : #4A8CFF;"
                         "}"
                         )
    return button


def contact_text(self):
    text = QLabel("Contact us", self)
    text.setFixedHeight(185)
    text.setFixedWidth(474)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;" +
        "font-size: 50px;" +
        "font-weight: bold;" +
        "color: '#003BA3';" +
        "padding: 0px;"
    )
    return text


def text1Contact(texte, self):
    text = QLabel(texte, self)
    text.setFixedHeight(185)
    text.setFixedWidth(474)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;" +
        "font-size: 35px;" +
        "font-weight: regular;" +
        "color: '#000000';" +
        "padding: 0px;"
    )
    return text


def text2Contact(texte, self):
    text = QLabel(texte, self)
    text.setFixedHeight(185)
    text.setFixedWidth(474)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;" +
        "font-size: 40px;" +
        "font-weight: bold;" +
        "color: '#000000';" +
        "padding: 0px;"
    )
    return text


def text3Contact(texte, self):
    text = QLabel(texte, self)
    text.setFixedHeight(185)
    text.setFixedWidth(474)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;" +
        "font-size: 30px;" +
        "font-weight: regular;" +
        "color: '#003BA3';" +
        "padding: 0px;"
    )
    return text


class contactPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1440,1024)
        self.initUI()

    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self)  # white rectangle
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self)  # white rectangle
        sidebar.move(0, 0)
        line = QtSvg.QSvgWidget('./images/line.svg', self)  # white rectangle
        line.move(300, 200)
        image_label = QLabel(self)
        text = contact_text(self)  # Contact us text
        text.move(1090, 49)

        # icons
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg', self)
        logoIcon.move(17, 35)
        # icons
        start_label = QLabel(self)
        start = QPixmap('./images/start.png')
        start_label.move(16, 165)
        start_label.setPixmap(start)
        menu_icon = QtSvg.QSvgWidget('./images/menu.svg', self)
        menu_icon.move(15, 214)
        about_icon = QtSvg.QSvgWidget('./images/about.svg', self)
        about_icon.move(16, 261)
        help_icon = QtSvg.QSvgWidget('./images/help.svg', self)
        help_icon.move(16, 312)
        contact_icon = QtSvg.QSvgWidget('./images/contact.svg', self)
        contact_icon.move(16, 363)

        # buttons
        menu = create_buttonHelp("Start", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openUpload)
        menu = create_buttonHelp("Menu", self)
        menu.move(72, 214)
        menu.clicked.connect(self.openMenu)
        help = create_buttonHelp("Help", self)
        help.move(72, 261)
        help.clicked.connect(self.openHelp)
        contact = create_buttonHelp("Contact us", self)
        contact.move(72, 312)
        contact.clicked.connect(self.openContact)
        about = create_buttonHelp("About us", self)
        about.move(72, 363)
        about.clicked.connect(self.openAbout)

        # photos
        image_label1 = QLabel(self)
        email = QPixmap('./images/email.jpg')
        image_label1.move(300, 304)
        image_label1.setPixmap(email)
        image_label1 = QLabel(self)
        phone = QPixmap('./images/phone.jpg')
        image_label1.move(669, 304)
        image_label1.setPixmap(phone)
        image_label1 = QLabel(self)
        adress = QPixmap('./images/adress.jpg')
        image_label1.move(1024, 302)
        image_label1.setPixmap(adress)

        image_label = QLabel(self)
        text = text1Contact("chiffra@gmail.com", self)
        text.move(325, 550)
        text = text2Contact("E-mail", self)
        text.move(400, 480)
        text = text3Contact("Send us an email", self)
        text.move(351, 270)
        text = text1Contact("078374829", self)
        text.move(740, 550)
        text = text2Contact("Phone", self)
        text.move(780, 480)
        text = text3Contact("Give us a call", self)
        text.move(770, 270)
        text = text1Contact("Alger,algeria", self)
        text.move(1100, 550)
        text = text2Contact("Adress", self)
        text.move(1130, 480)
        text = text3Contact("Come see us", self)
        text.move(1100, 270)
        self.show()

"""                                           HELP PAGE                                             """


def create_buttonHelp(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(141)
    button.setFixedHeight(18)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 20px;"
                             "font-size: 18px;"
                             "text-align: left;"
                             "font-family: Roboto;"
                             "font-weight: Medium;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
    return button
def create_button2Help (name, self) :
        button2 = QPushButton(name, self)
        button2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button2.setFixedWidth(335)
        button2.setFixedHeight(74)
        button2.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 0px;"
                             "font-size: 30px;"
                             "font-family: Libre Franklin;"
                             "font-weight: bold;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
        return button2
def create_button3Help(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(230)
    button.setFixedHeight(23)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 500px;"
                             "font-size: 23px;"
                             "text-align: left;"
                             "font-family: Libre Baskerville;"
                             "font-weight: Medium;"
                             "background-color : #0000ffff;"
                             "color: '#4A8CFF';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #0000ffff;"
                             "}"
                             )
    return button
def upload_textHelp(self):
    text = QLabel("Help",self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 45px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 0px;"
    )
    return text
def HowToUse_text(self):
    text=QLabel("How to use Chiffra application ?",self)
    text.setFixedHeight(80)
    text.setFixedWidth(500)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 28px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 0px"
    )
    return text

def UploadPhoto_text(self):

    text=QLabel("To recognize a number, upload the number's photo on ",self)
    text.setFixedHeight(80)
    text.setFixedWidth(982)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Baskerville;" +
        "font-size: 23px;" +
        "font-weight: mixed;" +
        "color: '#000000';" +
        "padding: 0px"
    )
    return text
def AnyProblem_text(self):
    text = QLabel("Do you have any problems? ", self)
    text.setFixedHeight(80)
    text.setFixedWidth(500)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;" +
        "font-size: 28px;" +
        "font-weight: bold;" +
        "color: '#003BA3';" +
        "padding: 0px")
    return text
def MakeContact_text(self):
    text = QLabel("Please explain the issue in ", self)
    text.setFixedHeight(80)
    text.setFixedWidth(500)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Baskerville;" +
        "font-size: 23px;" +
        "font-weight: mixed;" +
        "color: '#000000';" +
        "padding: 0px"
    )
    return text



class helpPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1440,1024)
        self.initUI()

    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self) #white rectangle
        #white.move(0,0)
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self) #white rectangle
        sidebar.move(0,0)
        line = QtSvg.QSvgWidget('./images/line.svg', self) #white rectangle
        line.move(300,200)
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg', self)
        logoIcon.move(17, 35)
        rectangle = QtSvg.QSvgWidget('./images/Rectangle 28.svg', self)
        rectangle.move(300, 430)
        rectangle2 = QtSvg.QSvgWidget('./images/Rectangle 28.svg', self)
        rectangle2.move(300, 270)
        performance = QtSvg.QSvgWidget('./images/performance.svg', self)
        performance.move(300, 590)

        image_label = QLabel(self)
        image_label.move(450,233)
        text = upload_textHelp(self) #what is your number text
        text.move(1252,124)
        text2=HowToUse_text(self)#How to use Chiffra application
        text2.move(328,279)
        text3=UploadPhoto_text(self)#Upload a number's image to recognize the number
        text3.move(328,322)

        text4=AnyProblem_text(self)
        text4.move(328,429)
        text5=MakeContact_text(self)
        text5.move(328,472)

        #contact button in text
        link = create_button3Help("Contact us ", self)
        link.clicked.connect(self.openContact)
        link.move(600, 500)
        #What is your number in text
        whatisyournumber = create_button3Help("What is your number?", self)
        whatisyournumber.clicked.connect(self.openUpload)
        whatisyournumber.move(883, 350)


        #icons
        start_label = QLabel(self)
        start = QPixmap('./images/start.png')
        start_label.move(16, 165)
        start_label.setPixmap(start)
        menu_icon= QtSvg.QSvgWidget('./images/menu.svg',self)
        menu_icon.move(15,214)
        about_icon= QtSvg.QSvgWidget('./images/about.svg',self)
        about_icon.move(16,261)
        help_icon= QtSvg.QSvgWidget('./images/help.svg',self)
        help_icon.move(16,312)
        contact_icon= QtSvg.QSvgWidget('./images/contact.svg',self)
        contact_icon.move(16,363)


        #buttons
        menu = create_buttonHelp("Start", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openUpload)
        menu = create_buttonHelp("Menu",self)
        menu.move(72,214)
        menu.clicked.connect(self.openMenu)
        help = create_buttonHelp("Help",self)
        help.move(72,261)
        help.clicked.connect(self.openHelp)
        contact = create_buttonHelp("Contact us",self)
        contact.move(72,312)
        contact.clicked.connect(self.openContact)
        about = create_buttonHelp("About us",self)
        about.move(72,363)
        about.clicked.connect(self.openAbout)
        self.show()

"""                                        ABOUT PAGE                                     """

def create_buttonAbout(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(141)
    button.setFixedHeight(18)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 20px;"
                             "font-size: 18px;"
                             "text-align: left;"
                             "font-family: Roboto;"
                             "font-weight: Medium;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
    return button

def upload_textAbout(self):
    text = QLabel("About us",self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 50px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 0px;"
    )
    return text
class aboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1440, 1024)
        self.initUI()
    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self) #white rectangle
        #white.move(0,0)
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self) #white rectangle
        sidebar.move(0,0)
        line = QtSvg.QSvgWidget('./images/line.svg', self) #white rectangle
        line.move(300,200)
        text = upload_textAbout(self) #what is your number text
        text.move(1130,115)
        #icons
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg',self)
        logoIcon.move(17, 35)
        chiffraIcon = QtSvg.QSvgWidget('./images/chiffra.svg', self)
        chiffraIcon.move(300,250)
        whoWeAre = QtSvg.QSvgWidget('./images/who we are.svg', self)
        whoWeAre.move(489,441)
        defIcon = QtSvg.QSvgWidget('./images/we are team.svg', self)
        defIcon.move(339,516)
        listIcon = QtSvg.QSvgWidget('./images/list.svg', self)
        listIcon.move(348,651)
        self.setWindowIcon(QIcon("./images/logo.png"))
        self.setWindowIconText("logo")

        # icons
        start_label = QLabel(self)
        start = QPixmap('./images/start.png')
        start_label.move(16, 165)
        start_label.setPixmap(start)
        menu_icon = QtSvg.QSvgWidget('./images/menu.svg', self)
        menu_icon.move(15, 214)
        about_icon = QtSvg.QSvgWidget('./images/about.svg', self)
        about_icon.move(16, 261)
        help_icon = QtSvg.QSvgWidget('./images/help.svg', self)
        help_icon.move(16, 312)
        contact_icon = QtSvg.QSvgWidget('./images/contact.svg', self)
        contact_icon.move(16, 363)

        # buttons
        menu = create_buttonHelp("Start", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openUpload)
        menu = create_buttonHelp("Menu", self)
        menu.move(72, 214)
        menu.clicked.connect(self.openMenu)
        help = create_buttonHelp("Help", self)
        help.move(72, 261)
        help.clicked.connect(self.openHelp)
        contact = create_buttonHelp("Contact us", self)
        contact.move(72, 312)
        contact.clicked.connect(self.openContact)
        about = create_buttonHelp("About us", self)
        about.move(72, 363)
        about.clicked.connect(self.openAbout)

        self.show()

"""                                            DETECT PAGE                                         """

def create_buttonDetected(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(141)
    button.setFixedHeight(18)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 20px;"
                             "font-size: 18px;"
                             "text-align: left;"
                             "font-family: Roboto;"
                             "font-weight: Medium;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
    return button
def create_button2Detected (name, self) :
    button2 = QPushButton(name, self)
    button2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button2.setFixedWidth(200)
    button2.setFixedHeight(66)
    button2.setStyleSheet("QPushButton"
                          "{"
                          "border-radius: 0px;"
                          "font-size: 25px;"
                          "font-family: Libre Franklin;"
                          "font-weight: bold;"
                          "background-color : #003BA3;"
                          "color: 'white';"
                          "}"
                          "QPushButton::pressed"
                          "{"
                          "background-color : #4A8CFF;"
                          "}"
                          )
    return button2
def upload_textDetected(self):
    text = QLabel("What is your number?",self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 50px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 0px;"
    )
    return text
def chiffre_text(self,nombre):
    text = QLabel(nombre,self)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 36px;"+
        "font-weight: bold;"+
        "color: '#12D76E';"+
        "padding: 0px;"
    )
    return text
def time_text(self,nombre):
    text = QLabel(nombre+" seconds",self)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 36px;"+
        "font-weight: bold;"+
        "color: '#12D76E';"+
        "padding: 0px;"
    )
    return text
def taux_text(self,nombre):
    text = QLabel(nombre+"%",self)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 36px;"+
        "font-weight: bold;"+
        "color: '#12D76E';"+
        "padding: 0px;"
    )
    return text
class detectPage(QWidget):
    def __init__(self, nombre: str, time: str, taux: str):
        super().__init__()
        self.nombre = nombre
        self.time = time
        self.taux = taux
        self.resize(1440,1024)
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self)  # white rectangle
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self)  # white rectangle
        sidebar.move(0, 0)
        line = QtSvg.QSvgWidget('./images/line.svg', self)  # white rectangle
        line.move(300, 200)
        detectIcon = QtSvg.QSvgWidget('./images/Number detected box.svg', self)
        detectIcon.move(512, 250)
        taux_ressemblance = taux_text(self, str(self.taux))
        taux_ressemblance.move(955, 670)
        chiffre = chiffre_text(self, str(self.nombre))
        chiffre.move(1116,570)
        timetxt = time_text(self, str(self.time))
        timetxt.move(832,620)
        text = upload_textDetected(self)  # what is your number text
        text.move(784, 83)
        # icons
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg', self)
        logoIcon.move(17, 35)

        self.setWindowIcon(QIcon("./images/logo.png"))
        self.setWindowIconText("logo")

        # icons
        start_label = QLabel(self)
        start = QPixmap('./images/start.png')
        start_label.move(16, 165)
        start_label.setPixmap(start)
        menu_icon = QtSvg.QSvgWidget('./images/menu.svg', self)
        menu_icon.move(15, 214)
        about_icon = QtSvg.QSvgWidget('./images/about.svg', self)
        about_icon.move(16, 261)
        help_icon = QtSvg.QSvgWidget('./images/help.svg', self)
        help_icon.move(16, 312)
        contact_icon = QtSvg.QSvgWidget('./images/contact.svg', self)
        contact_icon.move(16, 363)

        # buttons
        menu = create_buttonHelp("Start", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openUpload)
        menu = create_buttonHelp("Menu", self)
        menu.move(72, 214)
        menu.clicked.connect(self.openMenu)
        help = create_buttonHelp("Help", self)
        help.move(72, 261)
        help.clicked.connect(self.openHelp)
        contact = create_buttonHelp("Contact us", self)
        contact.move(72, 312)
        contact.clicked.connect(self.openContact)
        about = create_buttonHelp("About us", self)
        about.move(72, 363)
        about.clicked.connect(self.openAbout)
        tryButton = create_button2NonDetect("Try Again", self)
        tryButton.move(1150, 884)
        tryButton.clicked.connect(self.openUpload)

    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self) #white rectangle
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self) #white rectangle
        sidebar.move(0,0)
        line = QtSvg.QSvgWidget('./images/line.svg', self) #white rectangle
        line.move(300,200)
        detectIcon= QtSvg.QSvgWidget('./images/Number detected box.svg',self)
        detectIcon.move(512,250)
        chiffre = chiffre_text(self,str(self.nombre))
        chiffre.move(950,606)
        text = upload_textDetected(self) #what is your number text
        text.move(784,83)
        #icons
        menu_icon= QtSvg.QSvgWidget('./images/menu.svg',self)
        menu_icon.move(15,165)
        about_icon= QtSvg.QSvgWidget('./images/about.svg',self)
        about_icon.move(16,214)
        help_icon= QtSvg.QSvgWidget('./images/help.svg',self)
        help_icon.move(16,261)
        contact_icon= QtSvg.QSvgWidget('./images/contact.svg',self)
        contact_icon.move(16,312)
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg',self)
        logoIcon.move(17, 35)

        self.setWindowIcon(QIcon("./images/logo.png"))
        self.setWindowIconText("logo")

        #buttons
        menu = create_buttonDetected("Menu",self)
        menu.move(72,165)
        menu.clicked.connect(self.openMenu)
        help = create_buttonDetected("Help",self)
        help.move(72,214)
        help.clicked.connect(self.openHelp)
        contact = create_buttonDetected("Contact us",self)
        contact.move(72,261)
        contact.clicked.connect(self.openContact)
        about = create_buttonDetected("About us",self)
        about.move(72,312)
        about.clicked.connect(self.openAbout)
        tryButton = create_button2Detected("Try Again", self)
        tryButton.move(1150,884)
        tryButton.clicked.connect(self.openUpload)
        self.show()


"""                                                NON DETECTED PAGE                                        """

def create_buttonNonDetect(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(141)
    button.setFixedHeight(18)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 20px;"
                             "font-size: 18px;"
                             "text-align: left;"
                             "font-family: Roboto;"
                             "font-weight: Medium;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
    return button
def create_button2NonDetect (name, self) :
        button2 = QPushButton(name, self)
        button2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button2.setFixedWidth(200)
        button2.setFixedHeight(66)
        button2.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 0px;"
                             "font-size: 25px;"
                             "font-family: Libre Franklin;"
                             "font-weight: bold;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
        return button2
def upload_textNonDetect(self):
    text = QLabel("What is your number?",self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 50px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 0px;"
    )
    return text
class notDetectedPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1440,1024)
        self.initUI()

    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self) #white rectangle
        #white.move(0,0)
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self) #white rectangle
        sidebar.move(0,0)
        line = QtSvg.QSvgWidget('./images/line.svg', self) #white rectangle
        line.move(300,200)
        image_label = QLabel(self)
        notdetected = QPixmap('./images/Not detected box.jpg')
        image_label.move(501, 250)
        image_label.setPixmap(notdetected)
        text = upload_textNonDetect(self) #what is your number text
        text.move(784,83)
        #icons
        menu_icon= QtSvg.QSvgWidget('./images/menu.svg',self)
        menu_icon.move(15,165)
        about_icon= QtSvg.QSvgWidget('./images/about.svg',self)
        about_icon.move(16,214)
        help_icon= QtSvg.QSvgWidget('./images/help.svg',self)
        help_icon.move(16,261)
        contact_icon= QtSvg.QSvgWidget('./images/contact.svg',self)
        contact_icon.move(16,312)
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg',self)
        logoIcon.move(17, 35)
       #set window icon
        self.setWindowIcon(QIcon("./images/logo.png"))
        self.setWindowIconText("logo")

        #buttons
        menu = create_buttonNonDetect("Menu",self)
        menu.move(72,165)
        menu.clicked.connect(self.openMenu)
        help = create_buttonNonDetect("Help",self)
        help.move(72,214)
        help.clicked.connect(self.openHelp)
        contact = create_buttonNonDetect("Contact us",self)
        contact.move(72,261)
        contact.clicked.connect(self.openContact)
        about = create_buttonNonDetect("About us",self)
        about.move(72,312)
        about.clicked.connect(self.openAbout)
        tryButton = create_button2NonDetect("Try Again", self)
        tryButton.move(1150,884)
        tryButton.clicked.connect(self.openUpload)
        self.show()


"""                                         LOADING PAGE                                            """

def create_buttonLoad(name, self):
    button = QPushButton(name, self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    self.resize(1440,1024)
    button.setStyleSheet("QPushButton"
                         "{"
                         "border-radius: 20px;"
                         "font-size: 18px;"
                         "text-align: left;"
                         "font-family: Roboto;"
                         "font-weight: Medium;"
                         "background-color : #003BA3;"
                         "color: 'white';"
                         "}"
                         "QPushButton::pressed"
                         "{"
                         "background-color : #4A8CFF;"
                         "}"
                         )
    return button


def create_button2Load(name, self):
    button2 = QPushButton(name, self)
    button2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button2.setFixedWidth(335)
    button2.setFixedHeight(74)
    button2.setStyleSheet("QPushButton"
                          "{"
                          "border-radius: 0px;"
                          "font-size: 30px;"
                          "font-family: Libre Franklin;"
                          "font-weight: bold;"
                          "background-color : #003BA3;"
                          "color: 'white';"
                          "}"
                          "QPushButton::pressed"
                          "{"
                          "background-color : #4A8CFF;"
                          "}"
                          )
    return button2


def upload_textLoad(self):
    text = QLabel("What is your number?", self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;" +
        "font-size: 50px;" +
        "font-weight: bold;" +
        "color: '#003BA3';" +
        "padding: 0px;"
    )
    return text


def loadingtextLoad(self):
    text = QLabel("Loading ...", self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Roboto;" +
        "font-size: 30px;" +
        "font-weight: bold;" +
        "color: '#003BA3';" +
        "padding: 0px;"
    )
    return text

class TaskThread(QtCore.QThread):
    taskFinished = QtCore.pyqtSignal()
    def run(self):
        dataset = projet.Dataset("Dataset/ALL")
        image = projet.ImageChiffre("user/chiffre.png")
        nombre = image.correlation(dataset.path)
        self.nombre = nombre
        self.taux = image.taux
        self.taskFinished.emit()


class loadPage(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.resize(1440,1024)

        self.setWindowTitle('Loading')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self)  # white rectangle
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self)  # white rectangle
        sidebar.move(0, 0)
        line = QtSvg.QSvgWidget('./images/line.svg', self)  # white rectangle
        line.move(300, 200)
        upload = QtSvg.QSvgWidget('./images/load.svg', self)
        upload.move(510, 340)
        text = upload_textLoad(self)  # what is your number text
        text.move(784, 83)
        # icons
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg', self)
        logoIcon.move(17, 35)
        start_label = QLabel(self)
        start = QPixmap('./images/start.png')
        start_label.move(16, 165)
        start_label.setPixmap(start)
        menu_icon = QtSvg.QSvgWidget('./images/menu.svg', self)
        menu_icon.move(15, 214)
        about_icon = QtSvg.QSvgWidget('./images/about.svg', self)
        about_icon.move(16, 261)
        help_icon = QtSvg.QSvgWidget('./images/help.svg', self)
        help_icon.move(16, 312)
        contact_icon = QtSvg.QSvgWidget('./images/contact.svg', self)
        contact_icon.move(16, 363)

        textload = loadingtextLoad(self)  # Loading text text
        textload.move(770, 600)

        # buttons
        menu = create_buttonLoad("Start", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openUpload)
        menu = create_buttonLoad("Menu", self)
        menu.move(72, 214)
        menu.clicked.connect(self.openMenu)
        help = create_buttonLoad("Help", self)
        help.move(72, 261)
        help.clicked.connect(self.openHelp)
        contact = create_buttonLoad("Contact us", self)
        contact.move(72, 312)
        contact.clicked.connect(self.openContact)
        about = create_buttonLoad("About us", self)
        about.move(72, 363)
        about.clicked.connect(self.openAbout)

        # progress bar
        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.move(695, 562)
        self.progress.setRange(0, 1)
        self.progress.setStyleSheet(
            "QProgressBar"
            "{"
            "border-radius: 20px;"
            "border : 2px solid #4A8CFF ;"
            "border-radius: 8px; "
            "text-align: center;"
            "color: white;"

            "font-weight: bold;"
            "background-color: #003BA3;"
            "color: 'white';"
            "}"
            "QProgressBar::chunk"
            "{"
            # "border-bottom-right-radius: 10px;"
            # " border-top-right-radius: 10px;" 
            # "border-bottom-left-radius: 10px;"
            # " border-top-left-radius: 10px;" 
            " background-color: #4A8CFF;"
            "}"
        )
        self.myLongTask = TaskThread()
        self.onStart()
        self.myLongTask.taskFinished.connect(self.onFinished)

    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openDetected(self,nombre,time,taux):
        self.ui = detectPage(nombre,time,taux)
        self.hide()
        self.ui.show()

    def openNotDetected(self):
        self.ui = notDetectedPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def onStart(self):
        self.start_time = time.time()
        self.progress.setRange(0, 0)
        self.myLongTask.start()

    def onFinished(self):
        # Stop the pulsation
        self.elapsed_time =  float(f'{time.time() - self.start_time:.2f}')
        pourcentage = ((self.myLongTask.taux * 100) / 6)
        self.taux = float(f'{pourcentage:.2f}')
        self.progress.setRange(0, 1)
        self.progress.setValue(1)
        if(self.myLongTask.nombre != -1):
            self.openDetected(self.myLongTask.nombre, self.elapsed_time, self.taux)
        else:
            self.openNotDetected()

    def initUI(self):
        self.setWindowTitle('Loading')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self)  # white rectangle
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self)  # white rectangle
        sidebar.move(0, 0)
        line = QtSvg.QSvgWidget('./images/line.svg', self)  # white rectangle
        line.move(300, 200)
        upload = QtSvg.QSvgWidget('./images/load.svg', self)
        upload.move(510, 340)
        text = upload_textLoad(self)  # what is your number text
        text.move(784, 83)
        # icons
        menu_icon = QtSvg.QSvgWidget('./images/menu.svg', self)
        menu_icon.move(15, 165)
        about_icon = QtSvg.QSvgWidget('./images/about.svg', self)
        about_icon.move(16, 214)
        help_icon = QtSvg.QSvgWidget('./images/help.svg', self)
        help_icon.move(16, 261)
        contact_icon = QtSvg.QSvgWidget('./images/contact.svg', self)
        contact_icon.move(16, 312)
        logo = QtSvg.QSvgWidget('./images/logo.svg', self)
        logo.move(17, 35)
        textload = loadingtextLoad(self)  # Loading text text
        textload.move(770, 600)

        # buttons
        menu = create_buttonLoad("Menu", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openMenu)
        help = create_buttonLoad("Help", self)
        help.move(72, 214)
        help.clicked.connect(self.openHelp)
        contact = create_buttonLoad("Contact us", self)
        contact.move(72, 261)
        contact.clicked.connect(self.openContact)
        about = create_buttonLoad("About us", self)
        about.move(72, 312)
        about.clicked.connect(self.openAbout)

        #loading bar

        self.progress = QProgressBar(self)
        self.progress.setGeometry(0, 0, 300, 25)
        self.progress.setMaximum(100)
        self.progress.move(695,562)
        self.progress.setRange(0, 1)
        self.progress.setStyleSheet(
            "QProgressBar"
            "{"
            "border-radius: 20px;"
            "border : 2px solid #4A8CFF ;"
            "text-align: center;"
            "color: white;"

            "font-weight: bold;"
            "background-color: #003BA3;"
            "color: 'white';"
            "}"
            "QProgressBar::chunk"
            "{"
            " background-color: #4A8CFF;"
            "}"
        )
        self.show()




"""                                          UPLOAD PAGE                                             """

def create_buttonUpload(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(141)
    button.setFixedHeight(18)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 20px;"
                             "font-size: 18px;"
                             "text-align: left;"
                             "font-family: Roboto;"
                             "font-weight: Medium;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
    return button
def create_button2Upload (name, self) :
        button2 = QPushButton(name, self)
        button2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        button2.setFixedWidth(335)
        button2.setFixedHeight(74)
        button2.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 0px;"
                             "font-size: 30px;"
                             "font-family: Libre Franklin;"
                             "font-weight: bold;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
        return button2
def upload_textUpload(self):
    text = QLabel("What is your number?",self)
    text.setFixedHeight(82)
    text.setFixedWidth(656)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 50px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 0px;"
    )
    return text
class uploadPage(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1440,1024)
        self.initUI()

    def openLoading(self):
        self.ui = loadPage()
        self.hide()
        self.ui.show()

    def openUpload(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openFileDialog(self):
        # save user image
        imgPath = QFileDialog.getOpenFileName(self,'Choose an image','c:\\','Image files (*.png *.jpg)')
        img = cv2.imread(imgPath[0])
        path = os.path.abspath(os.getcwd())
        cv2.imwrite(os.path.join(path, 'user/chiffre.png'), img)
        #Loading
        dataset = projet.Dataset('Dataset')
        image = projet.ImageChiffre('user/chiffre.png')
        self.ui = loadPage()
        self.hide()
        self.ui.show()

    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openDetected(self, nombre):
        self.ui = detectPage(nombre)
        self.hide()
        self.ui.show()

    def openMenu(self):
        self.ui = homePage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        white = QtSvg.QSvgWidget('./images/white.svg', self) #white rectangle
        #white.move(0,0)
        sidebar = QtSvg.QSvgWidget('./images/sidebar.svg', self) #white rectangle
        sidebar.move(0,0)
        line = QtSvg.QSvgWidget('./images/line.svg', self) #white rectangle
        line.move(300,200)
        image_label = QLabel(self)
        upload = QPixmap('./images/upload image box.jpg')
        image_label.move(450,233)
        image_label.setPixmap(upload)
        text = upload_textUpload(self) #what is your number text
        text.move(784,83)

        #icons
        start_label = QLabel(self)
        start = QPixmap('./images/start.png')
        start_label.move(16,165)
        start_label.setPixmap(start)

        menu_icon= QtSvg.QSvgWidget('./images/menu.svg',self)
        menu_icon.move(15,214)
        about_icon= QtSvg.QSvgWidget('./images/about.svg',self)
        about_icon.move(16,261)
        help_icon= QtSvg.QSvgWidget('./images/help.svg',self)
        help_icon.move(16,312)
        contact_icon= QtSvg.QSvgWidget('./images/contact.svg',self)
        contact_icon.move(16,363)
        logoIcon = QtSvg.QSvgWidget('./images/logo.svg', self)
        logoIcon.move(17, 35)
        #buttons
        menu = create_buttonUpload("Start", self)
        menu.move(72, 165)
        menu.clicked.connect(self.openUpload)
        menu = create_buttonUpload("Menu",self)
        menu.move(72,214)
        menu.clicked.connect(self.openMenu)
        help = create_buttonUpload("Help",self)
        help.move(72,261)
        help.clicked.connect(self.openHelp)
        contact = create_buttonUpload("Contact us",self)
        contact.move(72,312)
        contact.clicked.connect(self.openContact)
        about = create_buttonUpload("About us",self)
        about.move(72,363)
        about.clicked.connect(self.openAbout)
        upload_button = create_button2Upload("Upload image", self)
        upload_button.move(650,726)
        upload_button.clicked.connect(self.openFileDialog)
        # aboutclicked.connect(loading_page)
        self.show()

"""                                     HOME PAGE                                                  """

def create_buttonHome(name,self):
    button = QPushButton(name,self)
    button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
    button.setFixedWidth(212)
    button.setFixedHeight(66)
    button.setStyleSheet("QPushButton"
                             "{"
                             "border-radius: 20px;"
                             "font-size: 25px;"
                             "font-family: Libre Franklin;"
                             "font-weight: bold;"
                             "background-color : #003BA3;"
                             "color: 'white';"
                             "}"
                             "QPushButton::pressed"
                             "{"
                             "background-color : #4A8CFF;"
                             "}"
                             )
    return button
def home_text(self):
    text = QLabel("What is\nthis number?",self)
    #text.move(98,153) #position
    text.setAlignment(Qt.AlignLeft)
    text.setWordWrap(True)
    text.setStyleSheet(
        "font-family: Libre Franklin;"+
        "font-size: 100px;"+
        "font-weight: bold;"+
        "color: '#003BA3';"+
        "padding: 75px;"
    )
    return text


class homePage(QWidget):

    def __init__(self):
        super().__init__()
        self.resize(1440,1024)
        self.initUI()
    def openContact(self):
        self.ui = contactPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openHelp(self):
        self.ui = helpPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def openAbout(self):
        self.ui = aboutPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()

    def openStart(self):
        self.ui = uploadPage()
        self.ui.initUI()
        self.hide()
        self.ui.show()
    def initUI(self):
        self.setWindowTitle('Chiffra')
        self.setWindowIcon(QIcon('./images/logo.png'))
        svgwhite = QtSvg.QSvgWidget('./images/white.svg', self) #white rectangle
        svggrey = QtSvg.QSvgWidget('./images/gris.svg', self) #rectangle gris
        svggrey.move(0,0)
        svgillustration = QtSvg.QSvgWidget('./images/home.svg',self) #illustration
        svgillustration.move(800,400)
        text = home_text(self) #what is your number text
        #buttons
        start = create_buttonHome("Start",self)
        start.clicked.connect(self.openStart)
        help = create_buttonHome("Help",self)
        help.clicked.connect(self.openHelp)
        contact = create_buttonHome("Contact us",self)
        contact.clicked.connect(self.openContact)
        about = create_buttonHome("About us",self)
        about.clicked.connect(self.openAbout)
        text.move(0,0)
        start.move(98, 450)
        help.move(98, 557)
        contact.move(98, 664)
        about.move(98, 771)
        self.show()
