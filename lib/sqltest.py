import streamlit as st
from contextlib import contextmanager
from sqlmodel import SQLModel, Field, Session, create_engine, select, update, delete
from pydantic import BaseModel, EmailStr, conint
import pandas as pd
import importlib.metadata
import re  # 导入正则表达式模块
import time
# 正确获取版本
sqlmodel_version = importlib.metadata.version("sqlmodel")
print(f"SQLModel 版本: {sqlmodel_version}")

 


# -------------------
# 数据库会话管理
# -------------------

# -------------------
# 全局引擎管理
# -------------------
_ENGINE = None
#设置 echo=True 在 create_engine 中可以打印出 SQL 语句，这对于调试很有帮助。在生产环境中，通常将其设置为 False。
def get_engine():
    global _ENGINE
    if _ENGINE is None:
        _ENGINE = create_engine("sqlite:///mydatabase.db", echo=True)
    return _ENGINE


@contextmanager
def get_db_session():
    engine = get_engine()
    session = Session(engine)
    try:
        yield session
        session.commit()
    except Exception as e:
        session.rollback()
        st.error(f"数据库操作失败: {e}")
        raise
    finally:
        session.close()

# 缓存数据库初始化
@st.cache_resource
def init_db():
    print("Initializing database...")
    # 直接使用 SQLModel 的元数据，无需额外配置
    engine = get_engine()

    # create_engine只是建立连接，并不会删除或重新创建整个数据库。现有的数据和表结构会被保留，除非显式地执行了删除操作，
    # 比如调用metadata.drop_all(engine)。

    SQLModel.metadata.create_all(engine)  # 自动处理表结构
    
    if "db_initialized" not in st.session_state:
        st.session_state["db_initialized"] = True
    
# -------------------
# 数据模型与验证
# -------------------
class User(SQLModel, table=True):
    __table_args__ = {"extend_existing": True}  # 允许扩展现有表
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: EmailStr
    age: int
class UserForm(BaseModel):
    name: str
    email: EmailStr
    age: int
# 显示数据库内容
def show_database_content():
    with get_db_session() as session:
        users = session.exec(select(User)).all()
        if not users:
            st.warning("数据库中暂无用户数据")
            return

        df = pd.DataFrame([user.model_dump() for user in users])
        st.subheader("数据库内容")
        st.dataframe(df)
# -------------------
# Streamlit 应用
# -------------------
def main():
    st.set_page_config(page_title="用户管理系统", layout="wide")
    st.title("🔧 用户管理系统")

    # 初始化数据库（仅首次运行）
    if "db_initialized" not in st.session_state:
        with st.spinner("初始化数据库..."):
            init_db()
        st.session_state["db_initialized"] = True

    # 侧边栏导航
    menu_index = st.sidebar.radio(
        "选择功能",
        ["用户列表", "添加用户", "编辑用户", "删除用户","显示数据库内容","test"]
    )

    # 根据选择渲染页面
    if menu_index == "用户列表":
        show_users()
    elif menu_index == "添加用户":
        add_user()
    elif menu_index == "编辑用户":
        edit_user()
    elif menu_index == "删除用户":
        delete_user()
    elif menu_index == "显示数据库内容":  # 添加对应的功能调用
        show_database_content()

    elif menu_index == "test":  # 添加对应的功能调用
        add_user_test()
# -------------------

# -------------------
# 显示用户列表
# -------------------
def show_users():
    with get_db_session() as session:
        users = session.exec(select(User)).all()
        if not users:
            st.warning("暂无用户数据")
            return

        df = pd.DataFrame([user.model_dump() for user in users])
        editable_df = st.data_editor(df, hide_index=True)
        
        # 批量更新逻辑
        modified_users = []
        for index, row in editable_df.iterrows():
            user = session.get(User, row["id"])
            if user and any([
                user.name != row["name"],
                user.email != row["email"],
                user.age != row["age"]
            ]):
                user.name = row["name"]
                user.email = row["email"]
                user.age = row["age"]
                modified_users.append(user)
        
        if modified_users:
            session.add_all(modified_users)
            st.success(f"已更新 {len(modified_users)} 条记录")

# -------------------
# 添加用户
# -------------------
def add_user():
    with get_db_session() as session:

        # 初始化 session_state
        if "name" not in st.session_state:
            st.session_state.name = ""
        if "email" not in st.session_state:
            st.session_state.email = ""
        if "age" not in st.session_state:
            st.session_state.age = None


        with st.form("add_user"):
            print(f"st.session_state.name{st.session_state.name}")
            name = st.text_input("姓名",value=st.session_state.name)
            email = st.text_input("邮箱",value=st.session_state.email)
            age  = st.number_input("年龄", min_value=1, max_value=150)

            submit_button = st.form_submit_button("提交",use_container_width=True)
            clear_button = st.form_submit_button('清除',use_container_width=True)

            if submit_button:
                if name and email and age:
                    # 验证邮箱格式
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
                        st.error("邮箱格式不正确！")
                        return  # 阻止后续代码执行
                    form_data = UserForm(
                        name = name,
                        email = email,
                        age  = age
                    )
                else :
                    st.error("请填写所有字段")
                    st.rerun()   

                print("提交表单数据:")
                try:
                    new_user = User(**form_data.model_dump())
                    print("新用户数据:", new_user)
                    session.add(new_user)
                    st.success(f"用户 {new_user.name} 添加成功！")

            
                    with st.spinner("添加成功"):
                         time.sleep(1)
                    #st.rerun()
                except ValueError as e:
                    st.error(f"输入无效: {e}")

            if clear_button:
                print("clear_button:")
                 # 清除输入框
                st.session_state.name = ""
                st.session_state.email = ""
                st.session_state.age = None
                st.success(f"用户 清除成功！")
                with st.spinner("清除成功！..."):
                    time.sleep(1)
                st.rerun()
                

# -------------------
# 添加用户
# -------------------
def add_user_test():
        # 初始化 session_state
    if "name" not in st.session_state:
        st.session_state.name = ""
    if "email" not in st.session_state:
        st.session_state.email = ""
    if "age" not in st.session_state:
        st.session_state.age = None

    with st.form("add_user",clear_on_submit=True):
        name = st.text_input("姓名",value=st.session_state.name)
        email = st.text_input("邮箱",value=st.session_state.email)
        age  = st.number_input("年龄", min_value=1, max_value=150)
        submit_button = st.form_submit_button("提交",use_container_width=True)
        clear_button = st.form_submit_button('清除',use_container_width=True)
        if submit_button:
            print("提交表单数据:")

        if clear_button:
            st.session_state.name = ""
            st.session_state.email = ""
            st.session_state.age = None
            st.rerun()  # 重新加载页面以清空表单
# -------------------
# 编辑用户
# -------------------
def edit_user():
    with get_db_session() as session:
        users = session.exec(select(User)).all()
        if not users:
            st.warning("暂无用户可编辑")
            return
        
        user_id = st.selectbox("选择用户", [u.id for u in users], format_func=lambda x: f"ID {x}")
        user = session.get(User, user_id)
        
        if not user:
            st.error("用户不存在")
            return

        with st.form("edit_user"):
            form_data = UserForm(
                name=st.text_input("姓名", value=user.name),
                email=st.text_input("邮箱", value=user.email),
                age=st.number_input("年龄", min_value=1, max_value=150, value=user.age)
            )
            
            if st.form_submit_button("更新"):
                try:
                    user.name = form_data.name
                    user.email = form_data.email
                    user.age = form_data.age
                    st.success("用户信息更新成功")
                    st.rerun()
                except ValueError as e:
                    st.error(f"输入无效: {e}")

# -------------------
# 删除用户
# -------------------
def delete_user():
    with get_db_session() as session:
        users = session.exec(select(User)).all()
        if not users:
            st.warning("暂无用户可删除")
            return
        
        user_id = st.selectbox("选择要删除的用户", [u.id for u in users], format_func=lambda x: f"ID {x}")
        if not user_id:
            st.write("请选择用户")
            return
        
        if st.button("确认删除", use_container_width=True):
            user = session.get(User, user_id)
            if user:
                session.delete(user)
                st.success("用户删除成功")
                st.rerun()
            else:
                st.error("用户不存在")

if __name__ == "__main__":
    main()