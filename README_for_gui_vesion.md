# 使用streamlit实现的图形化界面选课系统

## 简介
一个简单的选课系统。

## 运行
### 本地运行
clone 到本地后在src/目录下终端运行`streamlit run Course_Selecting_app.py`。
### 云端运行
我已经在streamlit cloud 上完成了deploy,可直接进入网站`https://courseselecting-system.streamlit.app`使用，数据存储在github上。

## 功能说明
app分为student端和administrator端。

student端：选课、查看已选课程、支持多个学生使用;

administrator端：CourseList、StudentList、AddCourse、AddStudent;

administrator端设有密码，默认为`11111111`。可后台修改。