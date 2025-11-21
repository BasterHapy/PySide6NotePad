from PySide6.QtWidgets import QMenuBar
from src.menubar_menu import FileMenu,EditMenu,FormatMenu,ViewMenu,HelpMenu

class MenuBar(QMenuBar):
    """菜单栏

    :param QMenuBar: PySide6 菜单栏
    """
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """设置菜单栏界面"""
        # 实例化 文件、编辑、格式、查看、帮助 菜单
        self.file_menu = FileMenu(self)
        self.edit_menu = EditMenu(self)
        self.format_menu = FormatMenu(self)
        self.view_menu = ViewMenu(self)
        self.help_menu = HelpMenu(self)

        # 添加多个按钮
        self.addMenu(self.file_menu)
        self.addMenu(self.edit_menu)
        self.addMenu(self.format_menu)
        self.addMenu(self.view_menu)
        self.addMenu(self.help_menu)

        # 背景为白色
        self.setStyleSheet("QMenuBar {background-color: white}")
