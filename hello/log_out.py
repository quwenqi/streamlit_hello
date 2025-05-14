import streamlit as st
with st.form("Credentials",clear_on_submit=True):  
    l,c,r=st.columns(3)
    with c:
        submitted = st.form_submit_button("退出")
        # 处理记住密码选项
        if submitted:
            st.session_state.logged_in = False
            st.rerun()
    
   
def logout():
    but=st.button("Log out")
    if but:
        st.session_state.logged_in = False
        st.rerun()
        
 