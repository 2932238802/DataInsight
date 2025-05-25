
import streamlit as st
from common import pltconfig
import pandas as pd
import common.pltconfig 
from Radar import RadarAnalysis

def RenderRadar(numerical_cols):
    
    radar_width, radar_height = st.columns(2)
    
    st.session_state.ra_title_name = st.text_input(
        label="请输入标题名字",
        value="雷达图",
        key="ratitle_name"
    )
    
    # 宽度
    with radar_width:
        st.session_state.ra_width = st.selectbox(
            "✍️ 选择图像宽度(英寸)",
            options=pltconfig.PLTWIDTH,  
            index=5 if len(pltconfig.PLTWIDTH) > 5 else len(pltconfig.PLTWIDTH) - 1,
            key="radar_width",
            help="绘制图形的宽度，单位为英寸"
        )
        
    # 高度
    with radar_height:
        st.session_state.ra_height = st.selectbox(
            "🦘 选择图像高度(英寸)",
            options=pltconfig.PLTWIDTH,  
            index=2 if len(pltconfig.PLTHEIGHT) > 2 else len(pltconfig.PLTHEIGHT) - 1,
            key="radar_height",
            help="绘制图形的高度，单位为英寸"
        )
    
    choose_project,choose_choices = st.columns(2)
    
    # 强行改为项目 方便分析
    df = st.session_state.df.copy()
    projects = df.iloc[:, 0] 
    
    with choose_project:
        ra_choose_project = st.selectbox(
            "请选择对应的项目",
            projects,
            index = 0,
            key = "ra_select_poject",
            help= "指定对应的行"
        )
    st.session_state.raselect_poject = ra_choose_project
    
    with choose_choices:
        ra_choose_choices = st.multiselect(
            label= "选择对应的属性",
            options=df.columns[1:].tolist(),
            default=df.columns[1:].tolist(), 
            key = "ra_select_labels",
            help = "绘制对应雷达图所需的属性"
        )
    st.session_state.raselect_labels = ra_choose_choices
        
    
    ra_linecolor,ra_linewidth = st.columns(2)
    
    with ra_linecolor:
        st.session_state.ra_linecolor = st.selectbox(
            label= "选择雷达图边缘线颜色",
            options = common.pltconfig.COLOR,
            index= 0,
            key = "ralinecolor"
        )
    with ra_linewidth:
        st.session_state.ra_linewidth = st.slider(
            label = "边缘线的厚度",
            min_value= 0.1,
            max_value= 2.0,
            value= 1.0,
            step = 0.05,
            key = "arlinewidth"
        )
    
    ra_fillcolor,ra_fillalpha = st.columns(2)
    
    with ra_fillcolor:
        st.session_state.ra_fillcolor = st.selectbox(
            label = "填充颜色",
            options = common.pltconfig.COLOR,
            index= 0,
            key = "rafillcolor"
        )
    with ra_fillalpha:
        st.session_state.ra_fillalpha = st.slider(
            label = "填充的透明度",
            min_value= 0.0,
            max_value= 1.0,
            value= 0.8,
            step = 0.05,
            key = "arlinealpha"
        )
    
    
    if st.button(" 🫏 开始渲染", key="run_heatmap"):
        PerformRa()
        
        
def PerformRa():
    width = st.session_state.ra_width
    height =st.session_state.ra_height
    labels = st.session_state.raselect_labels
    
    df = st.session_state.df
    project_row_series = df.loc[st.session_state.raselect_poject]

    stats_series = project_row_series[st.session_state.raselect_labels]
    stats = stats_series.tolist() 
    
    if RadarAnalysis.RadarAnalysis.Validate(st.session_state.raselect_poject):
        st.success(" 🐮 数据都存在 开始绘制!")
    else:
        st.error(" 🤡 数据错误!")
        return 
    
    titlename = st.session_state.ra_title_name
    linecolor = st.session_state.ra_linecolor
    linewidth = st.session_state.ra_linewidth
    fillalpha =  st.session_state.ra_fillalpha
    fillcolor = st.session_state.ra_fillcolor
    fig = RadarAnalysis.RadarAnalysis.Draw(
        width=width,
        height=height,
        labels=labels,
        stats=stats,
        titlename=titlename,
        linecolor=linecolor,
        linewidth=linewidth,
        fill_alpha=fillalpha,
        fill_color=fillcolor
    )
    
    st.session_state.ra = fig
    st.success("数据渲染完成")