[app]
# 核心修正：告诉 GitHub 代码在当前文件夹
source.dir = .
# 核心修正：必须写版本号
version = 0.1
title = 给你一个礼物
# 包名
package.name = opao_gift
package.domain = org.test

# 包含的文件后缀
source.include_exts = py,png,jpg,kv,atlas,mp3

# ！！！重点：必须包含 jnius 依赖 ！！！
requirements = python3,kivy==2.2.1,pyjnius

# ！！！重点：必须申请修改音量的权限 ！！！
android.permissions = MODIFY_AUDIO_SETTINGS, INTERNET

# (可选) 锁定屏幕方向为竖屏
orientation = portrait

# 如果你要在 MuMu 模拟器跑，建议加上 x86 架构

android.archs = armeabi-v7a, x86
