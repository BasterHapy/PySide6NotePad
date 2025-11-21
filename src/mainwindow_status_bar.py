from PySide6.QtWidgets import QStatusBar,QLabel
from src.custome_signal_bus import signal_bus

class StatusBar(QStatusBar):
    """状态栏

    :param QStatusBar: PySide6 状态栏
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """设置界面"""

        # 初始化 显示开头和结尾 光标位置 缩放比例 编码格式(固定)
        self.start_end_label = QLabel("从顶部开始查找下一项")
        self.cursor_pos_label = QLabel("第1行 第1列")
        self.zoom_in_out_label = QLabel("100%")
        self.encode_label = QLabel("UTF-8")

        # 设置风格样式
        self.start_end_label.setStyleSheet(".QLabel {padding-left: 10px;padding-right: 380px}")
        self.cursor_pos_label.setStyleSheet(".QLabel {padding-left: 10px;padding-right: 45px}")
        self.zoom_in_out_label.setStyleSheet(".QLabel {padding-right: 10px;padding-right: 45px;}")
        self.encode_label.setStyleSheet(".QLabel {padding-right: 45px}")

        # 全局添加控件
        self.addWidget(self.start_end_label)
        self.addWidget(self.cursor_pos_label)
        self.addWidget(self.zoom_in_out_label)
        self.addWidget(self.encode_label)
        
    def show_or_hide(self,toggled:bool):
        """事件处理"""
        if toggled:
            self.show()
        else:
            self.hide()

    def update_cursor_pos(self,row:int,column:int):
        """更新光标位置

        :param row: 光标的行
        :param column: 光标的列
        """
        self.cursor_pos_label.setText(f"第{row}行,第{column}列")