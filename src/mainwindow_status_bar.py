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
        self.start_end_label = QLabel()
        self.cursor_pos_label = QLabel("第 1行,第 1列")
        self.zoom_in_out_label = QLabel("100%")
        self.encode_label = QLabel("UTF-8")

        # 设置风格样式
        self.start_end_label.setStyleSheet(".QLabel {padding-right: 340px}")
        self.cursor_pos_label.setStyleSheet(".QLabel {padding-left: 10px;padding-right: 40px}")
        self.zoom_in_out_label.setStyleSheet(".QLabel {padding-right: 10px;padding-right: 40px;}")
        self.encode_label.setStyleSheet(".QLabel {padding-right: 40px}")

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
        self.cursor_pos_label.setText(f"第{row:>2}行,第{column:>2}列")
    
    def show_find_status(self,find_status:str):
        """显示查找状态

        :param find_status: start or end
        """
        if find_status == "start":
            self.start_end_label.setText("从顶部开始查找下一项!") 
            self.start_end_label.setStyleSheet(".QLabel {padding-right: 180px}")

        elif find_status == "end":
            self.start_end_label.setText("从底部开始查找下一项!")
            self.start_end_label.setStyleSheet(".QLabel {padding-right: 180px}")
            
        else:
            self.start_end_label.setText("")
        