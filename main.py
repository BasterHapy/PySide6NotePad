import sys
from PySide6.QtWidgets import QApplication,QStyleFactory
from src.notepad_main import NotePad
from PySide6.QtGui import QFont
import resource_rc

def main():
    """主函数"""
    # 创建程序 无需传入命令
    app = QApplication([])

    # 设置全局字体
    app.setFont(QFont("DejaVu Sans Mono", 11))
    ## 设置主题为支持明暗 Linux 默认支持
    app.setStyle(QStyleFactory.create("Fusion"))

    # 实例化记事本
    notepad = NotePad()

    # 显示记事本
    notepad.show()

    # 检测主循环退出
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
    