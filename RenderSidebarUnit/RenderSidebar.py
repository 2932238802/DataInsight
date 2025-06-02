import streamlit as st

from RenderSidebarUnit.HandleFileUpload import HandleFileUpload
from RenderSidebarUnit.RenderAnalysis import RenderAnalysis

# 简单的样式
def RenderSidebar():
    with st.sidebar:
        st.title(" 🐦工作台🐦 ")
        HandleFileUpload()
        RenderAnalysis()