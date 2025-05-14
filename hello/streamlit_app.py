# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022-2024)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from pathlib import Path
import streamlit as st
import os
from streamlit.runtime.scriptrunner import get_script_run_ctx



if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

dir_path = Path(__file__).parent
print("=======")
print(dir_path)



ctx = get_script_run_ctx()
print(ctx)
ctx_main_script = ""
if ctx: 
    ctx_main_script = ctx.main_script_path
    print(f"ctx_main_script=={ctx_main_script}")

# 获取页面路径（假设 page 是从外部传入的）
page = "./"

main_script_path = os.path.join(os.getcwd(), ctx_main_script)
main_script_directory = os.path.dirname(main_script_path)
print(f"main_script_directory=={main_script_directory}")
 
 # Convenience for handling ./ notation and ensure leading / doesn't refer to root directory
page = os.path.normpath(page.strip("/"))
 
 # Build full path
requested_page = os.path.join(main_script_directory, page)
print(f"requested_page=={requested_page}")

dir_path = main_script_directory
print("=======")
print(os.path.join(dir_path,"log_out.py"))




if st.session_state.logged_in:
    pagelist = {
        "❤️ Home account":
        [
            st.Page(os.path.join(dir_path/"log_out.py"),        icon=":material/logout:"),
            st.Page(os.path.join(dir_path/"Hello.py"),          icon=":material/favorite:"),
            st.Page(os.path.join(dir_path/"Animation_Demo.py"), icon=":material/wifi_home:"),
            st.Page(os.path.join(dir_path/"Plotting_Demo.py"),  icon=":material/favorite:"),
            st.Page(os.path.join(dir_path/"Mapping_Demo.py"),   icon=":material/favorite:"),
            st.Page(os.path.join(dir_path/"Dataframe_Demo.py"), icon=":material/favorite:"),
        ],
        "🔥 Your account":
        [
            st.Page(os.path.join(dir_path,"Hello2.py"),          icon=":material/favorite:"),
        ],
    }
else:
    pagelist = {
            "🔥 Log in":
            [
                st.Page(os.path.join(dir_path,"log_in.py"),     icon=":material/login:"),
            ],
        }
def run():
        page = st.navigation(pagelist,position="sidehbar")
        page.run()
  

if __name__ == "__main__":
    run()
