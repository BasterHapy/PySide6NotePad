from PySide6.QtWidgets import QPlainTextEdit,QFontDialog,QFileDialog
from PySide6.QtGui import QFont,QWheelEvent,QDesktopServices
from PySide6.QtPrintSupport import QPrintDialog,QPrinter
from PySide6.QtCore import Qt,QDateTime
from src.messagebox_save_file import MessageSaveFile
from src.custome_signal_bus import signal_bus
from src.global_variable import DEFAILT_NAME,HOME_PATH

class PlainTextEdit(QPlainTextEdit):
    """纯文本编辑

    :param QPlainTextEdit: PySide6 QPlainTextEdit
    """
    def __init__(self):
        """初始化"""
        super().__init__()
        self.file_path = ""

    def has_text(self):
        """是否有文本"""
        if self.toPlainText():
            signal_bus.has_text.emit(True)
        else:
            signal_bus.has_text.emit(False)

    def show_msg_save(self):
        """是否显示保存文件消息框"""
        if self.document().isModified():
            msg_save = MessageSaveFile(self)
            msg_save.show()
        else:
            pass

    def open_file(self):
        """打开文件"""
        self.file_path,_ = QFileDialog.getOpenFileName(self,"打开",HOME_PATH,"(*.txt);;(*.*)")

        if self.file_path:  
            # 文件路径不为空 更新全局变量 并读取文件
            signal_bus.modification_changed.emit(self.get_modification_changed,self.file_path.rsplit("/")[-1])
            with open(self.file_path,"r") as file:
                self.setPlainText(file.read())

    def save_file(self):
        """保存文件"""
        if self.file_path:
            
            # 文件路径不为空 更新全局变量 并读取文件
            signal_bus.modification_changed.emit(self.get_modification_changed,self.file_path.rsplit("/")[-1])

            with open(self.file_path,"w") as file:
                # 保存时 重置文本改变状态
                self.document().setModified(False)
                file.write(self.toPlainText())

            # 每次写入以后 撤销与重做状态 为Fasle
            self.setUndoRedoEnabled(False)

        else:
            # 另存为
            self.save_file_as()

    def save_file_as(self):
        """保存文件"""
        # 保存文件 返回文件路径
        file_path,_ = QFileDialog.getSaveFileName(self,"另存为",HOME_PATH,"(*.txt);;(*.*)")

        if file_path:
            
            # 文件路径不为空 更新全局变量 并读取文件
            signal_bus.modification_changed.emit(self.get_modification_changed,self.file_path.rsplit("/")[-1])

            with open(file_path,"w") as file:

                # 保存时 重置文本改变状态
                self.document().setModified(False)
                file.write(self.toPlainText())

            # 每次写入以后 撤销与重做状态 为Fasle
            self.setUndoRedoEnabled(False)

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
                self.zoomOut()
        else:
            return super().wheelEvent(e)

    def get_modification_changed(self):
        """获取修改状态"""
        return self.document().isModified()




