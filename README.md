# PySide6 记事本 (PySide6NotePad)

windows 10
![Windows 10 工作站](./resource/show/windows10Show.jpg)

fedora43 wayland
![Fedora 43 Wayland](./resource/show/fedora43WaylandShow.png)

Kubuntu2404 x11
![Kubuntu 24.04 X11](./resource/show/Kubuntu2404X11Show.jpg)

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![PySide6](https://img.shields.io/badge/PySide6-6.10-green.svg)](LICENSE)

一款使用PySide6 实现的win10风格的跨平台记事本应用。
 
本项目是基于PySide 6技术开发的“模仿性学习”实践案例——初衷就是让刚接触PySide 6的小伙伴，通过模仿Windows系统原生记事本的功能开发，直观掌握PySide 6 GUI开发的核心逻辑、控件使用与交互实现技巧。虽主要聚焦PySide 6，但项目中涉及的多数开发逻辑与PyQt兼容，PyQt学习者也能参考使用。
 
目前项目会持续维护win10记事本基础功能，确保模仿学习的核心案例稳定可用；同时会重点围绕“模仿性学习”优化：比如补充PySide 6相关的详细代码注释、整理模仿开发过程中的常见问题解决方案、录制针对新手的模仿开发拆解视频等。

# 如何运行
建议使用[uv](https://uv.doczh.com/)工具

## 克隆项目
```bash
git clone https://github.com/BasterHapy/PySide6NotePad.git
```

## 进入目录文件夹
```bash
cd PySide6NotePad
```
## 创建虚拟机环境
```bash
uv venv pyside6_venv -p 3.11
```
## 安装Python依赖
```bash
uv pip install -r requirements.txt
```
## 运行
```bash
python main.py
```

## 许可证
本项目采用 GNU GPL v3 许可证；详见 [LICENSE](./LICENSE) 文件。
