import streamlit as st 
from datetime import datetime

def my_callback():
    print(f"curdate: {datetime.now()} first: {st.session_state.value1} sec: {st.session_state.value2}")

    
#st.set_page_config(page_title="用户管理系统", layout="wide")
st.set_page_config(page_title="用户管理系统", layout="centered" ,  page_icon=":rocket:", initial_sidebar_state="auto",menu_items={
        "Get Help": "https://example.com/help",
        "About": "Built by [Your Company](https://your-company.com)"
    })
#点击layout 可以进入page_config 里面有很多可用图片🔥™🎉🚀🌌💣✨🌙🎆🎇


st.title("🔧 用户管理系统")
col1,col2,col3=st.columns(3)
with col1:
    with st.container(border=True):
        tab1,tab2 = st.tabs([" 🙆‍♀️ t1","📥 t2"])
        tab2.write("tab2")
        tab1.write("tab1")
     
with col2:
    with st.container(border=True):
        tab1,tab2 = st.tabs([" 🙆‍♀️ t1","📥 t2"])
        tab2.write("tab2")
        tab1.write("tab1")
with col3:
    with st.container(border=True):
        tab1,tab2 = st.tabs([" 🙆‍♀️ t1","📥 t2"])
        tab2.write("tab2")
        tab1.write("tab1")


with st.form('my_form',clear_on_submit=True):
    st.radio(label='🙆‍♀️ part1:', options=[
                        '解决', '未解决', '未完全解决'], horizontal=True,
                        key='value1')

    error_list = ['答非所问', '推荐错误', '推荐不准确', '回答不详细', '信息更新不及时']
    not_saf_reason = st.radio(
        label='🤦‍♀️ part2:', options=error_list, horizontal=True,key='value2')

    submit_button = st.form_submit_button(
                    label='📥 点我提交', on_click=my_callback,use_container_width=True
                    )

   