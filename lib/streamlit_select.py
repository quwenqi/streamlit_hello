import os
import streamlit as st
from streamlit_tree_select import tree_select

import tkinter as tk
from tkinter import filedialog

def select_folder_path():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory()  # 打开选择文件夹对话框
    root.destroy()  # 删除 Tkinter 对象``
    return folder_path

def get_folder_structure(path):
    """获取文件夹结构并转换为 tree_select 所需的 nodes 格式"""
    nodes = []
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        node = {"label": item, "value": item_path}
        if os.path.isdir(item_path):
            node["children"] = get_folder_structure(item_path)
        nodes.append(node)
    return nodes

if 'folder_path' not in st.session_state: 
    st.session_state.folder_path = None

if 'button_label' not in st.session_state:
    st.session_state.button_label = "选择文件夹路径:"

# 展示树形菜单
st.title("本地文件夹树形菜单")
 
 
if st.button(st.session_state.button_label):
    folder_path = select_folder_path()
    if folder_path:
        st.session_state.button_label = "选择文件夹路径:"
        st.session_state.folder_path = folder_path
        st.session_state.button_label+=folder_path
        st.rerun()
        
 

if st.session_state.folder_path:
    folder_nodes = get_folder_structure(st.session_state.folder_path)
    return_select = tree_select(nodes=folder_nodes)

    # 显示选择结果
    if return_select:
        st.write("已选择的文件夹/文件：")
        st.write(return_select)