import streamlit as st
import numpy as np

from LinearRegression.RenderLinearRegression import RenderLinearRegression
from HeatMap.RenderHeatMap import RenderHeatMap
from Radar.RenderRadar import RenderRadar
from Pie.RenderPie import RenderPie
from Bar.RenderBar import RenderBar
from SA.RenderSA import RenderSA
import default.InitSessionState


def TurnNone():
    """当图表类型改变时，重置相关的 session_state 变量。"""
    keys_to_reset = [
        'regression_plot',
        'regression_plot_predict',
        'pie',
        'ra',
        'hm',
    ]
    
    for key in keys_to_reset:
        if key in st.session_state:
            st.session_state[key] = None
            
    st.info("图表类型已更改，相关分析结果已重置") 

            
def RenderAnalysis():
    
    df = st.session_state.get('df', None)
    
    # 获取数据
    # 返回列表
    # numerical_cols 包含只有数据
    if df is None or df.empty:  
        st.info("**🤡 请输入文件哦**")
        return
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    plot_type = st.selectbox(
        " 🧩 选择图表类型:",
        [
            "雷达图", 
            "热力图", 
            "简单线性回归图",
            "柱状图&条形图",
            "饼图",
            "模拟退火"
        ],
        
        key="plot_type_selector",
        on_change=TurnNone
    )
    
    if plot_type == "简单线性回归图":
        with st.expander("🛠️ 线性回归参数设置", expanded=True):
            default.InitSessionState.InitSessionState()
            RenderLinearRegression()
    
    if plot_type == "热力图":
        with st.expander("🛠️ 热力图参数设置", expanded=True):
            default.InitSessionState.InitSessionState()
            RenderHeatMap()
            
    if plot_type == "雷达图":
        with st.expander("🛠️ 雷达图参数设置", expanded=True):
            default.InitSessionState.InitSessionState()
            RenderRadar()
            
    if plot_type == "饼图":
        with st.expander("🛠️ 饼图参数设置", expanded=True):
            default.InitSessionState.InitSessionState()
            RenderPie()

    if plot_type == "柱状图&条形图":
        with st.expander("🛠️ 柱状图&条形图参数设置", expanded=True):
            default.InitSessionState.InitSessionState()
            RenderBar()
    
    if plot_type == "模拟退火":
        with st.expander(" ✍️ 模拟退火算法",expanded=True):
            
            default.InitSessionState.InitSessionState()
            RenderSA()