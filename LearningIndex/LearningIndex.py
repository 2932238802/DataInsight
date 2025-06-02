import streamlit as st
from LearningIndex import common

def LearningIndex():
    with st.expander("numpy", expanded=False):
        st.info("TODO")
        
    with st.expander("streamlit", expanded=False):
        st_read_md_title = "md 读取MD文件"
        st_end = "end"
        
        st_read_md_tab, end = st.tabs(
            [
            st_read_md_title,
            st_end
            ]                     
        )

        with st_read_md_tab:
            st.subheader(st_read_md_title)
            st.markdown(GetMd("st_read_md"), unsafe_allow_html=True)
        
        with end:
            st.info("end")

    with st.expander("matplotlib.pyplot",expanded=False):
        pass
    
    with st.expander("python",expanded=False):
        random_uniform = "随机生成区间内的浮点数"
        py_end = "end"
        
        random_uniform_tab,py_end_tab = st.tabs(
            [random_uniform,py_end]
        )
        
        with random_uniform_tab:
            st.subheader(random_uniform)
            st.markdown(GetMd("random_uniform"),unsafe_allow_html=True)
        
        with py_end_tab:
            st.info("end")

def GetMd(ps:str):
    with open(common.Path[f'{ps}'],"r",encoding="utf-8") as file:
        md_text = file.read()
        return md_text