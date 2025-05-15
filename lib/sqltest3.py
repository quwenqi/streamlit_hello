import streamlit as st 
from datetime import datetime
from io import StringIO
 

def my_callback():
    print(f"curdate: {datetime.now()} first: {st.session_state.value1} sec: {st.session_state.value2}")

    
#st.set_page_config(page_title="用户管理系统", layout="wide")
st.set_page_config(page_title="用户管理系统", layout="centered" ,  page_icon=":rocket:", initial_sidebar_state="auto",menu_items={
        "Get Help": "https://example.com/help",
        "About": "Built by [Your Company](https://your-company.com)"
    })
#点击layout 可以进入page_config 里面有很多可用图片🔥™🎉🚀🌌💣✨🌙🎆🎇


st.title("🔧 用户管理系统")
col1,col2,col3 =st.columns(3)
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

 
#文件上传
upload_file=st.file_uploader('上传文件',type=['csv','json','txt'])
if upload_file:
    # st.write(upload_file.getvalue())
    # 读取文件内容
    # st.write(StringIO(upload_file.getvalue().decode('utf-8')).read())
    # st.write(pd.read_csv(upload_file))
    pass
else:
    st.write('您还未上传文件')



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

number=st.slider("粉丝量",value=80,min_value=0,max_value=2000,step=1)
with st.expander("更多信息"):
    st.title("传智教育")
    st.write("黑马程序员")
    st.write("博学谷")


col1_1, col1_2, col1_3 = st.columns(3,border=True,vertical_alignment='bottom')
def my_button1callback():
     
     st.write("博学谷")

with col1_1:
    input1 = st.text_input("请输入文本", "默认文本", key="text_input_1")
    sub_1 = st.button("提交", key="button1", on_click = my_button1callback)
    if sub_1:
        st.write("博学谷")
with col1_2:
    input2 = st.text_input("请输入文本", "默认文本", key="text_input_2")

with col1_3:
    input3 = st.text_input("请输入文本", "默认文本", key="text_input_3")

 



with st.form(key="my_form_sub2"):
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
        submitted_2 = st.form_submit_button("Submit" )

    if submitted_2:
        st.write('Submitted!')


with st.form(key="my_form_sub"):

    st.markdown("""
        <style>
            .stTextInput {
                display: flex;
                align-items: center;
            }
            .stTextInput > label {
                width: 80px;  /* 设置 label 的宽度 */
                font-weight: bold;
                margin-right: 0px;  /* 设置 label 和输入框之间的间距 */
                margin-left: 0px;  /* 设置 label 和输入框之间的间距 */
            }
                
           .stSlider {
                display: flex;
                align-items: center;
            }
            .stSlider > label {
                width: 80px;  /* 设置 label 的宽度 */
                font-weight: bold;
                margin-right: 0px;  /* 设置 label 和输入框之间的间距 */
            }


        </style>
    """, unsafe_allow_html=True)


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
        submitted = st.form_submit_button("Submit")

    if submitted:
        st.write('Submitted!')
