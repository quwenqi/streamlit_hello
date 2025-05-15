import streamlit as st

def clear_text():
    st.session_state["text"] = ""

input = st.text_input("text", key="text")    
st.button("clear text input", on_click=clear_text)
#st.write(input)