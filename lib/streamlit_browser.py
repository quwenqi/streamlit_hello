import streamlit as st
from streamlit_file_browser import st_file_browser
import os

# 设置页面标题
st.title('本地文件浏览器与修改ddd')

# 指定要浏览的本地目录路径
path = os.path.join(os.getcwd(), "123")

st.write("选择的文件:", path)
# 使用文件浏览器组件
event = st_file_browser(path, 
                        use_static_file_server=False,

                        artifacts_site="http://localhost:8502/down",
                        artifacts_download_site="http://localhost:8502/down/",

                        show_delete_file=True,
                        show_choose_file=True,
                        show_choose_folder=True,
                        show_download_file=True,
                        show_new_folder=True,
                        show_upload_file=True,
                        show_rename_file=True,
                        show_rename_folder=True,
                        static_file_server_path="http://localhost:8502/down",
                        key='A')

# 显示选择的文件信息
if event is not None:
    st.write("选择的文件:", event)

# 如果选择了文件且允许修改文件
    if event and event.get("type") == "SELECT_FILE":
        file_path = event.get("target")
        file_path=file_path.get("path")
       
        st.write("文件路径x:", file_path)
        file_path = path+"/"+file_path
        # 显示文件内容（仅示例，根据文件类型调整）
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
 

            # 允许用户修改文件内容
            new_content = st.text_area("修改文件内容", value=file_content)
            if st.button("保存修改"):
                with open(file_path, 'w') as file:
                    file.write(new_content)
                st.success("文件已修改并保存!")

        except Exception as e:
            st.error("读取文件出错: " + str(e))