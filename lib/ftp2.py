import streamlit as st
 
import ftplib
from ftplib import error_perm
from streamlit_tree_select import tree_select

st.set_page_config(page_title="网页版FTP客户端", layout="wide", page_icon="📂")

st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-image:linear-gradient(to right, #99ff99, #00ccff);
    }
    </style>
""", unsafe_allow_html=True)

def progress(percent):
    bar.progress(percent)

 
choose1 = st.button("连接服务器", key="choose1", use_container_width=True)
choose2 = st.button("下载文件", key="choose2", use_container_width=True)
choose3 = st.button("上传文件", key="choose3", use_container_width=True)

if choose1:
    c1, c2 = st.columns(2)
    with c1:
        ftp_host = st.text_input("请输入FTP服务器IP",value="192.168.1.3")
        ftp_port = st.number_input("请输入服务器端口号",value=21)
    with c2:
        ftp_username = st.text_input("请输入FTP用户名",value="ftpuser2")
        ftp_password = st.text_input("请输入FTP用户密码", type="password",value="qu123456")

    ftp = ftplib.FTP(timeout=30)

    try:
        if len(ftp_host)>0 and len(str(ftp_port))>0 and len(ftp_username)>0 and len(ftp_password)>0:
            ftp.connect(ftp_host, int(ftp_port))
            ftp.login(ftp_username, ftp_password)
            if ftp.getwelcome().startswith("220"):
                st.success("连接FTP服务器成功！")

                if 'ftp_host' not in st.session_state:
                    st.session_state.ftp_host = ftp_host
                if 'ftp_port' not in st.session_state:
                    st.session_state.ftp_port = int(ftp_port)
                if 'ftp_username' not in st.session_state:
                    st.session_state.ftp_username = ftp_username
                if 'ftp_password' not in st.session_state:
                    st.session_state.ftp_password = ftp_password

                #ftp.cwd("FTP")
                with st.expander("查看FTP服务器上文件信息"):
                    st.write(ftp.nlst())
        else:
            st.error("连接FTP失败，请检查输入信息是否正确！")
    except error_perm:
        st.error("连接FTP失败，请检查输入信息是否正确！")

elif choose2:

    ftp = ftplib.FTP(timeout=30)

    if 'ftp_host' not in st.session_state:
        st.warning("您还没有连接FTP服务器，请先切换到【连接FTP服务器】选项卡，成功登录FTP服务器后再使用本页面功能！")
    else:
        ftp.connect(st.session_state.ftp_host, int(st.session_state.ftp_port))
        ftp.login(st.session_state.ftp_username, st.session_state.ftp_password)

        #ftp.cwd("FTP")

        empty_list = []
        for x in range(len(ftp.nlst())):
            empty_list.append({"label": ftp.nlst()[x], "value": ftp.nlst()[x]})
        nodes = [
            {
            "label": "待下载的文件",
            "value": "待下载的文件",
            "children": empty_list}
        ]
        return_select = tree_select(nodes)["checked"]

        with st.form("FTP下载"):
            local_save_path = st.text_input("请输入本地用来保存下载文件的文件夹路径")
            submitted = st.form_submit_button("点我开始下载文件")
            if submitted:
                bar = st.progress(0)
                if len(return_select) > 0:
                    if len(local_save_path) > 0:
                        for y in range(len(return_select)):
                            with open(local_save_path + "\\" + str(return_select[y]), "wb") as fp:
                                ftp.retrbinary("RETR " + str(return_select[y]), fp.write)
                        progress(100)
                        st.success("下载完成！")
        ftp.quit()

elif choose3:
    if 'ftp_host' not in st.session_state:
        st.warning("您还没有连接FTP服务器，请先切换到【连接FTP服务器】选项卡，成功登录FTP服务器后再使用本页面功能！")
    else:
        file = st.file_uploader("请选择要上传的文件", accept_multiple_files=True)
        if file is not None:
            if len(file) > 0:
                file_name_list = []
                for m in range(len(file)):
                    file_name_list.append(file[m].name)
                with st.expander("点击查看待上传的文件列表"):
                    st.write(file_name_list)

                ftp = ftplib.FTP(timeout=30)
                ftp.connect(st.session_state.ftp_host, int(st.session_state.ftp_port))
                ftp.login(st.session_state.ftp_username, st.session_state.ftp_password)

                if ftp.getwelcome().startswith("220"):
                    st.success("连接FTP服务器成功！")
                    #ftp.cwd("FTP")
                    with st.form("FTP上传"):
                        submitted = st.form_submit_button("点我开始上传文件")
                        if submitted:
                            bar = st.progress(0)
                            if len(file_name_list) > 0:
                                for x in range(len(file_name_list)):
                                    ftp.storbinary("STOR " + str(file_name_list[x]), file[x], blocksize=8192)
                                progress(100)
                                st.success("上传完成！")
                                with st.expander("点击查看上传成功的文件列表"):
                                    st.write(ftp.nlst())
                ftp.quit()