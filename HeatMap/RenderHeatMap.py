from HeatMap.HeatMapAnalysis import HeatMapAnalysis
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
from common import pltconfig
import seaborn as sns

def RenderHeatMap(numerical_cols):

    hmcol_width, hmcol_height = st.columns(2)
    
    with hmcol_width:
        st.session_state.hmcol_width = st.selectbox(
            " ✍️ 选择图像宽度(10 较为合适英寸)",
            pltconfig.PLTWIDTH,
            index = 5 if len(pltconfig.PLTWIDTH) > 5 else len(pltconfig.PLTWIDTH) - 1,
            key = "hm_width",
            help = "绘制图案的宽"
        )
        
    with hmcol_height:
        st.session_state.hmcol_height = st.selectbox(
            " 🦘 选择图像高度(6 较为合适英寸)",
            pltconfig.PLTHEIGHT,
            index = 2 if len(pltconfig.PLTHEIGHT) > 2 else len(pltconfig.PLTHEIGHT) - 1,
            key = "hm_height",
            help = "绘制图案的高"
        )
        
    annot, cmap = st.columns(2)
    with annot:
        annot_is = st.radio(
            " 🐿️ 是否显示数值",
            ["是","否"],
            index=0,
            key="hm_annot"
        )
        if annot_is == "是":
            st.session_state.hmannot = True
        else:
            st.session_state.hmannot = False
            
    with cmap:
        st.session_state.hmcmap = st.selectbox(
            " 🪢 选择颜色条样式",
            list(pltconfig.CMAP_DICT.keys()),
            index=0,
            key = "hm_cmap",
            help="颜色条样式"
        ) 
    
    
    # 颜色映射的中间段
    # linewidths 单元格之间的距离
    center, linewidths = st.columns(2)
    with center:
        set_center = st.checkbox(" 🧞‍♂️ 设置颜色映射中心点?", key="hm_set_center")
        if set_center:
            st.session_state.hmcenter = st.number_input(
                "中心点值 (例如 0)",
                value=0.0,
                step=0.1,
                help="指定颜色映射的中心。对于发散型颜色图（如 coolwarm, RdBu_r），此值对应于中间颜色。",
                key="hm_center" 
            )
        else:
            st.session_state.hmcenter = None
    
    with linewidths:
        st.session_state.hmlinewidths = st.number_input(
            " 😻 请输入线条宽度",
            min_value=0.0,
            max_value=1.0,
            step = 0.1,
            key = "hm_linewidths",
            help="图形之间的线条宽度"
        )
    
    linecolor, cbar_kws = st.columns(2)
    
    with linecolor:
        st.session_state.hmlinecolor = st.selectbox(
            " 👻 选择线条颜色样式",
            pltconfig.COLOR,
            index=0,
            key = "hm_linecolor",
            help="线条颜色样式"
        ) 
        
    if st.button(" 🫏 开始渲染", key="run_heatmap"):
        PerformHeatmap()

def PerformHeatmap():
    try:
        width = st.session_state.hmcol_width
        height = st.session_state.hmcol_height
        annot = st.session_state.hmannot
        cmap = pltconfig.CMAP_DICT[st.session_state.hmcmap]
        center = st.session_state.hmcenter
        linewidths = st.session_state.hmlinewidths
        linecolor = st.session_state.hmlinecolor
        
        # 获取数据
        df = st.session_state.df
        
        if df is None:
            st.error("未找到数据，请确保已上传或选择数据。")
            return
        
        # 选择数值型列
        numeric_df = df.select_dtypes(include=[np.number])
        
        if numeric_df.empty:
            st.error("选择的数据集中不包含数值型数据，无法绘制热力图。")
            return
        
        # 处理缺失值（例如，用平均值填充）
        numeric_df = numeric_df.fillna(numeric_df.mean())
        
        # 绘制热力图
        fig = HeatMapAnalysis.DrawHM(
            df = numeric_df,  # 确保传递的是数值型数据
            width = width,
            height = height,
            annot = annot,
            cmap = cmap,
            center = center,
            linewidths = linewidths,
            linecolor = linecolor
        )
        
        st.session_state.hm = fig
        
        st.success("渲染完成")
        
    except Exception as e:
        st.error(f"绘制热力图时发生错误: {e}")
