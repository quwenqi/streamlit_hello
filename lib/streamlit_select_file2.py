import streamlit as st
import pandas as pd

st.title("文件内容显示和编辑工具")

# 上传文件
uploaded_file = st.file_uploader("选择一个文件", type=["txt", "csv", "xlsx", "ini"])

if uploaded_file is not None:

    # 根据文件类型显示内容
    if uploaded_file.type == "text/plain":
        # 显示并编辑文本文件内容
        content = uploaded_file.read().decode("utf-8")
        edited_content = st.text_area("编辑文件内容", content, height=400)
        
        # 添加一个按钮来保存编辑后的内容
        if st.button("保存编辑内容"):
            with open("edited_file.txt", "w") as f:
                f.write(edited_content)
            st.success("文件内容已保存！")
    
    elif uploaded_file.type == "text/csv":
        df = pd.read_csv(uploaded_file)
        # 使用 st.data_editor 来编辑 DataFrame
        edited_df = st.data_editor(df)
        
        # 添加一个按钮来保存编辑后的内容
        if st.button("保存编辑内容"):
            edited_df.to_csv("edited_file.csv", index=False)
            st.success("文件内容已保存！")
    
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
        df = pd.read_excel(uploaded_file)
        # 使用 st.data_editor 来编辑 DataFrame
        edited_df = st.data_editor(df)
        
        # 添加一个按钮来保存编辑后的内容
        if st.button("保存编辑内容"):
            edited_df.to_excel("edited_file.xlsx", index=False)
            st.success("文件内容已保存！")

    else:
    # 显示并编辑文本文件内容
        content = uploaded_file.read().decode("utf-8")
        edited_content = st.text_area("编辑文件内容", content, height=400)
        
        # 添加一个按钮来保存编辑后的内容
        if st.button("保存编辑内容"):
            with open("edited_file.txt", "w") as f:
                f.write(edited_content)
            st.success("文件内容已保存！")