
import streamlit as st
import pandas as pd
from common import pltconfig

from Pie import PieAnalysis
def RenderPie():
    
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
    
    st.session_state.pietitle_name = st.text_input(
        label="请输入标题名字",
        value="饼图",
        key="pie_title_name"
    )
    
    pie_width_cols,pie_height_cols = st.columns(2)
    
    with pie_width_cols:
        st.session_state.piewidth = st.selectbox(
            "✍️ 选择图像宽度(英寸)",
            options=pltconfig.PLTWIDTH,  
            index=5 if len(pltconfig.PLTWIDTH) > 5 else len(pltconfig.PLTWIDTH) - 1,
            key="pie_width",
            help="绘制图形的宽度，单位为英寸"
        )
        
    # 高度
    with pie_height_cols:
        st.session_state.pieheight = st.selectbox(
            "🦘 选择图像高度(英寸)",
            options=pltconfig.PLTWIDTH,  
            index=2 if len(pltconfig.PLTHEIGHT) > 2 else len(pltconfig.PLTHEIGHT) - 1,
            key="radar_height",
            help="绘制图形的高度，单位为英寸"
        )
            
    labels,sizes = st.columns(2)
    with labels:
        st.session_state.pielabels = st.selectbox(
            label = "选择对应的标签列",
            options= df.columns,
            index=0,
            key = "pie_labels",
        )
    
    y_option = [i for i in df.columns if i != st.session_state.pielabels]
    with sizes:
        st.session_state.piesizes = st.selectbox(
            label = "选择对应的数据列",
            options= y_option,
            index=0,
            key = "pie_sizes",
        )
    
    shadow,startangle = st.columns(2)
    
    with shadow:
        pie_shadow = st.radio(
            label= "是否需要阴影",
            options=["是","否"],
            index = 1,
            key = "pie_shadow"
        )
        
        if pie_shadow == "是":
            st.session_state.pieshadow = True
        else:
            st.session_state.pieshadow = False

        
        
    with startangle:
        st.session_state.piestartangle= st.slider(
        "起始角度", 
        min_value=0, 
        max_value=360, 
        value=0,  
        step=1,
        key = "pie_startangle"
    )
        
    # piecolor_theme_choose  = st.selectbox(
    #     label = "主题颜色选择",
    #     options=pltconfig.COLOR_THEME_OPTIONS.keys(),
    #     index=0,
    #     key = "pie_color_theme",
    # )    
    
    # st.session_state.piecolor_theme = pltconfig.COLOR_THEME_OPTIONS[piecolor_theme_choose]
    
    if st.button(
        label="开始渲染",
        key = "pie_draw",
    ):
        PerformPieAnalysis()
        
def PerformPieAnalysis():
    
    fig = PieAnalysis.PieAnalysis.Draw()
    
    st.session_state.pie = fig
    st.success("数据渲染完成")
    
        
    
        
    
            
    