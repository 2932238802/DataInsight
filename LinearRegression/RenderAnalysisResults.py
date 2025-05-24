
import streamlit as st
import matplotlib.pyplot as plt
from common import convert

# 图案显示
# 线性预测
# 线性预测
def LRRenderAnalysisResults():
    if st.session_state.get('regression_plot') is not None: 
        with st.expander("📈 回归分析结果", expanded=True):
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.pyplot(st.session_state.regression_plot)
            
            with col2:
                plot_bytes = convert.convert_plt_to_bytes(st.session_state.regression_plot)
                
                st.download_button(
                    label="⬇️ 下载图表",
                    data=plot_bytes,
                    file_name=f"regression_{st.session_state.X_}_vs_{st.session_state.y_}.png",
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

# 分析预测结果
def LRRenderAnalysisResultsPredict():
    if st.session_state.get('regression_plot_predict') is not None: 
        with st.expander("📈 预测分析结果", expanded=True):
            col1, col2 = st.columns([5, 1])
            
            with col1:
                st.pyplot(st.session_state.regression_plot_predict)
            
            with col2:
                plot_bytes = convert.convert_plt_to_bytes(st.session_state.regression_plot_predict)
                
                st.download_button(
                    label="⬇️ 下载图表",
                    data=plot_bytes,
                    file_name=f"regression_{st.session_state.X_}_vs_{st.session_state.y_}_predict.png",
                    mime="image/png",
                    help="下载PNG预测图格式的高清图表",
                    use_container_width=True,
                    key="download_regression_plot_predict"
                )
                
                export_format = st.selectbox(
                    "导出格式",
                    ["PNG"],
                    index=0,
                    help="选择图片导出格式",
                    key="selectbox_download_plot_predict"
                )
                
                