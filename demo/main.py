########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
########################################################################

########################################################################
## IMPORTS
########################################################################
import sys
from PySide2 import *
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtGui import QPainter
from PySide2.QtWidgets import (QMainWindow, QApplication)
from PySide2.QtCharts import QtCharts

from random import randrange
from functools import partial
import csv

########################################################################
# IMPORT GUI FILE
from ui_interface import *
########################################################################

########################################################################
## A LIST OF UI WIDGETS TO APPLY SHADOW
########################################################################
shadow_elements = { 
    "left_menu_frame",
    "frame_3",
    "frame_5",
    "header_frame",
    "frame_9"
}

########################################################################
## MAIN WINDOW CLASS
########################################################################
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        #######################################################################
        ## # Remove window tittle bar
        ########################################################################    
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint) 

        #######################################################################
        ## # Set main background to transparent
        ########################################################################  
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
      
        #######################################################################
        ## # Shadow effect style
        ########################################################################  
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        
        #######################################################################
        ## # Appy shadow to central widget
        ########################################################################  
        self.ui.centralwidget.setGraphicsEffect(self.shadow)   

        #######################################################################
        # Set window Icon
        # This icon and title will not appear on our app main window because we removed the title bar
        #######################################################################
        self.setWindowIcon(QtGui.QIcon(":/icons/icons/pie-chart.svg"))
        # Set window tittle
        self.setWindowTitle("QT CHARTS")

        #################################################################################
        # Window Size grip to resize window
        #################################################################################
        QSizeGrip(self.ui.size_grip)

        #######################################################################
        #Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())
        #######################################################################
        #Close window
        self.ui.close_window_button.clicked.connect(lambda: self.close())
        #######################################################################
        #Restore/Maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())
        #######################################################################

        #######################################################################
        #Left Menu toggle button (Show hide menu labels)
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())


        # ###############################################
        # Function to Move window on mouse drag event on the tittle bar
        # ###############################################
        def moveWindow(e):
            # Detect if the window is  normal size
            # ###############################################  
            if self.isMaximized() == False: #Not maximized
                # Move window only when window is normal size  
                # ###############################################
                #if left mouse button is clicked (Only accept left mouse button clicks)
                if e.buttons() == Qt.LeftButton:  
                    #Move window 
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()
        #######################################################################
      
        #######################################################################
        # Add click event/Mouse move event/drag event to the top header to move the window
        #######################################################################
        self.ui.header_frame.mouseMoveEvent = moveWindow
        #######################################################################

        #######################################################################
        # SHOW WINDOW
        #######################################################################
        self.show()

        #######################################################################
        # Apply shadow to widgets on shadow_elements list
        #######################################################################
        for x in shadow_elements:
                #######################################################################
                ## # Shadow effect style
                ######################################################################## 
                effect = QtWidgets.QGraphicsDropShadowEffect(self)
                effect.setBlurRadius(18)
                effect.setXOffset(0)
                effect.setYOffset(0)
                effect.setColor(QColor(0, 0, 0, 255))  
                getattr(self.ui, x).setGraphicsEffect(effect) 

        #navigate to Settings page
        self.ui.percentage_bar_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.percentage_bar_chart))
        self.ui.temperature_bar_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.temperature_bar_chart))
        self.ui.nested_donut_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.nested_donuts))
        self.ui.line_chart_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.line_charts))
        self.ui.bar_charts_btn.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.bar_charts))

        self.create_percentage_bar_chart()
        self.temperature_records()
        self.create_nested_donuts()
        self.create_line_chart()
        self.create_bar_graph()


    #######################################################################
    # Update restore button icon on msximizing or minimizing window
    #######################################################################
    def restore_or_maximize_window(self):
        # If window is maxmized
        if self.isMaximized():
            self.showNormal()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/maximize-2.svg"))
        else:
            self.showMaximized()
            # Change Icon
            self.ui.restore_window_button.setIcon(QtGui.QIcon(u":/icons/icons/minimize-2.svg"))

     ########################################################################
    # Slide left menu function
    ########################################################################
    def slideLeftMenu(self):
        # Get current left menu width
        width = self.ui.left_menu_frame.width()

        # If minimized
        if width == 0:
            # Expand menu
            newWidth = 200
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/chevron-left.svg"))
        # If maximized
        else:
            # Restore menu
            newWidth = 0
            self.ui.open_close_side_bar_btn.setIcon(QtGui.QIcon(u":/icons/icons/align-center.svg"))

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_menu_frame, b"maximumWidth")#Animate minimumWidht
        self.animation.setDuration(550)
        self.animation.setStartValue(width)#Start value is the current menu width
        self.animation.setEndValue(newWidth)#end value is the new menu width
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.animation.start()
    #######################################################################


    #######################################################################
    # Add mouse events to the window
    #######################################################################
    def mousePressEvent(self, event):
        # ###############################################
        # Get the current position of the mouse
        self.clickPosition = event.globalPos()
        # We will use this value to move the window
    #######################################################################
    #######################################################################

    # 
    def create_percentage_bar_chart(self):

        set0 = QtCharts.QBarSet("Tesla")
        set1 = QtCharts.QBarSet("Google")
        set2 = QtCharts.QBarSet("Amazon")
        set3 = QtCharts.QBarSet("Facebook")
        set4 = QtCharts.QBarSet("WeChat")

        set0.append([1, 2, 3,  4, 5, 6])
        set1.append([5, 0, 0,  4, 0, 7])
        set2.append([3, 5, 8, 13, 8, 5])
        set3.append([5, 6, 7,  3, 4, 5])
        set4.append([9, 7, 5,  3, 1, 2])

        series = QtCharts.QPercentBarSeries()
        series.append(set0)
        series.append(set1)
        series.append(set2)
        series.append(set3)
        series.append(set4)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Leading Tech Companies in 2021")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)


        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        axis = QtCharts.QBarCategoryAxis()
        axis.append(categories)
        chart.createDefaultAxes()
        chart.setAxisX(axis, series)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)


        self.ui.chart_view = QtCharts.QChartView(chart)
        self.ui.chart_view.setRenderHint(QPainter.Antialiasing)
        self.ui.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)
        # QChart.setTheme(theme)

        # print(self.ui.chart_view.chart().theme())
        # self.ui.chart_view.chart().setBackgroundBrush(QtGui.QColor("gray"))

        # self.setCentralWidget(chart_view)

        # self.lineEdit = QLineEdit(self.percentage_bar_chart_cont)
        # self.lineEdit.setObjectName(u"lineEdit")

        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ui.chart_view.sizePolicy().hasHeightForWidth())
        self.ui.chart_view.setSizePolicy(sizePolicy)
        self.ui.chart_view.setMinimumSize(QSize(0, 300))
        self.ui.percentage_bar_chart_cont.addWidget(self.ui.chart_view, 0, 0,  9, 9)
        self.ui.frame.setStyleSheet(u"background-color: transparent")

    # 
    def temperature_records(self):
        low = QtCharts.QBarSet("Min")
        high = QtCharts.QBarSet("Max")
        low.append([-52, -50, -45.3, -37.0, -25.6, -8.0,
                    -6.0, -11.8, -19.7, -32.8, -43.0, -48.0])
        high.append([11.9, 12.8, 18.5, 26.5, 32.0, 34.8,
                     38.2, 34.8, 29.8, 20.4, 15.1, 11.8])

        series = QtCharts.QStackedBarSeries()
        series.append(low)
        series.append(high)

        chart = QtCharts.QChart()
        chart.addSeries(series)
        chart.setTitle("Temperature records in celcius")
        chart.setAnimationOptions(QtCharts.QChart.SeriesAnimations)

        categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul",
                      "Aug", "Sep", "Oct", "Nov", "Dec"]
        axisX = QtCharts.QBarCategoryAxis()
        axisX.append(categories)
        axisX.setTitleText("Month")
        chart.addAxis(axisX, Qt.AlignBottom)
        axisY = QtCharts.QValueAxis()
        axisY.setRange(-52, 52)
        axisY.setTitleText("Temperature [&deg;C]")
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisX)
        series.attachAxis(axisY)

        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)
        chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chart_view.sizePolicy().hasHeightForWidth())
        chart_view.setSizePolicy(sizePolicy)
        chart_view.setMinimumSize(QSize(0, 300))
        self.ui.temperature_bar_chart_cont.addWidget(chart_view, 0, 0, 9, 9)
        self.ui.frame_2.setStyleSheet(u"background-color: transparent")

    # 
    def create_nested_donuts(self):
        self.setMinimumSize(800, 600)
        self.donuts = []
        self.chart_view = QtCharts.QChartView()
        self.chart_view.setRenderHint(QPainter.Antialiasing)
        self.chart = self.chart_view.chart()
        self.chart.legend().setVisible(False)
        self.chart.setTitle("Nested donuts demo")
        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.chart_view.chart().setTheme(QtCharts.QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_view.sizePolicy().hasHeightForWidth())
        self.chart_view.setSizePolicy(sizePolicy)
        self.chart_view.setMinimumSize(QSize(0, 300))
        self.ui.nested_donut_chart_cont.addWidget(self.chart_view, 0, 0, 9, 9)
        self.ui.frame_7.setStyleSheet(u"background-color: transparent")

        self.min_size = 0.1
        self.max_size = 0.9
        self.donut_count = 5

        self.setup_donuts()

        self.update_timer = QTimer(self)
        self.update_timer.timeout.connect(self.update_rotation)
        self.update_timer.start(1250)

    def setup_donuts(self):
        for i in range(self.donut_count):
            donut = QtCharts.QPieSeries()
            slccount = randrange(3, 6)
            for j in range(slccount):
                value = randrange(100, 200)

                slc = QtCharts.QPieSlice(str(value), value)
                slc.setLabelVisible(True)
                slc.setLabelColor(Qt.white)
                slc.setLabelPosition(QtCharts.QPieSlice.LabelInsideTangential)

                # Connection using an extra parameter for the slot
                slc.hovered[bool].connect(partial(self.explode_slice, slc=slc))

                donut.append(slc)
                size = (self.max_size - self.min_size)/self.donut_count
                donut.setHoleSize(self.min_size + i * size)
                donut.setPieSize(self.min_size + (i + 1) * size)
                print(i)

            self.donuts.append(donut)
            self.chart_view.chart().addSeries(donut)



    def update_rotation(self):
        for donut in self.donuts:
            phase_shift =  randrange(-50, 100)
            donut.setPieStartAngle(donut.pieStartAngle() + phase_shift)
            donut.setPieEndAngle(donut.pieEndAngle() + phase_shift)

    def explode_slice(self, exploded, slc):
        if exploded:
            self.update_timer.stop()
            slice_startangle = slc.startAngle()
            slice_endangle = slc.startAngle() + slc.angleSpan()

            donut = slc.series()
            idx = self.donuts.index(donut)
            for i in range(idx + 1, len(self.donuts)):
                self.donuts[i].setPieStartAngle(slice_endangle)
                self.donuts[i].setPieEndAngle(360 + slice_startangle)
        else:
            for donut in self.donuts:
                donut.setPieStartAngle(0)
                donut.setPieEndAngle(360)

            self.update_timer.start()

        slc.setExploded(exploded)

    def create_line_chart(self):
        self.series = QtCharts.QLineSeries()
        self.series.append(0, 6)
        self.series.append(2, 4)
        self.series.append(3, 8)
        self.series.append(7, 4)
        self.series.append(10, 5)
        self.series.append(QPointF(11, 1))
        self.series.append(QPointF(13, 3))
        self.series.append(QPointF(17, 6))
        self.series.append(QPointF(18, 3))
        self.series.append(QPointF(20, 2))

        self.chart = QtCharts.QChart()
        self.chart.legend().hide()
        self.chart.addSeries(self.series)
        self.chart.createDefaultAxes()
        self.chart.setTitle("Simple line chart example")

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())
        self.chartView.setSizePolicy(sizePolicy)
        self.chartView.setMinimumSize(QSize(0, 300))
        self.ui.line_charts_cont.addWidget(self.chartView, 0, 0, 9, 9)
        self.ui.frame_16.setStyleSheet(u"background-color: transparent")

    def create_bar_graph(self):
        self.set0 = QtCharts.QBarSet("Jane")
        self.set1 = QtCharts.QBarSet("John")
        self.set2 = QtCharts.QBarSet("Axel")
        self.set3 = QtCharts.QBarSet("Mary")
        self.set4 = QtCharts.QBarSet("Sam")

        self.set0.append([1, 2, 3, 4, 5, 6])
        self.set1.append([5, 0, 0, 4, 0, 7])
        self.set2.append([3, 5, 8, 13, 8, 5])
        self.set3.append([5, 6, 7, 3, 4, 5])
        self.set4.append([9, 7, 5, 3, 1, 2])

        self.barSeries = QtCharts.QBarSeries()
        self.barSeries.append(self.set0)
        self.barSeries.append(self.set1)
        self.barSeries.append(self.set2)
        self.barSeries.append(self.set3)
        self.barSeries.append(self.set4)

        self.lineSeries = QtCharts.QLineSeries()
        self.lineSeries.setName("trend")
        self.lineSeries.append(QPoint(0, 4))
        self.lineSeries.append(QPoint(1, 15))
        self.lineSeries.append(QPoint(2, 20))
        self.lineSeries.append(QPoint(3, 4))
        self.lineSeries.append(QPoint(4, 12))
        self.lineSeries.append(QPoint(5, 17))

        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.barSeries)
        self.chart.addSeries(self.lineSeries)
        self.chart.setTitle("Line and barchart example")

        self.categories = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
        self.axisX = QtCharts.QBarCategoryAxis()
        self.axisX.append(self.categories)
        self.chart.setAxisX(self.axisX, self.lineSeries)
        self.chart.setAxisX(self.axisX, self.barSeries)
        self.axisX.setRange("Jan", "Jun")

        self.axisY = QtCharts.QValueAxis()
        self.chart.setAxisY(self.axisY, self.lineSeries)
        self.chart.setAxisY(self.axisY, self.barSeries)
        self.axisY.setRange(0, 20)

        self.chart.legend().setVisible(True)
        self.chart.legend().setAlignment(Qt.AlignBottom)

        self.chartView = QtCharts.QChartView(self.chart)
        self.chartView.setRenderHint(QPainter.Antialiasing)

        self.chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        self.chartView.chart().setTheme(QtCharts.QChart.ChartThemeDark)


        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chartView.sizePolicy().hasHeightForWidth())
        self.chartView.setSizePolicy(sizePolicy)
        self.chartView.setMinimumSize(QSize(0, 300))
        self.ui.bar_charts_cont.addWidget(self.chartView, 0, 0, 9, 9)
        self.ui.frame_18.setStyleSheet(u"background-color: transparent")



########################################################################
## EXECUTE APP
########################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
########################################################################
## END===>
########################################################################  
