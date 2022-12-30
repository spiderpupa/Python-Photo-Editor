from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuHelp(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Photo Editor"))
        _translate = QtCore.QCoreApplication.translate

        self.menubar.setObjectName("menubar")

        self.menu_help = QtWidgets.QMenu(self.menubar)
        self.menu_help.setObjectName("도움말")
        self.menu_help.setTitle(_translate("MainWindow", "도움말"))

        self.help_help = QtWidgets.QAction(self.menu_help)
        self.help_help.setObjectName("도움말")
        self.help_help.setText(_translate("MainWindow", "불러오기"))
        self.help_help.setShortcut("Ctrl + H")

        self.help_info = QtWidgets.QAction(self.menu_help)
        self.help_info.setObjectName("정보")
        self.help_info.setText(_translate("MainWindow", "정보"))


        