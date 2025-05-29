import streamlit as st
import logging
import time

def log_dis():
    # 确保 st.session_state 中有 'log' 属性
    if "log" not in st.session_state:
        st.session_state.log = ""

    # 配置日志
    root_logger = logging.getLogger()
    if not root_logger.hasHandlers():
        class StreamlitHandler(logging.Handler):
            def emit(self, record):
                st.session_state.log += self.format(record) + "\n"

        streamlit_handler = StreamlitHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        streamlit_handler.setFormatter(formatter)
        root_logger.addHandler(streamlit_handler)
        root_logger.setLevel(logging.DEBUG)

    st.title("日志显示示例")

    # 创建两个列，用于放置按钮
    col1, col2 = st.columns(2)
    with col1:
        if st.button("记录日志"):
            logging.info("这是一个信息日志1。")

    with col2:
        if st.button("清除日志"):
            st.session_state.log = ""

    # 使用 st.text_area 显示日志
    st.text_area("日志", st.session_state.log, height=200)

if __name__ == "__main__":
    log_dis()