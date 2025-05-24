import streamlit as st
import pandas as pd

def HandleFileUpload():
    uploaded_file = st.file_uploader("上传数据文件 (Excel)", type=["xlsx"])
    if uploaded_file:
        try:
            st.session_state.df = pd.read_excel(uploaded_file)
            st.session_state.update({k: None for k in ['regression_plot', 'X_', 'y_']})
            st.success("✅ 文件上传成功！")
            
        except Exception as e:
            st.error(f"❌ 文件加载失败: {e}")
            st.session_state.df = None