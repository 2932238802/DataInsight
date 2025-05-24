import streamlit as st
import numpy as np

from LinearRegression.RenderLinearRegression import RenderLinearRegression
import default.InitSessionState


def TurnNone():
    """当图表类型改变时，重置相关的 session_state 变量。"""
    keys_to_reset = [
        'regression_plot',
        'regression_plot_predict',
    ]
    
    for key in keys_to_reset:
        if key in st.session_state:
            st.session_state[key] = None
            
    st.info("图表类型已更改，相关分析结果已重置") 

            
def RenderAnalysis():
    
    df = st.session_state.get('df', None)
    
    # 获取数据
    # 返回列表
    if df is None or df.empty:  # 同时检查None和空DataFrame
        st.info("**🤡 请输入文件哦**")
        return
    numerical_cols = df.select_dtypes(include=np.number).columns.tolist()
    
    plot_type = st.selectbox(
        " 🧩 选择图表类型:",
        ["散点图", "热力图", "简单线性回归图"],
        key="plot_type_selector",
        on_change=TurnNone
    )
    
    if plot_type == "简单线性回归图":
        with st.expander("🛠️ 线性回归参数设置", expanded=True):
            RenderLinearRegression(numerical_cols)
    
    if plot_type == "热力图":
        with st.expander("🛠️ 线性回归参数设置", expanded=True):
            # TODO:这里完成热力图渲染
            pass
        
            
