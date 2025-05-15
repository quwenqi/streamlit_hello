import streamlit as st 
from datetime import datetime
from io import StringIO
 


with st.form(key="my_form_sub"):
    # 创建一个水平容器
    col3_1,col3_2,col3_3 = st.columns(3,vertical_alignment='center',gap='small',border=False)  # 创建4列，等宽
    # 在每一列中放置控件
    with col3_1:
        text_input4 = st.text_input(
            label="ID:",
            #value="123",
            #label_visibility="collapsed",  # 隐藏标签
            key="1",
            placeholder="请输入内容"  # 提示文本
        )
    with col3_2:
        text_input = st.text_input(
            label="NAME:",
            value="",
            #label_visibility="collapsed",  # 隐藏标签
            placeholder="请输入内容",  # 提示文本
            key="2"
        )
    # 提交按钮放在第四列
    with col3_3:
        submitted_2 = st.form_submit_button("Submit_1" )

        if submitted_2:
            st.write('Submitted!')


with st.form(key="my_form_sub2"):




    # 创建一个水平容器
    col1,col2,col3,col4= st.columns(4,vertical_alignment='center',gap='small',border=False)  # 创建4列，等宽

    # 在每一列中放置控件
 

    with col1:
        text_input2 = st.text_input(
            label="ID:",
            #value="123",
            #label_visibility="collapsed",  # 隐藏标签
            key="2_1",
            placeholder="请输入内容"  # 提示文本
        )

    with col2:
        slider_value = st.slider(
            "SLIDER:",
            0,
            100,
            50,
            #label_visibility="collapsed",  # 隐藏标签
        )

    # 在每一列中放置控件
    with col3:
        text_input = st.text_input(
            label="NAME:",
            value="",
            #label_visibility="collapsed",  # 隐藏标签
            placeholder="请输入内容",  # 提示文本
            key="2_2"
        )

    # 提交按钮放在第四列
    with col4:
        submitted = st.form_submit_button("Submitd_2" )

        if submitted:
            st.write('Submitted!')
