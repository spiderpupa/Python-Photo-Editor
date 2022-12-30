from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MenuFile(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Photo Editor"))
        _translate = QtCore.QCoreApplication.translate

        self.menubar.setObjectName("menubar")

        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("파일")
        self.menu_file.setTitle(_translate("MainWindow", "파일"))
        
        self.file_load = QtWidgets.QAction(self.menu_file)
        self.file_load.setObjectName("불러오기")
        self.file_load.setText(_translate("MainWindow", "불러오기"))
        self.file_load.setShortcut("Ctrl + O")

        self.file_new = QtWidgets.QAction(self.menu_file)
        self.file_new.setObjectName("새로 만들기")
        self.file_new.setText(_translate("MainWindow", "새로 만들기"))
        self.file_new.setShortcut("Ctrl + N")

        self.file_save = QtWidgets.QAction(self.menu_file)
        self.file_save.setObjectName("저장")
        self.file_save.setText(_translate("MainWindow", "저장"))
        self.file_save.setShortcut("Ctrl + S")

        self.file_newSave = QtWidgets.QAction(self.menu_file)
        self.file_newSave.setObjectName("다른 이름으로 저장")
        self.file_newSave.setText(_translate("MainWindow", "다른 이름으로 저장"))
        self.file_newSave.setShortcut("Ctrl + N + S")

        self.file_import = QtWidgets.QAction(self.menu_file)
        self.file_import.setObjectName("불러오기")
        self.file_import.setText(_translate("MainWindow", "불러오기"))
        self.file_newSave.setShortcut("Ctrl + I")

        self.file_export = QtWidgets.QAction(self.menu_file)
        self.file_export.setObjectName("내보내기")
        self.file_export.setText(_translate("MainWindow", "내보내기"))
        self.file_export.setShortcut("Ctrl + E")

        self.config = QtWidgets.QAction(self.menu_file)
        self.config.setObjectName("설정")
        self.config.setText(_translate("MainWindow", "설정"))
        self.config.setShortcut("Ctrl + ,")