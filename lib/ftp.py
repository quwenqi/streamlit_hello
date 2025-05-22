import streamlit as st
import os
import ftplib
from ftplib import error_perm
from ftpdown import myFtp
st.markdown("""
    <style>
    .stProgress > div > div > div > div {
        background-image:linear-gradient(to right, #99ff99, #00ccff);
    }
    </style>
""", unsafe_allow_html=True)


def progress(percent):
    bar.progress(percent)


c1, c2 = st.columns(2)
with c1:
    ftp_host = st.text_input("请输入FTP服务器IP", value="192.168.1.3")
    ftp_port = st.number_input("请输入服务器端口号", value=21)
with c2:
    ftp_username = st.text_input("请输入FTP用户名", value="ftpuser2")
    ftp_password = st.text_input("请输入FTP用户密码", value="qu123456")

if len(ftp_host) > 0 and ftp_port > 0 and len(ftp_username) > 0 and len(ftp_password) > 0:
    try:
        ftp = myFtp(ftp_host, int(ftp_port))
        ftp.Login(ftp_username, ftp_password)

        with st.expander("查看FTP服务器上文件信息"):
            st.write(ftp.GetList())

        with st.form("FTP下载"):
            file_wait_download = st.multiselect("请选择要下载的文件", ftp.GetList())
            local_save_path = st.text_input("请输入本地用来保存下载文件的文件夹路径", value="/home/qu/ftpx")
            submitted = st.form_submit_button("点我开始下载文件")
            if submitted:
                rootpath=ftp.GetPwd()
                #st.write("当前目录:", rootpath)
                bar = st.progress(0)
                for x in range(len(file_wait_download)):
                    #st.write("file_wait_download:", file_wait_download[x])
                    
                    ftp.DownLoadFileTree(local_save_path+"/"+file_wait_download[x],rootpath +"/" + file_wait_download[x])  # 从目标目录下载到本地目录d盘
                    progress(100)

        ftp.Close()
    except error_perm as e:
        st.error(f"发生错误: {e}")
        st.error("连接FTP失败，请检查输入信息是否正确！")
else:
    st.warning("您还有FTP服务器的连接信息没有完整填写！")

    '''
    sudo useradd -m ftpuser2
    sudo passwd qu123456

    配置完成后,可以通过以下命令启动vsftpd服务:
    sudo systemctl start vsftpd

    检查服务状态：
    sudo systemctl status vsftpd

    ftp:192.168.1.3

    sudo systemctl restart vsftpd

    '''
