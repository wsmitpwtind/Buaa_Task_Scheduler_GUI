# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacetgaKzO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(827, 484)
        MainWindow.setStyleSheet(u"*{color: #fff; border: none;}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"NovaFlat")
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"@font-face {\n"
"    font-family: NovaFlat;\n"
"    src: url(:/fonts/Nova_Flat/NovaFlat-Regular.ttf) format(\"truetype\");\n"
"}\n"
"*{\n"
"color: #fff;\n"
"font-family: NovaFlat;\n"
"font-size: 12px;\n"
"border: nine;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(33, 43, 51);\n"
"}\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_frame = QFrame(self.centralwidget)
        self.left_menu_frame.setObjectName(u"left_menu_frame")
        self.left_menu_frame.setMinimumSize(QSize(0, 0))
        self.left_menu_frame.setMaximumSize(QSize(200, 16777215))
        self.left_menu_frame.setStyleSheet(u"background-color: rgba(61, 80, 95, 100)")
        self.left_menu_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_menu_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.left_menu_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(61, 80, 95);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 0, 5)
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/icons/icons/pie-chart.svg"))
        self.label_2.setScaledContents(True)
        self.label_2.setWordWrap(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"NovaFlat")
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.left_menu_frame)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet(u"QFrame{background: none;}\n"
"QPushButton{\n"
"padding: 10px;\n"
"border-radius: 5px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.frame_12 = QFrame(self.frame_4)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.percentage_bar_btn = QPushButton(self.frame_12)
        self.percentage_bar_btn.setObjectName(u"percentage_bar_btn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.percentage_bar_btn.setIcon(icon)

        self.verticalLayout_4.addWidget(self.percentage_bar_btn)

        self.temperature_bar_btn = QPushButton(self.frame_12)
        self.temperature_bar_btn.setObjectName(u"temperature_bar_btn")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.temperature_bar_btn.setIcon(icon1)

        self.verticalLayout_4.addWidget(self.temperature_bar_btn)

        self.nested_donut_btn = QPushButton(self.frame_12)
        self.nested_donut_btn.setObjectName(u"nested_donut_btn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/target.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.nested_donut_btn.setIcon(icon2)

        self.verticalLayout_4.addWidget(self.nested_donut_btn)

        self.line_chart_btn = QPushButton(self.frame_12)
        self.line_chart_btn.setObjectName(u"line_chart_btn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/git-merge.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.line_chart_btn.setIcon(icon3)

        self.verticalLayout_4.addWidget(self.line_chart_btn)

        self.bar_charts_btn = QPushButton(self.frame_12)
        self.bar_charts_btn.setObjectName(u"bar_charts_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.bar_charts_btn.setIcon(icon4)

        self.verticalLayout_4.addWidget(self.bar_charts_btn)


        self.verticalLayout_3.addWidget(self.frame_12, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.left_menu_frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"background-color: rgb(61, 80, 95);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(30, 30))
        self.label_4.setMaximumSize(QSize(30, 30))
        self.label_4.setPixmap(QPixmap(u":/icons/icons/smile.svg"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_4)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)


        self.verticalLayout.addWidget(self.frame_5, 0, Qt.AlignBottom)

        self.frame_6 = QFrame(self.left_menu_frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QFrame{background: none;}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setFamily(u"NovaFlat")
        font2.setBold(False)
        font2.setWeight(50)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"")

        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 2, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(30, 30))
        self.label_8.setMaximumSize(QSize(30, 30))
        self.label_8.setPixmap(QPixmap(u":/images/images/icons8-patreon-50.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(30, 30))
        self.label_9.setMaximumSize(QSize(30, 30))
        self.label_9.setPixmap(QPixmap(u":/images/images/icons8-youtube-studio-50.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_9, 1, 0, 1, 1)

        self.label_10 = QLabel(self.frame_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(30, 30))
        self.label_10.setMaximumSize(QSize(30, 30))
        self.label_10.setPixmap(QPixmap(u":/images/images/icons8-paypal-50.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_6, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.left_menu_frame)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        self.main_body_frame.setFrameShape(QFrame.StyledPanel)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.header_frame = QFrame(self.main_body_frame)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setMinimumSize(QSize(0, 32))
        self.header_frame.setMaximumSize(QSize(16777215, 16777215))
        self.header_frame.setStyleSheet(u"QFrame{background-color: rgb(61, 80, 95);}")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 0, 5)
        self.open_close_side_bar_btn = QPushButton(self.header_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/align-center.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon5)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn, 0, Qt.AlignLeft)

        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.frame_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_11, 0, Qt.AlignHCenter|Qt.AlignBottom)


        self.horizontalLayout_4.addWidget(self.frame_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(61, 80, 95);\n"
"	border-radius: 15px;\n"
"	border: 3px solid rgb(120, 157, 186);\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(120, 157, 186);\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, 0)
        self.minimize_window_button = QPushButton(self.frame_11)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        self.minimize_window_button.setMinimumSize(QSize(30, 30))
        self.minimize_window_button.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon6)

        self.horizontalLayout_5.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.frame_11)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMinimumSize(QSize(30, 30))
        self.restore_window_button.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.frame_11)
        self.close_window_button.setObjectName(u"close_window_button")
        self.close_window_button.setMinimumSize(QSize(30, 30))
        self.close_window_button.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon8)

        self.horizontalLayout_5.addWidget(self.close_window_button)


        self.horizontalLayout_4.addWidget(self.frame_11, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.frame_8 = QFrame(self.main_body_frame)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_8)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgba(61, 80, 95, 100)")
        self.percentage_bar_chart = QWidget()
        self.percentage_bar_chart.setObjectName(u"percentage_bar_chart")
        self.verticalLayout_6 = QVBoxLayout(self.percentage_bar_chart)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_13 = QFrame(self.percentage_bar_chart)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_13 = QLabel(self.frame_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"background-color: none;")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_13, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.frame_13, 0, Qt.AlignTop)

        self.frame = QFrame(self.percentage_bar_chart)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(0, 300))
        self.frame.setStyleSheet(u"QFrame{background-color: none;}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.percentage_bar_chart_cont = QGridLayout(self.frame)
        self.percentage_bar_chart_cont.setObjectName(u"percentage_bar_chart_cont")

        self.verticalLayout_6.addWidget(self.frame)

        self.stackedWidget.addWidget(self.percentage_bar_chart)
        self.nested_donuts = QWidget()
        self.nested_donuts.setObjectName(u"nested_donuts")
        self.verticalLayout_11 = QVBoxLayout(self.nested_donuts)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_15 = QFrame(self.nested_donuts)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_15)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_15 = QLabel(self.frame_15)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"background-color: none;")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_15, 0, Qt.AlignTop)


        self.verticalLayout_11.addWidget(self.frame_15)

        self.frame_7 = QFrame(self.nested_donuts)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setMinimumSize(QSize(0, 300))
        self.frame_7.setStyleSheet(u"QFrame{background-color: none;}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.nested_donut_chart_cont = QGridLayout(self.frame_7)
        self.nested_donut_chart_cont.setObjectName(u"nested_donut_chart_cont")

        self.verticalLayout_11.addWidget(self.frame_7)

        self.stackedWidget.addWidget(self.nested_donuts)
        self.line_charts = QWidget()
        self.line_charts.setObjectName(u"line_charts")
        self.verticalLayout_13 = QVBoxLayout(self.line_charts)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_17 = QFrame(self.line_charts)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_17)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_16 = QLabel(self.frame_17)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"background-color: none;")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_16, 0, Qt.AlignTop)


        self.verticalLayout_13.addWidget(self.frame_17)

        self.frame_16 = QFrame(self.line_charts)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setMinimumSize(QSize(0, 300))
        self.frame_16.setStyleSheet(u"QFrame{background-color: none;}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.line_charts_cont = QGridLayout(self.frame_16)
        self.line_charts_cont.setObjectName(u"line_charts_cont")

        self.verticalLayout_13.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.line_charts)
        self.bar_charts = QWidget()
        self.bar_charts.setObjectName(u"bar_charts")
        self.verticalLayout_15 = QVBoxLayout(self.bar_charts)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_19 = QFrame(self.bar_charts)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_19)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_17 = QLabel(self.frame_19)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font1)
        self.label_17.setStyleSheet(u"background-color: none;")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_17, 0, Qt.AlignTop)


        self.verticalLayout_15.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.bar_charts)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setMinimumSize(QSize(0, 300))
        self.frame_18.setStyleSheet(u"QFrame{background-color: none;}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.bar_charts_cont = QGridLayout(self.frame_18)
        self.bar_charts_cont.setObjectName(u"bar_charts_cont")

        self.verticalLayout_15.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.bar_charts)
        self.temperature_bar_chart = QWidget()
        self.temperature_bar_chart.setObjectName(u"temperature_bar_chart")
        self.verticalLayout_9 = QVBoxLayout(self.temperature_bar_chart)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_14 = QFrame(self.temperature_bar_chart)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_14)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_14 = QLabel(self.frame_14)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"background-color: none;")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_14, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.frame_2 = QFrame(self.temperature_bar_chart)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(0, 300))
        self.frame_2.setStyleSheet(u"QFrame{background-color: none;}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.temperature_bar_chart_cont = QGridLayout(self.frame_2)
        self.temperature_bar_chart_cont.setObjectName(u"temperature_bar_chart_cont")

        self.verticalLayout_9.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.temperature_bar_chart)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.verticalLayout_2.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.main_body_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_9)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.size_grip = QPushButton(self.frame_9)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))

        self.horizontalLayout_7.addWidget(self.size_grip)


        self.verticalLayout_2.addWidget(self.frame_9, 0, Qt.AlignBottom)


        self.horizontalLayout.addWidget(self.main_body_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"QT CHARTS", None))
        self.percentage_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.temperature_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Temperature Records", None))
        self.nested_donut_btn.setText(QCoreApplication.translate("MainWindow", u"Nested Donuts", None))
        self.line_chart_btn.setText(QCoreApplication.translate("MainWindow", u"Line Chats", None))
        self.bar_charts_btn.setText(QCoreApplication.translate("MainWindow", u"Bar Chars", None))
        self.label_4.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SUPPORT ME", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.patreon.com/spinntv\"><span style=\" text-decoration: underline; color:#fff;\">Patreon</span></a></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PayPal", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><a href=\"https://www.youtube.com/c/SpinnTV/\"><span style=\" text-decoration: underline; color:#fff;\">Subscribe To Youtube</span></a></p></body></html>", None))
        self.label_8.setText("")
        self.label_9.setText("")
        self.label_10.setText("")
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Percentage Bar Chart", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"LINE CHARTS", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"BAR CHARTS", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Temperature Bar Chart", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Copyright Spinn Co. V 1.0.1", None))
        self.size_grip.setText("")
    # retranslateUi

