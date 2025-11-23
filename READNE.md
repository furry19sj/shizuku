# Shizuku 快速部署脚本

## 简介
这是一个用于自动化部署 Shizuku 应用的 Python 脚本，支持检查应用是否已安装、自动安装 APK、启动应用并执行 Shizuku 服务启动脚本，适用于需要快速配置 Shizuku 环境的场景（如开发调试、自动化测试等）。

## 功能特性
1. 自动检查设备是否已安装 Shizuku 应用
2. 未安装时自动通过 ADB 安装指定 APK 文件
3. 自动启动 Shizuku 管理界面
4. 配置 ADB 无线调试（TCP/IP 模式，端口 5555）
5. 自动执行 Shizuku 服务启动脚本

## 前置依赖
### 环境要求
- Python 3.6 及以上版本
- Windows 操作系统（脚本使用 `cmd /c` 执行命令，如需 Linux/macOS 支持需修改命令执行逻辑）
- 已配置 ADB 环境变量（确保命令行可直接执行 `adb` 命令）
- 安卓设备已开启开发者选项及 USB 调试模式
- 设备已通过 USB 连接至电脑（首次配置需 USB 连接，后续可无线调试）

### 依赖文件
1. 脚本文件：`shizuku_deploy.py`（可自定义文件名）
2. Shizuku APK 文件：命名为 `shizuku.apk`，并与脚本放在同一目录下
   - 下载地址：[Shizuku 官方仓库](https://github.com/RikkaApps/Shizuku) 或 [Google Play](https://play.google.com/store/apps/details?id=moe.shizuku.privileged.api)

## 使用步骤
1. **准备工作**
   - 确保安卓设备已开启 USB 调试（设置 → 开发者选项 → USB 调试）
   - 确认电脑已安装 Python 并配置环境变量，如未配置可直接运行 shizuku.exe
   - 确认 ADB 工具已安装并配置环境变量（可通过 `adb --version` 验证）

2. **运行脚本**
   ```bash
   # 进入脚本所在目录
   cd /shizuku/
   
   # 执行脚本
   python shizuku.py
