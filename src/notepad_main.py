from PySide6.QtWidgets import QMainWindow,QFrame
from src.mainwindow_plain_text_edit import PlainTextEdit
from src.mainwindow_menu_bar import MenuBar
from src.mainwindow_status_bar import StatusBar
from src.custome_signal_bus import signal_bus
from src.global_variable import BASE_NAME,DEFAULT_NAME,STAR                

class NotePad(QMainWindow):
    """记事本主窗口

    :param QMainWindow: PySide6 主窗口
    """
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.setup_event_bind()
    
    def setup_ui(self):
        """设置界面"""
        # 窗口设置
        self.setWindowTitle(f"{DEFAULT_NAME}{BASE_NAME}")
        self.resize(800, 500)

        # 菜单栏
        self.menu_bar = MenuBar()
        self.setMenuBar(self.menu_bar)

        # 实例化文本编辑
        self.plain_text_edit = PlainTextEdit()

        ## 取消边框
        self.plain_text_edit.setFrameShape(QFrame.Shape.NoFrame)
        
        ## 设置背景为白色
        self.plain_text_edit.setStyleSheet("QPlainTextEdit {background-color: white}")
        
        ##  中心控件设置为纯文本编辑
        self.setCentralWidget(self.plain_text_edit)

        # 实例化状态栏
        self.status_bar = StatusBar()
        self.setStatusBar(self.status_bar)
    
    def setup_event_bind(self):
        """设置事件绑定"""
        # 标题相关
        ## 更新*
        self.plain_text_edit.modificationChanged.connect(self.update_title)

        # 文本编辑相关
        ## 文件菜单
        self.menu_bar.file_menu.new_file.triggered.connect(self.plain_text_edit.show_msg_save)
        self.menu_bar.file_menu.new_window.triggered.connect(self.new_window)
        self.menu_bar.file_menu.open_file.triggered.connect(self.plain_text_edit.open_file)
        self.menu_bar.file_menu.save_file.triggered.connect(self.plain_text_edit.save_file)
        self.menu_bar.file_menu.save_file_as.triggered.connect(self.plain_text_edit.save_file_as)
        self.menu_bar.file_menu.print_file.triggered.connect(self.plain_text_edit.print_file)
        self.menu_bar.file_menu.exit_.triggered.connect(self.close)

        ## 编辑菜单
        self.plain_text_edit.undoAvailable.connect(self.menu_bar.edit_menu.undo.setEnabled)
        self.plain_text_edit.redoAvailable.connect(self.menu_bar.edit_menu.redo.setEnabled)
        self.plain_text_edit.copyAvailable.connect(self.menu_bar.edit_menu.copy.setEnabled)
        self.plain_text_edit.copyAvailable.connect(self.menu_bar.edit_menu.copy.setEnabled)
        self.plain_text_edit.copyAvailable.connect(self.menu_bar.edit_menu.delete.setEnabled)
        self.plain_text_edit.copyAvailable.connect(self.menu_bar.edit_menu.search.setEnabled)
        signal_bus.has_text.connect(self.menu_bar.edit_menu.find_.setEnabled)
        signal_bus.has_text.connect(self.menu_bar.edit_menu.find_next.setEnabled)
        signal_bus.has_text.connect(self.menu_bar.edit_menu.find_previous.setEnabled)


        self.menu_bar.edit_menu.undo.triggered.connect(self.plain_text_edit.undo)
        self.menu_bar.edit_menu.redo.triggered.connect(self.plain_text_edit.redo)
        self.menu_bar.edit_menu.cut.triggered.connect(self.plain_text_edit.cut)
        self.menu_bar.edit_menu.copy.triggered.connect(self.plain_text_edit.copy)
        self.menu_bar.edit_menu.paste.triggered.connect(self.plain_text_edit.paste)
        self.menu_bar.edit_menu.delete.triggered.connect(self.plain_text_edit.clear)
        self.menu_bar.edit_menu.select_all.triggered.connect(self.plain_text_edit.selectAll)
        self.menu_bar.edit_menu.date_.triggered.connect(self.plain_text_edit.insert_date_time)
        self.menu_bar.edit_menu.search.triggered.connect(self.plain_text_edit.bing_search)

        ## 查找 上一个 下一个 
        self.menu_bar.edit_menu.find_.triggered.connect(self.plain_text_edit.find_text_dialog.show)
        self.menu_bar.edit_menu.find_next.triggered.connect(self.plain_text_edit.find_next)
        self.menu_bar.edit_menu.find_previous.triggered.connect(self.plain_text_edit.find_previous)

        ## 格式菜单
        self.menu_bar.format_menu.auto_line_warp.toggled.connect(self.plain_text_edit.reset_line_warp_mode)
        self.menu_bar.format_menu.font_page.triggered.connect(self.plain_text_edit.get_font_dialog)

        ## 查看菜单
        self.menu_bar.view_menu.zoom_in_action.triggered.connect(self.plain_text_edit.zoomIn)
        self.menu_bar.view_menu.zoom_out_action.triggered.connect(self.plain_text_edit.zoom_out)
        self.menu_bar.view_menu.zoom_back_action.triggered.connect(self.plain_text_edit.reset_default_font_size)
        self.menu_bar.view_menu.show_status_bar.triggered.connect(self.status_bar.show_or_hide)

    def update_title(self,changed: bool):
        """更新标题*

        :param changed: 文本是否改变
        """
        if changed:
            if self.plain_text_edit.file_path:
                file_name = self.plain_text_edit.file_path.rsplit("/")[-1]
                self.setWindowTitle(f"{STAR}{file_name}{BASE_NAME}")
            else:
                self.setWindowTitle(f"{STAR}{DEFAULT_NAME}{BASE_NAME}")
        else:
            if self.plain_text_edit.file_path:
                file_name = self.plain_text_edit.file_path.rsplit("/")[-1]
                self.setWindowTitle(f"{file_name}{BASE_NAME}")
            else:
                self.setWindowTitle(f"{DEFAULT_NAME}{BASE_NAME}")        

    def new_window(self):
        """新窗口"""
        self.note_pad = NotePad()
        self.note_pad.show()