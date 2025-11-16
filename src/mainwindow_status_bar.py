from PySide6.QtWidgets import QStatusBar
from src.custome_signal_bus import signal_bus

class StatusBar(QStatusBar):
    """状态栏

    :param QStatusBar: PySide6 状态栏
    """
    def __init__(self,parent=None):
        super().__init__(parent)

    def show_or_hide(self,toggled:bool):
        """事件处理"""
        if toggled:
            self.show()
        else:
            self.hide()