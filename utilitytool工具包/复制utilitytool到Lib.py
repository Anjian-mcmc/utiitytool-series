#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
将路径.txt中的第一条路径的utilitytool文件夹复制到第二条路径
如有重复则覆盖
"""

import os
import shutil

def read_paths(file_path):
    """读取路径.txt中的两条路径"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        
        if len(lines) < 2:
            print(f"错误: 路径.txt中需要至少2条路径，当前只有{len(lines)}条")
            return None, None
        
        source_base = lines[0]
        target_base = lines[1]
        
        return source_base, target_base
        
    except FileNotFoundError:
        print(f"错误: 找不到文件 {file_path}")
        return None, None
    except Exception as e:
        print(f"读取路径文件时出错: {e}")
        return None, None

def copy_utilitytool_folder(source_base, target_base):
    """复制utilitytool文件夹"""
    
    # 构建完整路径
    source_folder = os.path.join(source_base, "utilitytool")
    target_folder = os.path.join(target_base, "utilitytool")
    
    print(f"源文件夹: {source_folder}")
    print(f"目标文件夹: {target_folder}")
    
    # 检查源文件夹是否存在
    if not os.path.exists(source_folder):
        print(f"错误: 源文件夹不存在 - {source_folder}")
        return False
    
    if not os.path.isdir(source_folder):
        print(f"错误: 源路径不是文件夹 - {source_folder}")
        return False
    
    # 创建目标目录（如果不存在）
    os.makedirs(target_base, exist_ok=True)
    
    try:
        # 如果目标文件夹已存在，先删除
        if os.path.exists(target_folder):
            print(f"目标文件夹已存在，正在删除...")
            shutil.rmtree(target_folder)
        
        # 复制整个文件夹
        print("正在复制文件夹...")
        shutil.copytree(source_folder, target_folder)
        
        print(f"✅ 复制完成!")
        print(f"从: {source_folder}")
        print(f"到: {target_folder}")
        
        # 统计复制了多少文件
        file_count = 0
        for root, dirs, files in os.walk(target_folder):
            file_count += len(files)
        
        print(f"共复制了 {file_count} 个文件")
        return True
        
    except PermissionError:
        print(f"错误: 权限不足，请以管理员身份运行")
        return False
    except Exception as e:
        print(f"复制过程中出错: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("utilitytool 文件夹复制工具")
    print("=" * 50)
    
    # 检查当前目录下是否有路径.txt
    path_file = "路径.txt"
    
    if not os.path.exists(path_file):
        print(f"当前目录没有找到 {path_file}")
        print(f"请确保 {path_file} 文件与脚本在同一目录")
        print()
        print("路径.txt 格式示例:")
        print("E:/a/制作ing")
        print("D:/备份/项目")
        input("\n按 Enter 退出...")
        return
    
    # 读取路径
    source_base, target_base = read_paths(path_file)
    if source_base is None or target_base is None:
        input("\n按 Enter 退出...")
        return
    
    print(f"源路径: {source_base}")
    print(f"目标路径: {target_base}")
    print()
    
    # 确认操作
    confirm = input("是否开始复制? (y/n): ").strip().lower()
    if confirm != 'y' and confirm != 'yes':
        print("操作取消")
        input("\n按 Enter 退出...")
        return
    
    print()
    # 执行复制
    success = copy_utilitytool_folder(source_base, target_base)
    
    if success:
        print("\n🎉 操作成功完成!")
    else:
        print("\n❌ 操作失败!")
    
    input("\n按 Enter 退出...")

if __name__ == "__main__":
    main()
