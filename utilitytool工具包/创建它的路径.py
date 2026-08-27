#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
创建路径.txt文件
"""

import os

def create_path_file():
    """创建路径.txt文件"""
    
    print("创建路径.txt文件")
    print("=" * 30)
    
    # 获取当前目录
    current_dir = os.getcwd()
    print(f"当前目录: {current_dir}")
    print()
    
    # 输入第一条路径（源路径）
    print("请输入第一条路径（包含utilitytool文件夹的路径）:")
    print("示例: E:/a/制作ing")
    print("留空则使用当前目录")
    path1 = input("> ").strip()
    
    if not path1:
        path1 = current_dir
        print(f"使用当前目录: {path1}")
    
    # 检查路径中是否有utilitytool文件夹
    utilitytool_path = os.path.join(path1, "utilitytool")
    if not os.path.exists(utilitytool_path):
        print(f"⚠ 警告: 路径 {path1} 中没有找到 utilitytool 文件夹")
        confirm = input("是否继续? (y/n): ").strip().lower()
        if confirm != 'y' and confirm != 'yes':
            print("操作取消")
            return
    
    # 输入第二条路径（目标路径）
    print()
    print("请输入第二条路径（要复制到的目标路径）:")
    print("示例: D:/备份/项目")
    path2 = input("> ").strip()
    
    if not path2:
        print("错误: 目标路径不能为空")
        return
    
    # 写入文件
    with open("路径.txt", "w", encoding="utf-8") as f:
        f.write(path1 + "\n")
        f.write(path2 + "\n")
    
    print()
    print("✅ 路径.txt 创建成功!")
    print("文件内容:")
    print("-" * 20)
    print(path1)
    print(path2)
    print("-" * 20)
    
    input("\n按 Enter 退出...")

if __name__ == "__main__":
    create_path_file()
