import streamlit as st
from LearningIndex import common


def LearningIndex():
    # numpy 
    with st.expander("numpy", expanded=False):
        st.info("TODO")
        
        
    # streamlit
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
    
    

def GetMd(ps:str):
    with open(common.Path[f'{ps}'],"r",encoding="utf-8") as file:
        md_text = file.read()
        return md_text