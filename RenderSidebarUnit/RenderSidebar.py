import streamlit as st

from RenderSidebarUnit.HandleFileUpload import HandleFileUpload
from RenderSidebarUnit.RenderAnalysis import RenderAnalysis

# 简单的样式
def RenderSidebar():
    with st.sidebar:
        st.title(" 🐦 控制面板")
        HandleFileUpload()
        RenderAnalysis()
            