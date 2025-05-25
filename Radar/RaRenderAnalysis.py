
import streamlit as st
from common import convert

def RaRenderAnalysis():
    if st.session_state.get('Ra') is not None: 
        with st.expander("📈 雷达图", expanded=True):
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.pyplot(st.session_state.ra)
            with col2:
                plot_bytes = convert.ConvertPltToBytes(st.session_state.Ra)
                
                st.download_button(
                    label="⬇️ 下载图表",
                    data=plot_bytes,
                    file_name=f"{st.session_state.ra_title_name}.png",
                    mime="image/png",
                    help="下载PNG格式的高清图表",
                    use_container_width=True,
                    key="download_regression_plot"
                )
                
                export_format = st.selectbox(
                    "导出格式",
                    ["PNG"],
                    index=0,
                    help="选择图片导出格式",
                    key="selectbox_download_plot"
                )