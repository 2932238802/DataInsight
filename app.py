#!/usr/bin/env python3
#coding: utf-8

# -----------------------------------------------------------------------------
# Copyright (c) 2025，5 [LosAngelous]
# 作者: LosAngelous
# 团队 Lsj & Yxy 
# -----------------------------------------------------------------------------




# -----------------------------------------------------------------------------
# 内置库的设置
# -----------------------------------------------------------------------------
# 库
import numpy as np
import streamlit as st
from pyngrok import conf
import os
from dotenv import load_dotenv 

# 设置开始界面 
# DataInsight 这个是项目名字
# 宽屏布局
st.set_page_config(page_title="DataInsight", layout="wide")

# 库 自定义库
import default.InitSessionState
from RenderSidebarUnit import RenderSidebar
from LinearRegression import LrRenderAnalysisResults
from HeatMap import HmRenderAnalysisResults
from Radar import RaRenderAnalysis
from Pie import PieRenderAnalysis
from Bar import BarRenderAnalysisResults
from About import RenderAbout
from Ngrok import RenderNgrok
from LearningIndex import LearningIndex


# -----------------------------------------------------------------------------
# 这里是读取本地的 env 文件token 这样便于 启动 ngrok
# 当然了 这是我自己的 token 你可以访问我的github去了解一下
# -----------------------------------------------------------------------------
load_dotenv()
NGROK_AUTHTOKEN_FROM_ENV = os.getenv("NGROK_AUTHTOKEN")
if NGROK_AUTHTOKEN_FROM_ENV:
    conf.get_default().auth_token = NGROK_AUTHTOKEN_FROM_ENV
    print("Ngrok Authtoken loaded from .env file")
else:
    print("Warning: NGROK_AUTHTOKEN not found in .env file or environment variables Ngrok might have limitations")
    








# -----------------------------------------------------------------------------
# 项目主要入口
# -----------------------------------------------------------------------------
def main():
    default.InitSessionState.InitSessionState()
    RenderSidebar.RenderSidebar()
    st.title("📊 DataInsight")

    if st.session_state.df is not None:
        # 创建标签页
        tabs = st.tabs(["数据展示", "知识学习","共享网址"])

        with tabs[0]:
            RenderDataPreview()
            Results()

        with tabs[1]:
            LearningIndex.LearningIndex()
            
        with tabs[2]:
            RenderNgrok.RenderNgrok()
            
    RenderAbout.RenderAbout()



# -----------------------------------------------------------------------------
# 初步项目展示
# -----------------------------------------------------------------------------
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




# -----------------------------------------------------------------------------
# 因为这是第一版本 所以有点丑陋 不过问题不大 TODO: 二版修改 if elif 
# -----------------------------------------------------------------------------
def Results():
    if "regression_plot" in st.session_state and st.session_state.regression_plot is not None:
        LrRenderAnalysisResults.LRRenderAnalysisResults()
        st.info("👈 请在左侧输入预测值,显示预测分析图", icon="ℹ️")
        if st.session_state.regression_plot_predict is not None:
            LrRenderAnalysisResults.LRRenderAnalysisResultsPredict()
    elif "hm" in st.session_state and st.session_state.hm is not None:
        HmRenderAnalysisResults.HmRenderAnalysisResults()
    elif "ra" in st.session_state and st.session_state.ra is not None:
        RaRenderAnalysis.RaRenderAnalysis()
    elif "pie" in st.session_state and st.session_state.pie is not None:
        PieRenderAnalysis.PieRenderAnalysis()
    elif st.session_state.bar_1 is not None and st.session_state.bar_2 is not None:
        BarRenderAnalysisResults.BarRenderAnalysisResults()
    else:
        st.info("👈 请在左侧输入预测值,显示预测分析图", icon="ℹ️")





if __name__ == "__main__":
    main()
