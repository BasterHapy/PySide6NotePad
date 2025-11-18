from PySide6.QtWidgets import (QDialog,QLayout,QVBoxLayout,QHBoxLayout,QLabel,QLineEdit,QGroupBox,
                               QRadioButton,QCheckBox,QPushButton)

class FindTextDialog(QDialog):
    """查找(文本)对话框

    :param QDialog: PySide6 QDialog对话框
    """
    def __init__(self,parent=None):
        """初始化

        :param parent: 父窗口, defaults to None
        """
        super().__init__(parent)
        self.setup_ui()    

    def setup_ui(self):
        """设置界面
        """
        # 窗口标题设置 wayland 不支持 仅设置窗口关闭按钮
        self.setWindowTitle("查找")

        # 窗口按钮只显示 关闭 win11默认 x11 wayland 不支持
        
        # 主布局使用垂直布局
        global_vbox = QVBoxLayout(self)
        
        # 固定大小 x11 windows 支持 wayland 奇怪
        global_vbox.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)

        # 创建标签和行编辑 并设置伙伴关系 使用水平布局
        find_lb = QLabel("查找内容(&N)")
        self.find_le = QLineEdit()

        find_lb.setBuddy(self.find_le)

        ll_hbox = QHBoxLayout()
        ll_hbox.addWidget(find_lb)
        ll_hbox.addWidget(self.find_le)

        # 组框架 使用垂直布局 添加俩个圆角按钮: 向上和向下 默认向下
        direct_gb = QGroupBox(title="方向")

        gb_vbox = QVBoxLayout(direct_gb)
        
        self.up_rbtn = QRadioButton("向上(&U)")
        self.down_rbtn = QRadioButton("向下(&D)")

        self.down_rbtn.setChecked(True)

        gb_vbox.addWidget(self.up_rbtn)
        gb_vbox.addWidget(self.down_rbtn)

        # 区分大小写、循环 复选框 添加到主布局中
        self.case_check = QCheckBox("区分大小写(&C)")
        self.range_check = QCheckBox("循环(&R)")

        # 查找下一个 与取消按钮
        self.find_next_btn = QPushButton("查找下一个")
        self.cancel_btn = QPushButton("取消")

        # 主布局添加布局 或控件
        global_vbox.addLayout(ll_hbox)
        global_vbox.addWidget(direct_gb)
        global_vbox.addWidget(self.case_check)
        global_vbox.addWidget(self.range_check)
        global_vbox.addWidget(self.find_next_btn)
        global_vbox.addWidget(self.cancel_btn)

    def set_event_bind(self):
        """设置事件绑定
        """
        # 按钮选中绑定事件
        self.cancel_btn.clicked.connect(self.close)
            

            
        



        
        