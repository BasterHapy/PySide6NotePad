from PySide6.QtWidgets import QMainWindow,QMenu,QApplication,QFileDialog
import sys

class NotePad(QMainWindow):
    """记事本主窗口

    :param QMainWindow: PySide6 主窗口
    """
    def __init__(self):
        """初始化"""
        super().__init__()
        self.setup_ui()
        self.setup_event_bind()

    def setup_ui(self):
        """设置界面"""
        # 窗口设置
        self.setWindowTitle(f"无标题 - 记事本")
        self.resize(800, 500)

        # 菜单栏
        menu_bar = self.menuBar()

        # 文件菜单
        self.file_menu = FileMenu()
        menu_bar.addMenu(self.file_menu)

    def setup_event_bind(self):
        """设置事件绑定"""
        self.file_menu.new_window.triggered.connect(self.new_window)
        self.file_menu.open_file.triggered.connect(self.open_file)

    def new_window(self):
        """新窗口"""
        self.note_pad = NotePad()
        self.note_pad.show()
    
    def open_file(self):
        """新文件"""
        file_path,_  = QFileDialog.getOpenFileName(self,"打开","/home/happy","(*.txt);;(*.*)")      


class FileMenu(QMenu):
    """菜单栏

    :param QMenu: PySide6 菜单
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """设置菜单栏界面"""
        self.setTitle("文件")
        
        self.new_window =  self.addAction("新窗口")
        self.open_file = self.addAction("打开")

def main():
    # 实例化应用
    app = QApplication([])

    # 实例化记事本
    notepad = NotePad()

    # 显示记事本
    notepad.show()

    # 检测主循环退出
    sys.exit(app.exec())

if __name__ == "__main__":
    main()