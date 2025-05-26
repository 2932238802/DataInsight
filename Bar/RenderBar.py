

import streamlit as st
import pandas as pd
from common import pltconfig

from Bar.BarAnalysis import BarAnalysis

def RenderBar():
    
    df = st.session_state.df
    
    for row_index_label in df.index:
        for col_name in df.columns:
            value = df.loc[row_index_label, col_name]
            reason = "无"
            is_empty = False
            if pd.isna(value):
                is_empty = True
                reason = "NaN/None"
            elif isinstance(value, str) and value.strip() == "":
                is_empty = True
                reason = "空或纯空格字符串"
            if is_empty:
                row_num = df.index.get_loc(row_index_label) + 1
                col_num = df.columns.get_loc(col_name) + 1
                st.error(
                    f"该表格存在空缺位置!\n"
                    f"位置: 行 '{row_index_label}' (第 {row_num} 行), "
                    f"列 '{col_name}' (第 {col_num} 列)。\n"
                    f"原因: {reason} (原始值: '{value}')"
                )
                return False
            
    barcol_width, barcol_height = st.columns(2)
    
    with barcol_width:
        st.session_state.barwidth = st.selectbox(
            " ✍️ 选择图像宽度(10 较为合适英寸)",
            pltconfig.PLTWIDTH,
            index = 5 if len(pltconfig.PLTWIDTH) > 5 else len(pltconfig.PLTWIDTH) - 1,
            key = "hm_width",
            help = "绘制图案的宽"
        )
        
    with barcol_height:
        st.session_state.barheight = st.selectbox(
            " 🦘 选择图像高度(6 较为合适英寸)",
            pltconfig.PLTHEIGHT,
            index = 2 if len(pltconfig.PLTHEIGHT) > 2 else len(pltconfig.PLTHEIGHT) - 1,
            key = "hm_height",
            help = "绘制图案的高"
        )
    
    # 标题
    st.session_state.bartitle = st.text_input(
        "输入柱状图标题",
        value="柱状图",
        max_chars=15,
        key= "bar_title",
    )
    
    col1,col2 = st.columns(2)
    with col1: 
        st.session_state.barx_label = st.selectbox(
            label="选择x轴的标签名(种类)",
            options= df.columns,
            key = "bar_x_label"
        )
        
    y_option = [i for i in df.columns if i != st.session_state.barx_label]
    with col2: 
        st.session_state.bary_label = st.selectbox(
            label="选择y轴的标签名(数值)",
            options= y_option,
            key = "bar_y_label"
        )
    
    
    if st.session_state.get("barx_label"):
        st.session_state.barcategories = df[st.session_state.barx_label].tolist()
    
    if st.session_state.get("bary_label"):
        st.session_state.barvalues = df[st.session_state.bary_label].tolist()

    st.info(f"选择种类列是 : {st.session_state.barcategories}")
    st.info(f"选择的数据列是 : {st.session_state.barvalues}")
    
    
    col3,col4 = st.columns(2)
    
    with col3:
        st.session_state.barinnerwidth = st.slider(
            label=" 💀 垂直柱状图内部的宽度",
            min_value= 0.3,
            max_value= 1.0,
            value=0.8,
            step=0.05,
        )
        
    with col4:
        st.session_state.barinnerheight = st.slider(
            label=" 👾 水平柱状图内部的宽度",
            min_value= 0.3,
            max_value= 1.0,
            value=0.8,
            step=0.05,
        )
    
    col5,col6 = st.columns(2)
    
    with col5:
        st.session_state.barcolor = st.selectbox(
            label=" ☠️ 选择柱状图的主要颜色基调",
            options = pltconfig.COLOR,
            key = "bar_color"
        )
    
    with col6:
        st.session_state.baredgecolor = st.selectbox(
            label=" 🦙 选择柱状图的边缘颜色基调",
            options = pltconfig.COLOR,
            key = "bar_edgecolor"
        )
    
    st.session_state.barlabelfontsize = st.number_input(
        label=" 👿 字体大小",
        min_value= 8,
        max_value= 24,
        key= "bar_labelfontsize"
    )
    
    col7,col8 = st.columns(2)
    
    with col7:
        st.session_state.bargridis_1 = st.radio(
            "是否需要网格线",
            options=["是","否"],
            index=1,
            key = "bar_gridis_1"
        )
    
    with col8:
        st.session_state.bargridis_2 = st.radio(
            "是否需要网格线",
            options=["是","否"],
            index=1,
            key = "bar_gridis_2"
        )
        
    if st.session_state.bargridis_1 == "否":
        st.session_state.bargridis_1 = False
    else:
        st.session_state.bargridis_1 = True
        
    if st.session_state.bargridis_2 == "否":
        st.session_state.bargridis_2 = False
    else:
        st.session_state.bargridis_2 = True
        
    
    
    if st.button(" 🫏 开始渲染", key="run_bar"):
        PerformBar()
        

def PerformBar():
    fig1,fig2 = BarAnalysis.Draw()
    
    st.session_state.bar_1 = fig1
    st.session_state.bar_2 = fig2
    
    