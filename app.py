import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


import default.InitSessionState
from RenderSidebarUnit import RenderSidebar
from LinearRegression import LrRenderAnalysisResults
from HeatMap import HmRenderAnalysisResults
from Radar import RaRenderAnalysis
from Pie import PieRenderAnalysis

from LearningIndex import LearningIndex

def main():
    st.set_page_config(page_title="DataInsight", layout="wide")
    default.InitSessionState.InitSessionState()
    RenderSidebar.RenderSidebar()
    st.title("📊 DataInsight")

    if st.session_state.df is not None:
        # 创建标签页
        tabs = st.tabs(["数据展示", "知识学习"])

        # 主页标签页内容
        with tabs[0]:
            RenderDataPreview()
            Results()

        # 第二页标签页内容
        with tabs[1]:
            LearningIndex.LearningIndex()

    else:
        st.info(
            """
            ## 欢迎来到 DataInsight
            - 该平台是一个收费,在线数模pyplot图生成平台
            - 联系电话:19857198709
            - ©lsj&yxy
            ---
            """
        )

def RenderDataPreview():
    with st.expander("🔍 数据概览", expanded=True):
        col1, col2 = st.columns([1, 2])
        with col1:
            st.markdown(f"""
            ### 数据集信息
            - 总行数: `{len(st.session_state.df)}`
            - 总列数: `{len(st.session_state.df.columns)}`
            - 数值型列: `{len(st.session_state.df.select_dtypes(include=np.number).columns)}`
            """)
        with col2:
            st.dataframe(st.session_state.df.head(8), use_container_width=True)
    st.markdown("---")

def Results():
    if "regression_plot" in st.session_state and st.session_state.regression_plot is not None:
        LrRenderAnalysisResults.LRRenderAnalysisResults()
        st.info("👈 请在左侧输入预测值,显示预测分析图", icon="ℹ️")
        if st.session_state.regression_plot_predict is not None:
            LrRenderAnalysisResults.LRRenderAnalysisResultsPredict()
        
    # 热力图
    elif "hm" in st.session_state and st.session_state.hm is not None:
        HmRenderAnalysisResults.HmRenderAnalysisResults()
        
    # 雷达图
    elif "ra" in st.session_state and st.session_state.ra is not None:
        RaRenderAnalysis.RaRenderAnalysis()
        
    elif "pie" in st.session_state and st.session_state.pie is not None:
        PieRenderAnalysis.PieRenderAnalysis()
        
    else:
        st.info("👈 请在左侧输入预测值,显示预测分析图", icon="ℹ️")


if __name__ == "__main__":
    main()
