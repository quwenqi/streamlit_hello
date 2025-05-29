import streamlit as st
import tkinter as tk
from tkinter import filedialog
from log  import log_dis  
import logging



class HorizontalLayout:
    def __init__(self, widths, vertical_alignment="center"):
        # 创建列
        self.columns = st.columns(widths, vertical_alignment=vertical_alignment)

    def __getitem__(self, index):
        # 允许使用下标访问列
        return self.columns[index]

    def __iter__(self):
        # 允许迭代列
        return iter(self.columns)

    def add_widget(self, element, index):
        with self.columns[index]:
            element()


def select_folder_path():
    root = tk.Tk()
    root.withdraw()  # 隐藏主窗口
    folder_path = filedialog.askdirectory()  # 打开选择文件夹对话框
    root.destroy()  # 删除 Tkinter 对象``
    return folder_path


def main():
    st.title("水平布局示例")

    # 定义一个函数来创建文本输入框
    def create_note():
        return st.write("名称:")

    def create_text_input():
        if st.session_state.get("text_input_value", False):
            return st.text_input(label="输入内容",value=st.session_state["text_input_value"], placeholder="输入内容", label_visibility='collapsed', key="text_input")
        else:
            return st.text_input(label="输入内容", placeholder="输入内容", label_visibility='collapsed', key="text_input")
    # 定义一个函数来创建按钮
    def create_button():
        return st.button("下载", key="send_button")
    
        # 定义一个函数来创建按钮
    def create_button_select():
        return st.button("..", key="select_button")

    # 创建一个水平布局，宽度比例为 1:10:2
    layout = HorizontalLayout([1, 8, 2, 2], vertical_alignment="center")

    # 在第一列中显示文本
    layout.add_widget(create_note, 0)

    # 将文本输入框添加到第二列
    layout.add_widget(create_text_input, 1)

    # 将按钮添加到第三列
    layout.add_widget(create_button_select, 2)

    # 将按钮添加到第三列
    layout.add_widget(create_button, 3)

    # 检查按钮是否被点击
    if st.session_state.get("send_button", False):
        st.write(f"send: {st.session_state.text_input}")
        logging.info(f"send: {st.session_state.text_input}")

    # 检查按钮是否被点击
    if st.session_state.get("select_button", False):
        try:
            st.session_state.text_input_value = select_folder_path()
        except Exception as e: 
           st.error("读取文件出错: " + str(e))
        st.rerun()
    log_dis()


    

if __name__ == "__main__":
    main()