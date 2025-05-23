import streamlit as st
from st_aggrid import AgGrid, GridOptionsBuilder ,DataReturnMode ,GridUpdateMode
import pandas as pd
 




# 定义单行选择表，选中行的数据，可以按字段/关键字读取出来
def aggrid(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    selection_mode = 'single' # 定义单选模式，多选为'multiple'
    enable_enterprise_modules = True # 设置企业化模型，可以筛选等
    gb.configure_default_column(editable=True) #定义允许编辑
    
    return_mode_value = DataReturnMode.FILTERED  #__members__[return_mode]
    gb.configure_selection(selection_mode, use_checkbox=True) # 定义use_checkbox
    
    gb.configure_side_bar()
    gb.configure_grid_options(domLayout='normal')
    gb.configure_pagination(paginationAutoPageSize=True)
    gridOptions = gb.build()
    
    update_mode_value = GridUpdateMode.MODEL_CHANGED|GridUpdateMode.MANUAL #__members__[update_mode]
    
    grid_response = AgGrid(
                        df, 
                        gridOptions=gridOptions,
                        data_return_mode=return_mode_value,
                        update_mode=update_mode_value,
                        enable_enterprise_modules=enable_enterprise_modules,
                        )  
    df = grid_response['data']
    selected = grid_response['selected_rows']
    
    return df, selected  


# 读取数据
df = pd.read_csv('./airline-safety.csv')
df, selected  =aggrid(df)

# 显示更新后的数据
st.write("更新后的数据:")
st.dataframe(df)


# 显示更新后的数据
st.write("选中:")
st.dataframe(selected)