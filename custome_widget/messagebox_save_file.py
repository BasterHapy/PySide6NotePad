from PySide6.QtWidgets import QMessageBox

class MessageSaveFile(QMessageBox):
    """保存文件消息框

    :param QMessageBox: PySide6 消息框
    """
    def __init__(self,parent=None):
        """初始化"""
        super().__init__(parent)
        self.filename = "无标题"
        self.setup_ui()
       

    def setup_ui(self):
        """设置界面"""
        # 窗口设置
        self.setWindowTitle("关于记事本")

        # 设置显示文本
        self.setText(f"你想要将更改保存到 {self.filename} 吗?")
        
        # 添加按钮
        self.addButton("取消",QMessageBox.ButtonRole.DestructiveRole)
        self.addButton("不保存(&N)",QMessageBox.ButtonRole.RejectRole)
        self.addButton("保存(&S)",QMessageBox.ButtonRole.AcceptRole)

