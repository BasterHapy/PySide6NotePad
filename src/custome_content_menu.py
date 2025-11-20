from PySide6.QtWidgets import QMenu

class ContentMenu(QMenu):
    """上下文菜单

    :param QMenu: PySide6 菜单类
    """
    def __init__(self,parent=None):
        """初始化"""
        super().__init__(parent)
        self.setup_ui()
    
    def setup_ui(self):
        """设置界面"""
        self.undo_action = self.addAction("撤销(&U)")
        self.addSeparator()
        self.cut_action = self.addAction("剪切(&T)")
        self.copy_action = self.addAction("复制(&C)")
        self.paste_action =  self.addAction("粘贴(&P)")
        self.delete_action = self.addAction("删除(&D)")
        self.addSeparator()
        self.select_all =  self.addAction("全选(&A)")
        self.addSeparator()
        self.bing_search_action = self.addAction("使用Bing搜索(&B)")
        self.addSeparator()

        # 从右边到左的阅读顺序
        self.read_right_left = self.addAction("从右到左的阅读顺序")

        # 默认 撤销 剪切  复制 粘贴 删除 全选 不可用
        self.undo_action.setEnabled(False)
        self.cut_action.setEnabled(False)
        self.copy_action.setEnabled(False)
        self.paste_action.setEnabled(False)
        self.delete_action.setEnabled(False)
        self.select_all.setEnabled(False)