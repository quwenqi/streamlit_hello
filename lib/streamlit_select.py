import os
import streamlit as st
from streamlit_tree_select import tree_select

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

# 指定要加载的本地文件夹路径
folder_path = "/home/ftpuser2"

# 获取文件夹结构
folder_nodes = get_folder_structure(folder_path)

# 展示树形菜单
st.title("本地文件夹树形菜单")
return_select = tree_select(nodes=folder_nodes)

# 显示选择结果
if return_select:
    st.write("已选择的文件夹/文件：")
    st.write(return_select)