import streamlit as st

if 'remember_credentials' not in st.session_state:
    st.session_state.remember_credentials = False

if 'username' not in st.session_state:
    st.session_state.username = ""

if 'password' not in st.session_state:
    st.session_state.password = ""

 

with st.form("Credentials",clear_on_submit=True):  

    # 如果记住密码被勾选，则从 session_state 中读取用户名和密码

    username = st.session_state.username
    password = st.session_state.password
 

    usr=st.text_input("账号名称",  value=username)  
    pwd=st.text_input("账号密码",  value=password ,type="password")  
    # 添加记住密码选项
    remember_me = st.checkbox("记住密码",value = st.session_state.remember_credentials)
    submitted = st.form_submit_button("登录")

    # 处理记住密码选项
    if submitted:

        if usr == "admin" and pwd == "123456":
            st.success("登录成功！")
  
            # 更新 session_state 中的用户名和密码
            st.session_state.username = usr
            st.session_state.password = pwd
            st.session_state.logged_in = True

            if remember_me:
                st.session_state.remember_credentials = True
            else:
                st.session_state.remember_credentials = False
                st.session_state.username = ""
                st.session_state.password = ""

            st.rerun()
        else:
            st.error("账号或密码错误！")


def login():
    if st.button("Log in"):
        st.session_state.logged_in = True
        st.rerun()
        
#login()











 