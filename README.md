## 一、使用说明:

### 1、导入/前置操作: （会操作的人em随你吧）
#### (1) 在使用之前,右击你的IDLE,选择"打开文件所在位置"选项
#### (2) 如果指向的还是一个快捷方式，一直重复(1)，直到指向一个名为pythonw.exe的文件为止
#### (2) 然后打开其中的Lib\site-packages文件夹,这就是存储python的第三方模块、包的位置
#### (3) 把此utilitytool文件夹直接复制到那里,完成!
#### (4) 导入:（废话这不谁都会吗）
import utilitytool as ut #使用时要用ut.前缀,例:ut.logintk 或 from utilitytool import *  #使用时不用ut.前缀,例: logintk

## 二、包含: 
去文件夹里面看看就行了

## 三、详细信息查看方式:
### 打开IDLE,不用新建文档,直接输入:
import utilitytool as ut 和 ut.模块名.__doc__() #模块名是你要查看详细信息的模块的名字（有些可能还没写）
