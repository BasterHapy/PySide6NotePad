import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtGui import QPainter, QPen, QPixmap
from PySide6.QtWidgets import QApplication, QWidget
 
 
class DemoMouseEvent(QWidget):
    def __init__(self, parent=None):
        super(DemoMouseEvent, self).__init__(parent)
 
        # 设置窗口标题
        self.setWindowTitle('鼠标事件演示')
        # 设置窗口大小
        self.setFixedSize(480, 320)
 
        self.beginPoint = QPoint()  # 起始点
        self.endPoint = QPoint()  # 结束点
 
        self.pixmap = QPixmap(self.rect().size())
        self.pixmap.fill(Qt.lightGray)
 
    # 重绘窗口事件
    def paintEvent(self, event):
        pp = QPainter(self.pixmap)
        pp.setPen(QPen(Qt.blue, 2))  # 设置画笔
 
        # 绘制直线
        pp.drawLine(self.beginPoint, self.endPoint)
        # 上一直线的终点就是下一直线的起点
        self.beginPoint = self.endPoint
 
        # 在画布上画出
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.pixmap)
 
    def wheelEvent(self, ev):
        mods = ev.modifiers()
        #print('mods=', mods)
        delta = ev.angleDelta()
        #print('delta=', delta)
        if Qt.ControlModifier == int(mods):
            if int(delta.y())>0:
                print("ctrl 向上滚轮")
            else:
                print("ctrl 向下滚轮")
 
    def mousePressEvent(self, event):
        # 鼠标左键按下
        if event.button() == Qt.LeftButton:
            self.startPoint = event.pos()
 
    def mouseReleaseEvent(self, event):
        # 鼠标左键释放
        if event.button() == Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新绘制
            self.update()
 
    def mouseMoveEvent(self, event):
        # 鼠标左键按下的同时移动鼠标
        if event.buttons() and Qt.LeftButton:
            self.endPoint = event.pos()
            # 重新绘制
            self.update()
 
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DemoMouseEvent()
    window.show()
    sys.exit(app.exec())