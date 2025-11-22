from PySide6.QtWidgets import QMessageBox
from PySide6.QtGui import QPixmap,QIcon

class MessageAboutNote(QMessageBox):
    """关于记事本对话框

    :param QMessageBox: PySide6 消息盒子
    """
    def __init__(self,parent=None):
        """初始化"""
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """设置界面"""
        # 窗口设置
        self.setWindowTitle("关于记事本")
        self.setWindowIcon(QIcon(":/resource/notepad.ico"))
        self.setIconPixmap(QPixmap(":/resource/notepad.png"))

        # 设置显示文本
        self.setText("使用PySide6实现的win10记事本\n作者：开心-开心急了")

        # 添加按钮
        self.addButton("确定",QMessageBox.ButtonRole.YesRole)
