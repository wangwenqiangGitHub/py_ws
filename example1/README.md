# Pyqt5应用程序开发步骤
## 安装环境
```
#安装python 
#更新pip
pip install -U pip
#权限
pip install --user <包>
pip install PyQt5
pip install PyQt5-tools
```

## 启动cmd,输入designer启动Qt Designer 设计界面
## 开始控件进行设计
## 使用控件文件转换为Python
```
#pyuic5 -o 名称.py 名称.ui 生成ui文件对应的py文件
pyuic5 -o xxx.py xxx.ui

```
## 创建主程序

```
