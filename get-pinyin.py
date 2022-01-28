# -*- coding: utf-8 -*-
#代码仅限学习和交流!
import requests,time,random,winreg
from lxml import etree
from PyQt5 import QtCore, QtGui, QtWidgets
def show_about_ui():
    aboutWindow.show()
def close_about_ui():
    aboutWindow.close()
def retime():#动态刷新所需时间
    s1,l1='',[]
    try:
        p=ui.textEdit.toPlainText()
        if ',' in p or '，' in p:
            ui.tips.setText("**请不要用逗号分隔!**")
            ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
        elif '、、' in p:
            ui.tips.setText("**请不要重复输入顿号!**")
            ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
        elif ' ' in p or ' ' in p:
            ui.tips.setText("**请不要输入空格!**")
            ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
        elif '\n' in p:
            ui.tips.setText("**请不要输入回车!**")
            ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
        else:
            if p[-1]!='、':
                p=p+'、'
            for i in p:
                if i=='、':
                    l1.append(s1)
                    s1=''
                else:
                    s1=s1+i
            a=random.randint(80,85)
            ui.tips.setText("**获取大约需要{}秒**".format(len(l1)*a/100))
            ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
    except:
        ui.tips.setText("**你好像还没有输入文字!**")
        ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
def getpinyin():#'Get'按钮后
    global out,out1
    a,s1,l1,list_other,out,out1,dic_other,headers=0,'',[],[],'','',{},{'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'}
    try:
        p=ui.textEdit.toPlainText()
    except:
        ui.tips.setText("**请输入文字!!!**")
        ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
    try:#爬取拼音
        if p[-1]!='、':
            p=p+'、'
        for i in p:
            if i=='、':
                l1.append(s1)
                s1=''
            else:
                s1=s1+i
        for s in l1:
            time.sleep(0.5)
            urls='https://hanyu.baidu.com/s'
            param={'wd':s,'ptype':'zici'}
            tree=etree.HTML(requests.get(url=urls,headers=headers,params=param).text)
            try:
                pinyin_list=tree.xpath('//div[@id="pinyin"]//span/b/text()')
                if len(pinyin_list) > 1:
                    dic_other={'zi':s,'yin':pinyin_list}
                    list_other.append(dic_other)
                pinyin=pinyin_list[0]
                if pinyin[0] == '[':
                    pinyin=pinyin[2:-2]
                if l1[-1] != s:
                    out=out+pinyin+'、'
                elif l1[-1] == s:
                    out=out+pinyin
            except:#错误处理
                if l1[-1]!=s:
                    out=out+'ERROR、'
                elif l1[-1] == s:
                    out=out+'ERROR'
        #lastWindow.show()
        if len(list_other)>0:
            s1=''
            for d in list_other:
                        out1=out1+'\n'+d['zi']+':'
                        for s in d['yin']:
                            if s[0] == '[':
                                s1=s[2:-2]
                            elif s[0]!='[':
                                s1=s
                            if s==d['yin'][-1]:
                                out1=out1+s1
                            elif s!=d['yin'][-1]:
                                out1=out1+s1+','
            other_ui.textBrowser.setText(out)
            other_ui.textBrowser_2.setText(out1)
            otherWindow.show()
            other_ui.tip2.setText('')
            last_ui.tip2.setText('')
            if 'ERROR'in out:
                other_ui.tip2.setText('**‘ERROR’可能为百度汉语未收录该词**')
                other_ui.tip2.setTextFormat(QtCore.Qt.MarkdownText)
        else:
            last_ui.textBrowser.setText(out)
            lastWindow.show()
            if 'ERROR'in out:
                last_ui.tip2.setText('**‘ERROR’可能为百度汉语未收录该词**')
                last_ui.tip2.setTextFormat(QtCore.Qt.MarkdownText)
    except:
        ui.tips.setText('**错误,请检查输入和网络!**')
        ui.tips.setTextFormat(QtCore.Qt.MarkdownText)
def save():#保存
    file=winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER,r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders'),"Desktop")[0]
    file+='\\拼音.txt'
    with open(file,'w',encoding='utf-8') as fp:
        fp.write(out+'\n'+out1)
        last_ui.tip2.setText('**保存成功!**')
        last_ui.tip2.setTextFormat(QtCore.Qt.MarkdownText)
        other_ui.tip2.setText('**保存成功!**')
        other_ui.tip2.setTextFormat(QtCore.Qt.MarkdownText)
def close_all_ui():
    otherWindow.close()
    other_ui.textBrowser.clear()
    other_ui.tip2.clear()
    lastWindow.close()
    last_ui.textBrowser.clear()
    last_ui.tip2.clear()
def copy_to():#复制
    clipboard = QtWidgets.QApplication.clipboard()
    clipboard.setText(out+'\n'+out1)
    last_ui.tip2.setText('**复制成功!**')
    last_ui.tip2.setTextFormat(QtCore.Qt.MarkdownText)
    other_ui.tip2.setText('**复制成功!**')
    other_ui.tip2.setTextFormat(QtCore.Qt.MarkdownText)
class Ui_mainWindow(object):#主窗口UI
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setWindowOpacity(0.9)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.tips = QtWidgets.QLabel(self.centralwidget)
        self.tips.setText("")
        self.tips.setObjectName("tips")
        self.gridLayout.addWidget(self.tips, 0, 1, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label_22.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 0, 2, 1, 1)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 3)
        self.textEdit.textChanged.connect(retime)
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.about_button.setObjectName("about_button")
        self.gridLayout.addWidget(self.about_button, 2, 0, 1, 1)
        self.about_button.clicked.connect(show_about_ui)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 2)
        self.pushButton.clicked.connect(getpinyin)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 360, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.textEdit, self.pushButton)
        mainWindow.setTabOrder(self.pushButton, self.about_button)
    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "获取拼音"))
        self.label.setText(_translate("mainWindow", "在这里输入汉字:"))
        self.label_22.setText(_translate("mainWindow", "如果输入多组文字，请用‘、’隔开!"))
        self.about_button.setText(_translate("mainWindow", "关于"))
        self.pushButton.setText(_translate("mainWindow", "GET!"))
class Ui_other(object):#含多音字的UI
    def setupUi(self, other):
        other.setObjectName("other")
        other.resize(274, 259)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        other.setWindowIcon(icon)
        other.setWindowOpacity(0.9)
        other.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gridLayout = QtWidgets.QGridLayout(other)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowser = QtWidgets.QTextBrowser(other)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 3)
        self.label = QtWidgets.QLabel(other)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.saveB = QtWidgets.QPushButton(other)
        self.saveB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveB.setObjectName("saveB")
        self.gridLayout.addWidget(self.saveB, 4, 0, 1, 1)
        self.copyB = QtWidgets.QPushButton(other)
        self.copyB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copyB.setObjectName("copyB")
        self.gridLayout.addWidget(self.copyB, 4, 1, 1, 1)
        self.closeB = QtWidgets.QPushButton(other)
        self.closeB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeB.setObjectName("closeB")
        self.gridLayout.addWidget(self.closeB, 4, 2, 1, 1)
        self.tip2 = QtWidgets.QLabel(other)
        self.tip2.setText("")
        self.tip2.setObjectName("tip2")
        self.gridLayout.addWidget(self.tip2, 0, 1, 1, 1)
        self.textBrowser_2 = QtWidgets.QTextBrowser(other)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.gridLayout.addWidget(self.textBrowser_2, 3, 0, 1, 3)
        self.label_2 = QtWidgets.QLabel(other)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.retranslateUi(other)
        self.copyB.clicked.connect(copy_to)
        self.closeB.clicked.connect(close_all_ui)
        self.saveB.clicked.connect(save)
        QtCore.QMetaObject.connectSlotsByName(other)

    def retranslateUi(self, other):
        _translate = QtCore.QCoreApplication.translate
        other.setWindowTitle(_translate("other", "结果"))
        self.label.setText(_translate("other", "获取到了："))
        self.saveB.setText(_translate("other", "保存"))
        self.copyB.setText(_translate("other", "复制"))
        self.closeB.setText(_translate("other", "关闭"))
        self.label_2.setText(_translate("other", "发现一些多音字(词)！"))
class Ui_last(object):#结果UI
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(298, 279)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.9)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.copyB = QtWidgets.QPushButton(Form)
        self.copyB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.copyB.setObjectName("copyB")
        self.gridLayout.addWidget(self.copyB, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.closeB = QtWidgets.QPushButton(Form)
        self.closeB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.closeB.setObjectName("closeB")
        self.gridLayout.addWidget(self.closeB, 2, 2, 1, 1)
        self.saveB = QtWidgets.QPushButton(Form)
        self.saveB.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveB.setObjectName("saveB")
        self.gridLayout.addWidget(self.saveB, 2, 0, 1, 1)
        self.tip2 = QtWidgets.QLabel(Form)
        self.tip2.setText("")
        self.tip2.setObjectName("tip2")
        self.gridLayout.addWidget(self.tip2, 0, 1, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ForbiddenCursor))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 1, 0, 1, 3)
        self.retranslateUi(Form)
        self.copyB.clicked.connect(copy_to)
        self.closeB.clicked.connect(close_all_ui)
        self.saveB.clicked.connect(save)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "结果"))
        self.copyB.setText(_translate("Form", "复制"))
        self.label.setText(_translate("Form", "获取到了："))
        self.closeB.setText(_translate("Form", "关闭"))
        self.saveB.setText(_translate("Form", "保存"))
class Ui_about(object):#关于UI
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(311, 193)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(0.9)
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 4, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 4, 1, 1)
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("楷体")
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 4)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setIndent(8)
        self.label_3.setObjectName("label_3")
        self.label_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_3.setOpenExternalLinks(True)
        self.gridLayout.addWidget(self.label_3, 1, 3, 1, 1)
        self.label.setBuddy(self.label)
        self.label_3.setBuddy(self.label_3)
        self.retranslateUi(Form)
        self.pushButton.clicked.connect(close_about_ui)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "关于"))
        self.label_2.setText(_translate("Form", "By link"))
        self.label_4.setText(_translate("Form", " "))
        self.pushButton.setText(_translate("Form", "关闭"))
        self.label.setText(_translate("Form", "这是一个简单的获取拼音的程序,\n通过爬取百度汉语的网页获得\n拼音,很适合小学一二年级的语文老师\n出试卷、出题目的时候批量获取拼音,\n也适合个人不认识的字的时候快速获取拼音的场景。"))
        self.label_3.setText(_translate("Form", "本程序已在[Github](https://github.com/link-fgfgui/get-pinyin)上开源"))
wangluo=None
#检查网络连接,否则不予启动
try:
    if '2' not in str(requests.get(url='https://www.baidu.com',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'},timeout=2.5).status_code) and '2' not in str(requests.get(url='https://www.qq.com/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62'},timeout=2.5).status_code):
        tiShiapp=QtWidgets.QApplication([])
        msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '访问网络失败,请连接到网络后再试。')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_box.setWindowIcon(icon)
        msg_box.setWindowOpacity(0.9)
        msg_box.show()
        tiShiapp.exec_()
    else:
        wangluo='200'
        app = QtWidgets.QApplication([])
        #初始化UI
        mainWindow=QtWidgets.QMainWindow()
        ui=Ui_mainWindow()
        ui.setupUi(mainWindow)
        lastWindow=QtWidgets.QWidget()
        last_ui=Ui_last()
        last_ui.setupUi(lastWindow)
        otherWindow=QtWidgets.QWidget()
        other_ui=Ui_other()
        other_ui.setupUi(otherWindow)
        aboutWindow = QtWidgets.QWidget()
        about_ui = Ui_about()
        about_ui.setupUi(aboutWindow)
        mainWindow.show()
        app.exec_()
except:
        tiShiapp=QtWidgets.QApplication([])
        if wangluo=='200':
            msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '程序初始化失败，请尝试重新启动。')
        else:
            msg_box =QtWidgets.QMessageBox(QtWidgets.QMessageBox.Critical, '错误', '无法连接到网络,请连接到网络后再试。')
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./icon/icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        msg_box.setWindowIcon(icon)
        msg_box.setWindowOpacity(0.9)
        msg_box.show()
        tiShiapp.exec_()