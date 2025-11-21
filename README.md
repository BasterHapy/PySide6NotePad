# PySide6 记事本 (PySide6NotePad)

一款使用PySide6 实现的win10风格的跨平台记事本应用。

[![Python](https://img.shields.io/badge/python-3.11-blue)](https://www.python.org/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
[![PySide6](https://img.shields.io/badge/PySide6-6.10-green.svg)](LICENSE)

## 目录
- [关于](#关于)
- [特性](#特性)
- [构建所需](#构建所需)
- [快速开始](#快速开始)
- [运行](#运行)
- [打包为 deb / rpm](#打包为-deb--rpm)
- [测试](#测试)
- [贡献](#贡献)
- [许可证](#许可证)
- [致谢](#致谢)

## 关于
该项目演示如何使用 PySide6 构建桌面 GUI 应用，并提供将应用打包为系统安装包（如 .deb、.rpm）的常见方法与示例命令。

## 特性
- 基本文本编辑（打开/保存/新建）
- 多文档/标签（如实现）
- Qt 资源支持（图标、样式）
- 支持通过 pyinstaller、fpm 等工具打包为独立可执行与系统包

## 构建所需
- Python >= 3.11
- pip
- (开发) PySide6
- 可选工具：pyinstaller, fpm, dpkg-deb, rpmbuild

示例 requirements.txt:
```text
PySide6>=6.0
```

## 快速开始（开发环境）
1. 克隆仓库并进入项目目录
```bash
git clone <repo-url>
cd PySide6NotePad
```

2. 创建并激活 Python 虚拟环境（确保使用 Python >= 3.11）
```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## 运行
从项目根目录运行主程序（示例）
```bash
python main.py
```

或在已打包的可执行中直接运行。

## 打包为 deb / rpm（常见方法）
下面示例假设项目在项目根以目录形式分发，程序入口为 `main.py`，并希望安装到 `/opt/pyside6_notepad` 或把可执行放到 `/usr/local/bin`。

方案 A — 使用 fpm（简单快速）：
1. 安装 fpm（需要 Ruby）
```bash
gem install --no-document fpm
```
2. 生成 deb 包（示例）
```bash
fpm -s dir -t deb -n pyside6-notepad -v 1.0.0 --prefix /opt/pyside6_notepad \
    -C . \
    main.py src resource resource_rc.py README.md
```
生成 rpm：
```bash
fpm -s dir -t rpm -n pyside6-notepad -v 1.0.0 --prefix /opt/pyside6_notepad ...
```
可在 fpm 中添加依赖声明：--depends "python3 (>= 3.11)"

方案 B — pyinstaller + 系统打包（推荐生成独立可执行减少目标系统依赖）：
1. 生成独立可执行
```bash
pip install pyinstaller
pyinstaller --onefile main.py
```
2. 使用 fpm 或 dpkg 工具将可执行打包为 deb/rpm
```bash
# 将 dist/main 放到 /usr/local/bin 并生成 deb
fpm -s dir -t deb -n pyside6-notepad -v 1.0.0 --prefix /usr/local/bin dist/main
```

方案 C — 原生打包方式（生产级）
- Debian/Ubuntu：在项目中添加 debian/ 目录并使用 dpkg-buildpackage 或 debuild
- RHEL/Fedora：编写 .spec 文件并用 rpmbuild 构建 rpm

注意事项：
- GUI 应用可能需要同时安装运行时依赖（字体、Qt 运行库），或选择将所有依赖打包进单个可执行。
- 生产包应包含桌面文件（.desktop）、图标安装路径与 postinst/preinst 脚本来创建快捷方式。

## 贡献
欢迎提交 issue 与 PR。请遵循项目的代码风格与贡献指南。提 PR 时请说明改动目的与测试步骤。

## 许可证
本项目采用 GNU GPL v3 许可证；详见 LICENSE 文件。

## 致谢
参考并部分样式借鉴自 Best-README-Template（othneildrew/Best-README-Template）。