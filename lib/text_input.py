import streamlit as st 
from datetime import datetime
from io import StringIO
 
import streamlit as st
 
 

with st.form(key="my_form_sub"):

    st.markdown("""
        <style>
            .stTextInput {
                display: flex;
                align-items: center;
            }
            .stTextInput > label {
                width: 80px;  /* 设置 label 的宽度 */
                margin-right: 0px;  /* 设置 label 和输入框之间的间距 */
                margin-left: 0px;  /* 设置 label 和输入框之间的间距 */
                font-weight: bold;  /* 为 st.text_input 的标签加粗 */
                font-size: 16px;
            }
                    
            .stSlider {
                display: flex;
                align-items: center;
            }
            .stSlider > label {
                width: 80px;  /* 设置 label 的宽度 */
                margin-right: 0px;  /* 设置 label 和输入框之间的间距 */
                font-weight: bold;
                font-size: 16px;
            }
        </style>
    """, unsafe_allow_html=True)

    
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
        submitted_2 = st.form_submit_button("Submit_1" ,use_container_width=True)

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
        submitted = st.form_submit_button("Submitd_2",use_container_width=True,type="tertiary",icon="🔥")
       
        if submitted:
            st.write('Submitted!')
but = st.button("提交", key="button1",use_container_width=True,type="primary",icon="🔥")
if st.button("Aloha", type="tertiary"):
    st.write("Ciao")