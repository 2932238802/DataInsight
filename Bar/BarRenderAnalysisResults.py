

import streamlit as st
from common import convert

def BarRenderAnalysisResults():
    """
    BarRenderAnalysisResults:
        渲染函数
    """
    
    st.info("Debug")
    if st.session_state.get('bar_1') is not None and st.session_state.get('bar_2') is not None:
        with st.expander("📈 柱状图", expanded=True):
            col1, col2 = st.columns([5, 1])
            
            with col1:
                
                st.pyplot(st.session_state.bar_1)
                st.pyplot(st.session_state.bar_2)
            
            with col2:
                # ConvertPltToBytes 封装的 二进制函数
                plot_bytes_1 = convert.ConvertPltToBytes(st.session_state.bar_1)
                plot_bytes_2 = convert.ConvertPltToBytes(st.session_state.bar_2)
                
                st.download_button(
                    label="⬇️ 下载图表",
                    data=plot_bytes_1,
                    file_name=f"bar_1.png",
                    mime="image/png",
                    help="下载PNG格式的高清图表",
                    use_container_width=True,
                    key="download_bar_1"
                )
                
                export_format = st.selectbox(
                    "导出格式",
                    ["PNG"],
                    index=0,
                    help="选择图片导出格式",
                    key="selectbox_download_bar_1"
                )
                
                st.download_button(
                    label="⬇️ 下载图表",
                    data=plot_bytes_2,
                    file_name=f"bar_2.png",
                    mime="image/png",
                    help="下载PNG格式的高清图表",
                    use_container_width=True,
                    key="download_bar_2"
                )
                
                export_format = st.selectbox(
                    "导出格式",
                    ["PNG"],
                    index=0,
                    help="选择图片导出格式",
                    key="selectbox_download_bar_2"
                )
        
    