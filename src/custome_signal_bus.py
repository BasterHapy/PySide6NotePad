from PySide6.QtCore import QObject,Signal

class SignalBus(QObject):
    """ 信号总线 """
    statusbar_action_checked = Signal(bool) # 状态栏勾选行为
    line_warp_action_checked = Signal(bool) # 换行勾选行为
    has_text = Signal(bool) # 是否有文本
    modification_changed = Signal(bool,str) # 文本內容改变
    


# 创建全局信号总线实例（只实例化一次）
signal_bus = SignalBus()