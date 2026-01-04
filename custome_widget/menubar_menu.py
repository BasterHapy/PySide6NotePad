from PySide6.QtWidgets import QMenu
from PySide6.QtGui import QKeySequence,QDesktopServices
from custome_widget.messagebox_about_notepad import MessageAboutNote
from custome_widget.custome_signal_bus import signal_bus
from custome_widget.global_variable import GLOBAL_CLIPBOARD

class FileMenu(QMenu):
    """文件菜单

    :param QMenu: PySide6 菜单
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """设置菜单项"""
        self.setTitle("文件(&F)")
        self.new_file = self.addAction("新建(&N)",QKeySequence.StandardKey.New)
        self.new_window = self.addAction("新窗口(&W)","Ctrl+Shift+N")
        self.open_file = self.addAction("打开(&O)",QKeySequence.StandardKey.Open)
        self.save_file = self.addAction("保存(&S)",QKeySequence.StandardKey.Save)
        self.addSeparator()
        self.save_file_as = self.addAction("另存为(&A)",QKeySequence.StandardKey.SaveAs)
        self.print_file = self.addAction("打印(&P",QKeySequence.StandardKey.Print)
        self.addSeparator()
        self.exit_ = self.addAction("退出(&X)",QKeySequence.StandardKey.Close)
        
class EditMenu(QMenu):
    """编辑菜单

    :param QMenu: PySide6 菜单类
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.set_event_bind()
    
    def setup_ui(self):
        """设置菜单项"""
        self.setTitle("编辑(&E)",)
        self.undo = self.addAction("撤销(&U)",QKeySequence.StandardKey.Undo)
        self.redo = self.addAction("重做(&B)",QKeySequence.StandardKey.Redo)
        self.addSeparator()
        self.cut =  self.addAction("剪切(&T)",QKeySequence.StandardKey.Cut)
        self.copy = self.addAction("复制(&C)",QKeySequence.StandardKey.Copy)
        self.paste = self.addAction("粘贴(&P)",QKeySequence.StandardKey.Paste)
        self.delete = self.addAction("删除(&L)",QKeySequence.StandardKey.Delete)
        self.addSeparator()
        self.search =  self.addAction("使用Bing搜索")
        self.find_ = self.addAction("查找(&F)",QKeySequence.StandardKey.Find)
        self.find_next = self.addAction("查找下一个(&N)",QKeySequence.StandardKey.FindNext)
        self.find_previous =  self.addAction("查找上一个(&V)",QKeySequence.StandardKey.FindPrevious)
        self.replace_ =  self.addAction("替换(&R)",QKeySequence.StandardKey.Replace)
        goto =self.addAction("转到(&G)","F3")
        self.addSeparator()
        self.select_all = self.addAction("全选(&A)",QKeySequence.StandardKey.SelectAll)
        self.date_ = self.addAction("时间/日期(&D)","F5")

        # 默认状态  撤销、剪切、复制、粘贴、删除 、搜索、查找、查找上一个、查找下一个、转到 不可用
        self.undo.setEnabled(False)
        self.cut.setEnabled(False)
        self.copy.setEnabled(False)
        self.paste.setEnabled(False)
        self.delete.setEnabled(False)
        self.search.setEnabled(False)
        self.find_.setEnabled(False)
        self.find_next.setEnabled(False)
        self.find_previous.setEnabled(False)
        goto.setEnabled(False)

    def set_event_bind(self):
        """设置时间绑定"""
        # 设置状态 粘贴

        GLOBAL_CLIPBOARD().dataChanged.connect(self.reset_paste_state)

    def reset_paste_state(self):
        """重新设置粘贴状态
        """
        clipbaord_text = GLOBAL_CLIPBOARD().text()
        if clipbaord_text:
            self.paste.setEnabled(True)
        else:
            self.paste.setEnabled(False)

class FormatMenu(QMenu):
    """格式菜单

    :param QMenu: PySide6 菜单类
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """设置菜单界面"""
        self.setTitle("格式(&O)")

        # 自动换行 和 字体 行为
        self.auto_line_warp = self.addAction("自动换行(&W)")
        self.font_page = self.addAction("字体(&F)")

        # 自动换行 可勾选且默认勾选
        self.auto_line_warp.setCheckable(True)
        self.auto_line_warp.setChecked(True)

class ViewMenu(QMenu):
    """查卡菜单

    :param QMenu: PySide6 菜单类
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """设置菜单界面"""
        self.setTitle("查看(&V)")

        # 实例化子菜单 缩放
        zoom_menu = self.addMenu("缩放(&Z)")

        # 子菜单添加行为 放大和缩小
        self.zoom_in_action = zoom_menu.addAction("放大(&I)",QKeySequence.StandardKey.ZoomIn) # ctrl shidt +
        self.zoom_out_action = zoom_menu.addAction("缩小(&O)",QKeySequence.StandardKey.ZoomOut) # ctrl -

        # 查看菜单 添加 恢复默认缩放 和状态栏 行为
        self.zoom_back_action = self.addAction("恢复默认缩放","Ctrl+0")
        self.show_status_bar =  self.addAction("状态栏(&S)")  

        # 状态栏 设置为可勾选并且默认勾选
        self.show_status_bar.setCheckable(True)
        self.show_status_bar.setChecked(True)
    
class HelpMenu(QMenu):
    """帮助菜单

    :param QMenu: PySide6 菜单类
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()
        self.set_event_bind()

    def setup_ui(self):
        """设置菜单界面"""
        self.setTitle("帮助(&H)")

        # 实例化 查看帮助 发送反馈 分割符 关于记事本 行为
        self.help_web = self.addAction("查看帮助(&H)")
        self.send_feedback_action  = self.addAction("发送反馈(&F)")
        self.addSeparator()
        self.about_notepad = self.addAction("关于记事本(&A)")

    def set_event_bind(self):
        """设置事件绑定
        """
        self.help_web.triggered.connect(self.get_help_page)
        self.send_feedback_action.triggered.connect(self.send_feedback)
        self.about_notepad.triggered.connect(self.get_about_note)    

    def get_help_page(self):
        """获取帮助页面"""
        help_url = "https://blog.csdn.net/weixin_72637522?type=blog"
        QDesktopServices.openUrl(help_url)

    def send_feedback(self):
        """发送反馈"""
        send_url = "https://github.com/BasterHapy/PySide6NotePad/issues"
        QDesktopServices.openUrl(send_url)

    def get_about_note(self):
        """获取关于记事本"""
        about_note  = MessageAboutNote()
        about_note.exec()
