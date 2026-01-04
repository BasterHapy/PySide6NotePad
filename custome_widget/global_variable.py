from pathlib import Path
from PySide6.QtGui import QGuiApplication

STAR = "*"
DEFAULT_NAME = "无标题"
BASE_NAME = " - 记事本"
HOME_PATH = str(Path.home())


GLOBAL_CLIPBOARD = QGuiApplication.clipboard 