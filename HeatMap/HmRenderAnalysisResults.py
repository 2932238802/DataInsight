import streamlit as st
from common import convert

# 图案显示
# 线性预测
# 线性预测
def HmRenderAnalysisResults():
    
    if st.session_state.get('hm') is not None:
        with st.expander("📈 热力图", expanded=True):
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.pyplot(st.session_state.hm)
            
            with col2:
                plot_bytes = convert.ConvertPltToBytes(st.session_state.hm)
                
                st.download_button(
                    label="⬇️ 下载图表",
                    data=plot_bytes,
                    file_name=f"heatmap.png",
                    mime="image/png",
                    help="下载PNG格式的高清图表",
                    use_container_width=True,
                    key="download_heatmap"
                )
                
                export_format = st.selectbox(
                    "导出格式",
                    ["PNG"],
                    index=0,
                    help="选择图片导出格式",
                    key="selectbox_download_heatmap"
                )
        
    