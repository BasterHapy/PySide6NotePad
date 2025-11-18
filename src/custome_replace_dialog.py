from PySide6.QtWidgets import (QDialog,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QPushButton,QCheckBox)

class ReplaceDialog(QDialog):
    """替换对话框

    :param QDialog: PySide6 对话框
    """
    def __init__(self,parent=None):
        """构造函数"""
        super().__init__(parent)
        self.setup_ui()

    def setup_ui(self):
        """设置用户界面"""

        # 标题设置为 替换
        self.setWindowTitle("替换")

        # 全局使用垂直布局
        global_vbox = QVBoxLayout(self)

        ## 查找内容使用 水平布局
        content_hbox = QHBoxLayout()

        ### 查找内容 标签以及输入框
        find_content_label =  QLabel("查找内容(&N):")
        find_content_ledit = QLineEdit()

        ### 设置伙伴关系 
        find_content_label.setBuddy(find_content_ledit)

        ## 布局添加控件
        content_hbox.addWidget(find_content_label)
        content_hbox.addWidget(find_content_ledit)

        ## 替换为 使用水平布局
        replace_hbox = QHBoxLayout()

        ### 替换为 标签以及输入框
        find_replace_label =  QLabel("替换为(&P):")
        find_replace_ledit = QLineEdit()

        ### 设置伙伴关系
        find_replace_label.setBuddy(find_replace_ledit)

        ## 布局添加控件
        replace_hbox.addWidget(find_replace_label)
        replace_hbox.addWidget(find_replace_ledit)

        ## 替换按钮们使用水平布局
        replace_btns_hbox = QHBoxLayout()

        ### 替换与全部替换按钮
        replace_btn = QPushButton("替换(&R)")
        all_replace_btn = QPushButton("全部替换(&A)")

        ## 布局添加控件
        replace_btns_hbox.addWidget(replace_btn)
        replace_btns_hbox.addWidget(all_replace_btn)

        ## 查找和取消 使用水平布局
        find_btns_hbox = QHBoxLayout()

        ### 查找下一个与取消按钮
        find_next_btn = QPushButton("查找下一个(&F)")
        cancel_btn = QPushButton("取消")

        ## 布局添加控件
        find_btns_hbox.addWidget(find_next_btn)
        find_btns_hbox.addWidget(cancel_btn)

        ## 勾选框们 使用垂直布局
        check_boxs_vbox = QVBoxLayout()

        ### 区分大小写 与 循环 勾选框
        case_sensitive_box = QCheckBox("区分大小写(&C)")
        range_box = QCheckBox("循环(&R)")

        ## 布局添加控件
        check_boxs_vbox.addWidget(case_sensitive_box)
        check_boxs_vbox.addWidget(range_box)

        # 全局布局添加布局
        global_vbox.addLayout(content_hbox)
        global_vbox.addLayout(replace_hbox)
        global_vbox.addLayout(replace_btns_hbox)
        global_vbox.addLayout(find_btns_hbox)
        global_vbox.addLayout(check_boxs_vbox)

        
        



