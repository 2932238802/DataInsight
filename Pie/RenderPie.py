
import streamlit as st
import pandas as pd
def RenderPie():
    
    df = st.session_state.df
    for row_index_label in df.index:
        for col_name in df.columns:
            value = df.loc[row_index_label, col_name]
            reason = "无"
            is_empty = False
            if pd.isna(value):
                is_empty = True
                reason = "NaN/None"
            elif isinstance(value, str) and value.strip() == "":
                is_empty = True
                reason = "空或纯空格字符串"
            if is_empty:
                row_num = df.index.get_loc(row_index_label) + 1
                col_num = df.columns.get_loc(col_name) + 1
                st.error(
                    f"该表格存在空缺位置!\n"
                    f"位置: 行 '{row_index_label}' (第 {row_num} 行), "
                    f"列 '{col_name}' (第 {col_num} 列)。\n"
                    f"原因: {reason} (原始值: '{value}')"
                )
                return False
            
    labels,sizes = st.columns(2)
    with labels:
        st.session_state.pielabels = st.selectbox(
            label = "选择对应的标签列",
            options= df.columns,
            index=0,
            key = "pie_labels",
        )
    
    with sizes:
        st.session_state.pielabels = st.selectbox(
            label = "选择对应的数据列",
            options= df.columns,
            index=0,
            key = "pie_sizes",
        )