from PyQt4 import QtCore, QtGui
import Practice_start, sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        font = QtGui.QFont()
        font.setKerning(False)
        Form.setFont(font)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(85, 170, 127);"))
        self.practice_session = QtGui.QPushButton(Form)
        self.practice_session.setGeometry(QtCore.QRect(180, 270, 131, 41))
        self.practice_session.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.practice_session.setObjectName(_fromUtf8("practice_session"))
        self.create_challenge = QtGui.QPushButton(Form)
        self.create_challenge.setGeometry(QtCore.QRect(540, 270, 141, 41))
        self.create_challenge.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);\n"
""))
        self.create_challenge.setObjectName(_fromUtf8("create_challenge"))
        self.acceptchallenge = QtGui.QPushButton(Form)
        self.acceptchallenge.setGeometry(QtCore.QRect(360, 370, 151, 41))
        self.acceptchallenge.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);\n"
""))
        self.acceptchallenge.setObjectName(_fromUtf8("acceptchallenge"))
        self.back = QtGui.QPushButton(Form)
        self.back.setGeometry(QtCore.QRect(30, 530, 51, 27))
        self.back.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.back.setObjectName(_fromUtf8("back"))
        self.close = QtGui.QPushButton(Form)
        self.close.setGeometry(QtCore.QRect(720, 530, 51, 27))
        self.close.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);"))
        self.close.setObjectName(_fromUtf8("close"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(300, 170, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label.setFont(font)
        self.label.setStyleSheet(_fromUtf8("color: rgb(0, 0, 49);\n"
""))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.practice_session.setText(_translate("Form", "Practice", None))
        self.create_challenge.setText(_translate("Form", "Create Challenge", None))
        self.acceptchallenge.setText(_translate("Form", "Accept Challenge", None))
        self.back.setText(_translate("Form", "Back", None))
        self.close.setText(_translate("Form", "close", None))
        self.label.setText(_translate("Form", "     Choose Your Session", None))


    def closeApp(self):
        print "Cancel pressed"
        sys.exit()

    def ready(self):
        self.obj.hide()
        sec = Practice_start.Ui_Form()
        sec.setupUi(self.obj)
        self.obj.show()

        sec.close.clicked.connect(self.closeApp)



"""if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())"""

