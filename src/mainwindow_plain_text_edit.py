from PySide6.QtWidgets import QPlainTextEdit,QFontDialog,QFileDialog,QMessageBox
from PySide6.QtGui import QFont,QWheelEvent,QDesktopServices,QTextDocument
from PySide6.QtPrintSupport import QPrintDialog,QPrinter
from PySide6.QtCore import Qt,QDateTime
from src.messagebox_save_file import MessageSaveFile
from src.custome_signal_bus import signal_bus
from src.global_variable import HOME_PATH
from src.custome_find_dialog import FindTextDialog
from src.custome_replace_dialog import ReplaceDialog

class PlainTextEdit(QPlainTextEdit):
    """纯文本编辑

    :param QPlainTextEdit: PySide6 QPlainTextEdit
    """
    def __init__(self):
        """初始化"""
        super().__init__()

        #  实例化 查找与替换对话框
        self.find_text_dialog = FindTextDialog(self)
        self.replace_dialog = ReplaceDialog(self)
        
        self.set_event_bind()
        self.file_path = ""

    def has_text(self):
        """是否有文本"""
        if self.toPlainText():
            signal_bus.has_text.emit(True)
        else:
            signal_bus.has_text.emit(False)

    def set_event_bind(self):
        """设置事件绑定"""
        self.textChanged.connect(self.has_text)
        self.find_text_dialog.find_next_btn.clicked.connect(self.auto_find_next)
        self.replace_dialog.find_next_btn.clicked.connect(self.replace_find_next)
        self.replace_dialog.replace_btn.clicked.connect(self.replace_once)

    def show_msg_save(self):
        """是否显示保存文件消息框"""
        if self.get_modification_changed():
            msg_save = MessageSaveFile(self)
            msg_save.show()
        else:
            self.file_path = ""
            self.clear()

    def open_file(self):
        """打开文件"""
        self.file_path,_ = QFileDialog.getOpenFileName(self,"打开",HOME_PATH,"(*.txt);;(*.*)")

        if self.file_path:  

            with open(self.file_path,"r") as file:
                self.setPlainText(file.read())

    def save_file(self):
        """保存文件"""
        if self.file_path:

            with open(self.file_path,"w") as file:
                # 保存时 重置文本改变状态
                self.set_modification_changed(False)
                file.write(self.toPlainText())
        else:
            # 另存为
            self.save_file_as()

    def save_file_as(self):
        """保存文件"""
        # 保存文件 返回文件路径
        file_path,_ = QFileDialog.getSaveFileName(self,"另存为",HOME_PATH,"(*.txt);;(*.*)")

        if file_path:
    
            with open(file_path,"w") as file:
                file.write(self.toPlainText())

            # 将 文件路径 局部变量 更新为全局属性
            self.file_path = file_path

    def print_file(self):
        """打印文件"""
        printer = QPrinter()
        dialog = QPrintDialog(printer)
        if dialog.exec():
            self.print_(printer)

    def get_select_text(self):
        """获取选中文本"""
        return self.textCursor().selectedText()

    def bing_search(self):
        """Bing搜索

        :param plain_text_edit: PySide6 PlainTextEdit
        """
        search_text = self.get_select_text()
        QDesktopServices.openUrl(f"https://cn.bing.com/search?q={search_text}")      

    def insert_date_time(self):
        """插入日期时间
        """
        currentDateTime = QDateTime.currentDateTime()
        formattedTime = currentDateTime.toString("hh:mm yyyy/MM/dd")
        self.insertPlainText(formattedTime)

    def auto_find_next(self):
        """自动查找下一个
        """
        # 将 属性变为 局部变量
        find_dialog = self.find_text_dialog

        # 查找文本 下一个 忽略大小写 循环 状态
        find_text = find_dialog.find_le.text()
        down_btn_status = find_dialog.down_rbtn.isChecked()
        case_check_status = find_dialog.case_check.isChecked()
        range_check_status = find_dialog.range_check.isChecked()

        # 查找 上一个 忽略大小写 标签
        backward_flag = QTextDocument.FindFlag.FindBackward
        case_flag = QTextDocument.FindFlag.FindCaseSensitively

        # 先使用二分法 判断是否 点击向上或向下
        if down_btn_status:
            
            # 获取查找状态 处理向下循环
            find_status = self.find(find_text)
            self.handel_next_range(find_status,range_check_status,find_text)

            # 判断是否勾选 忽略大小写 处理向下循环
            if case_check_status:
                find_status = self.find(find_text,case_flag)
                self.handel_next_range(find_status,range_check_status,find_text)
                
        else:
            # 获取查找状态 处理向上循环
            find_status = self.find(find_text,backward_flag)
            self.handel_previous_range(find_status,find_text)            

            # 判断是否勾选 忽略大小写 处理向上循环
            if case_check_status:
                flags = backward_flag | case_flag

                # 获取查找状态 处理向上循环
                find_status = self.find(find_text,flags)
                self.handel_previous_range(find_status,find_text)

    def __find_next(self,check_status: bool,range_check_status: bool,search_text: str) -> bool:
        """查找下一个

        :param check_status: 勾选状态
        :param range_check_status: 循环勾选状态
        :param search_text: 查找文本
        :return: 查找状态
        """

        # 判断是否勾选 忽略大小写
        if check_status:
            flag = QTextDocument.FindFlag.FindCaseSensitively
            find_status = self.find(search_text,flag)
            
            # 处理向下循环
            self.handel_next_range(find_status,search_text)

            return find_status
        
        # 没有选中 默认
        else:
            find_status = self.find(search_text)

            # 处理向下循环
            self.handel_next_range(find_status,range_check_status,search_text)

            return find_status

    def find_previous(self):
        """查找上一个"""
        # 将 查找对话框 定义为局部变量 方便调用
        find_dialog = self.find_text_dialog

        # 获取查找对话框 里的 查找内容
        search_text = find_dialog.find_le.text()

        # findflags 忽略大小写 上一个
        case_sen = QTextDocument.FindFlag.FindCaseSensitively
        backward = QTextDocument.FindFlag.FindBackward
        

        # 再判断是否勾选 忽略大小写
        if find_dialog.case_check.isChecked():
            find_status = self.find(search_text,case_sen|backward)

            # 处理向上循环
            self.handel_previous_range(find_status,search_text)

        
        # 没有选中 默认
        else:
            find_status = self.find(search_text,backward)

            # 处理向上循环
            self.handel_previous_range(find_status,search_text)

    def text_find_next(self):
        """查找对话框获取下一个"""

        # 将全局属性定义为局部变量
        find_dialog = self.find_text_dialog
        
        # 获取 忽略大小写与循环 勾选状态 查找文本
        case_check_status = find_dialog.case_check.isChecked()
        range_check_status = find_dialog.range_check.isChecked()
        find_text = find_dialog.find_le.text()

        # 查找下一个
        self.__find_next(case_check_status,range_check_status,find_text)

    def replace_find_next(self):
        """替换对话框中查找下一个

        :return: 获取查找状态
        """

        # 将 查找对话框 定义为局部变量
        replace_dialog = self.replace_dialog

        # 获取 忽略大小写与循环 勾选状态 查找文本
        case_check_status = replace_dialog.case_sensitive_box.isChecked()
        range_check_status = replace_dialog.range_box.isChecked()
        find_text = replace_dialog.find_content_ledit.text()

        # 查找下一个
        find_status = self.__find_next(case_check_status,range_check_status,find_text)

        return find_status

    def replace_once(self):
        """单个替换"""

        # 查找下一个 然后 替换
        find_status = self.replace_find_next()

        # 如果查找不为空 则 替换
        if find_status:
            
            # 获取 替换文本
            replace_text = self.replace_dialog.find_replace_ledit.text()
            self.textCursor().insertText(replace_text)

    def handel_next_range(self, find_status: bool,range_check_staus: bool,search_text: str):    
        """查找下一个重置光标"""
        if find_status is False:
    
            # 查看是否勾选 循环状态 => 勾选则 重置光标为Start => 不勾选则弹出消息对话框
            if range_check_staus:
                self.moveCursor(self.textCursor().MoveOperation.Start)
            else:
                self.show_find_info_message(search_text)

    def handel_previous_range(self, find_status: bool,search_text: str):    
        """查找上一个重置光标"""
        if find_status is False:
    
            # 查看是否勾选 循环状态 => 勾选则 重置光标为End => 不勾选则弹出消息对话框
            if self.find_text_dialog.range_check.isChecked():
                self.moveCursor(self.textCursor().MoveOperation.End)
            else:
                self.show_find_info_message(search_text)
            
    def show_find_info_message(self,search_text: str):
        """显示查找信息消息框

        :param search_text: 查找文本
        """
        QMessageBox.information(self.find_text_dialog or self.replace_dialog,"记事本",f'找不到"{search_text}"',QMessageBox.StandardButton.Yes)

    def show_replace_dialog(self):
        """显示替换对话框"""

        # 将 查找对话框 替换为 局部变量
        find_dialog = self.find_text_dialog 
        
        # 同步 查找对话框 忽略大小写、循环 勾选状态
        self.replace_dialog.case_sensitive_box.setChecked(find_dialog.case_check.isChecked())
        self.replace_dialog.range_box.setChecked(find_dialog.range_check.isChecked())

        # 显示替换对话框
        self.replace_dialog.show()

    def zoom_out(self,range=1):
        """缩小方法"""
        if self.font().pointSize() <= 11 :
            self.zoomOut(0)
        else:
            self.zoomOut(1)
        
    def reset_default_font_size(self):
        """设置默认字体大小
        """
        self.setFont(QFont("DejaVu Sans Mono", 12))
    
    def reset_line_warp_mode(self,toggled: bool):
        """重置换行模式"""
        # 勾选时 自动换行且不显示水平滚动条
        if toggled is True:
            self.setLineWrapMode(self.LineWrapMode.WidgetWidth)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        
        # 取消勾选时 不自动换行且水平滚动条一直显示
        else:
            self.setLineWrapMode(self.LineWrapMode.NoWrap)
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        
    def get_font_dialog(self):
        """字体对话框"""
        ok,font = QFontDialog.getFont()
        if ok:
            self.setFont(font)

    def wheelEvent(self, e: QWheelEvent):
        """鼠标滚动事件"""
        # 获取 KeyboardModifier 查看是否等于 ControlModifier
        if e.modifiers() == Qt.KeyboardModifier.ControlModifier:

            # y轴滚动角度 => 上下滚动角度
            delta = e.angleDelta().y()

            # 向上
            if delta > 0:
                self.zoomIn()

            # 向下
            else:
                self.zoom_out()
        else:
            return super().wheelEvent(e)

    def get_modification_changed(self):
        """获取修改状态"""
        self.document().isModified()
        
    def set_modification_changed(self,changed:bool):
        """设置修改状态"""
        return self.document().setModified(changed)




