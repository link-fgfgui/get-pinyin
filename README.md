# get-pinyin
 
随手写的一个爬取百度汉语拼音的程序

___

### 更新记录

优化代码--2022.1.20<br>
修复单个字无法被xpath正常解析的问题--2022.1.21 20:22<br>
修复保存和输出时结果最前或最后带有顿号的问题--2022.1.21 20:39<br>
修复输入时最后带有顿号导致错误的问题--2022.1.21 20:47<br>

___

使用的库：

time

requests

lxml


## 使用教程

### Windows

从[这里](https://www.python.org/downloads/)选一个喜欢的版本下载

用<br>`pip install requests`<br>`pip install lxml`<br>安装库

运行getpinyin.py

### Android

建议用**Pydroid3**运行<br>
给个下载地址：<br>
[Apkpure](https://apkpure.com/cn/pydroid-3-ide-for-python-3/ru.iiec.pydroid3),<br>
[百度网盘](https://pan.baidu.com/s/1C2Zc4sSt7_9W-ekeXXj6Rg?pwd=fema)<br>
[比邻云盘](https://pan.bilnn.com/s/qLa7T9)

建议装上Pydroid repository plugin，但想安装，要先装**Apkpure**。。。

[Apkpure](https://apkpure.com/cn/apkpure/com.apkpure.aegon),<br>
[百度网盘](https://pan.baidu.com/s/1C2Zc4sSt7_9W-ekeXXj6Rg?pwd=fema)<br>
[比邻云盘](https://pan.bilnn.com/s/qLa7T9)

然后再装**Pydroid repository plugin**

[Apkpure](https://apkpure.com/cn/pydroid-repository-plugin/ru.iiec.pydroid3.quickinstallrepo),<br>
[百度网盘](https://pan.baidu.com/s/1C2Zc4sSt7_9W-ekeXXj6Rg?pwd=fema)<br>
[比邻云盘](https://pan.bilnn.com/s/qLa7T9)

tips:比邻云盘下载后记得把后缀从`aspx`改成`xapk`<br>
tips:新版本如果安装不了python可以用旧版本<br>
tips：注意版本号！5.0的Pydroid要用2.0的Pydroid repository plugin，<br>
4.01的pydroid要用1.01的Pydroid repository plugin

1. 安装Apkpure
2. 打开，点**我的**，**应用管理**，**APK/XAPK管理**
3. 安装**Pydroid3**，**Pydroid repository plugin**
4. 打开Pydroid3，自动安装python，如果有引导，就*continue*
5. 点左上角按钮，**Pip**
6. 输入库的名称，点**install**(目前用了两个库：`requests`和`lxml`)
7. 等待，直至出现*Successfully*
8. 重复6，7步，安装所有库，确定LIBRARIES里有`requests`和`lxml`
9. 下载源文件并打开<br>（嫌麻烦也可以把`getpinyin.py`的源代码复制粘贴到主界面内）
10. 点右下角运行按钮，Enjoy！