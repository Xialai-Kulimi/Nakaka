from PyQt5 import QtCore, QtGui, QtWidgets
import time
from PyQt5.QtWidgets import QMessageBox
import hashlib
# exec("./../../venv/Lib/site-packages/nakakapag_tools/nakaka.py")
import socket


__version__ = 0.1
username = ''
password = ''
host = '220.135.245.148'


def sha256(input):
    sha_signature = \
        hashlib.sha256(input.encode()).hexdigest()
    return sha_signature


class CreateSocket:
    global host, username, password

    def __init__(self, port):
        self.s = socket.socket()
        self.s.connect((host, port))

        strs = username + '\n' + str(time.time()) + '\n' + sha256(
            username + password + str(time.time()))
        self.s.send(bytes(strs, 'utf8'))
        check = str(self.s.recv(1024), 'utf8')
        if check == 'got':
            return
        else:
            print('Error in logging', port)

    def send(self, gist: str, msg: str):
        strs = username + '\n' + gist + '\n' + msg + '\n' + str(time.time()) + '\n' + sha256(
            username + gist + msg + password + str(time.time()))
        self.s.send(bytes(strs, 'utf8'))
        check = str(self.s.recv(1024), 'utf8')
        if check == 'got':
            return
        else:
            print('Error in communicating with', self)

    def recv(self):
        data = str(self.s.recv(32767), 'utf8')
        # print('{data}', data)
        # print(len(data.split('\n')), len(data))
        # print('asd')
        if data.split('\n')[3] == sha256(data.split('\n')[0]+data.split('\n')[1] + password + data.split('\n')[2]):
            if (time.time()-float(data.split('\n')[2])) > 1:
                return 'Timed out'
            local_msg_log = open(data.split('\n')[0], 'a')
            local_msg_log.write(data.split('\n')[1] + ' ' + data.split('\n')[2])
            self.s.send(bytes('got', 'utf8'))
            return data.split('\n')[0], data.split('\n')[1], data.split('\n')[2]
        else:
            print(data.split('\n')[3], sha256(data.split('\n')[0]+data.split('\n')[1] + password +data.split('\n')[2]))
            return 'Server be hacked'

    def disconn(self):
        self.s.close()


# def click_login_2():
#     # MainWindow.label.setText("Wrong password\nor username!")
#     print(1)
#     time.sleep(0.5)
#     print(2)
#     # MainWindow.label.setText("Wrong password\nor username!!")
#     time.sleep(0.5)
#     print(3)
#     # MainWindow.label.setText("Wrong password\nor username!")


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 400, 400))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_3 = QtWidgets.QLabel(self.frame)

        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(0, 50, 300, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.label.setStyleSheet("color:rgb(255, 255, 255, 255)")
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label.setMouseTracking(True)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")

        self.label_2.setEnabled(True)
        self.label_2.setGeometry(QtCore.QRect(13, 152, 100, 11))
        font = QtGui.QFont()
        font.setFamily("Arial")
        # font.setPointSize(12)
        self.label_2.setStyleSheet("color:rgb(255, 255, 255, 255)")
        self.label_2.setFont(font)
        self.label_2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_2.setMouseTracking(True)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(False)
        self.label_2.setObjectName("label")

        self.label_3.setEnabled(True)
        self.label_3.setGeometry(QtCore.QRect(13, 182, 100, 11))
        font = QtGui.QFont()
        font.setFamily("Arial")
        # font.setPointSize(12)
        self.label_3.setStyleSheet("color:rgb(255, 255, 255, 255)")
        self.label_3.setFont(font)
        self.label_3.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label_3.setMouseTracking(True)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setTextFormat(QtCore.Qt.PlainText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_3.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(100, 150, 100, 20))
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit.setFont(font)

        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 180, 100, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(115, 230, 70, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.click_login)
        self.checkBox = QtWidgets.QCheckBox(self.frame)
        self.checkBox.setGeometry(QtCore.QRect(100, 210, 90, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox.setStyleSheet("color:rgb(255, 255, 255, 255)")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login"))
        self.label.setText(_translate("MainWindow", "# Login"))
        self.label_2.setText(_translate("MainWindow", "username:"))
        self.label_3.setText(_translate("MainWindow", "password:"))
        self.lineEdit.setText(_translate("MainWindow", ""))
        self.lineEdit_2.setText(_translate("MainWindow", ""))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.checkBox.setText(_translate("MainWindow", "Remeber me"))

    def click_login(self):
        # self.label.setText("Wrong password\nor username!")

        username = self.lineEdit.text()
        password = sha256(self.lineEdit_2.text())

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Username or password is incorrect.")
        # msg.setInformativeText(f"Your username: {self.lineEdit.text()}")
        msg.setWindowTitle("Login Failed")
        msg.setDetailedText(f"username: {username}\npassword_sha256: {password}")
        msg.exec_()
    # for i in range(10):
    #     self.label.setStyleSheet("color:rgb(255, 255, 255, 125);font-size:20px")
    #     time.sleep(1)
    #     self.label.setStyleSheet("color:rgb(255, 255, 255, 255);font-size:20px")
    #     time.sleep(1)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    p = MainWindow.palette()
    p.setColor(MainWindow.backgroundRole(), QtCore.Qt.black)
    MainWindow.setPalette(p)
    MainWindow.show()
    sys.exit(app.exec_())
