# 库
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

class BarAnalysis():
    """
    柱状图：
        分析逻辑
        绘画逻辑
    fig1,fig2:
        分别是竖着和横着的
    """
    
    @staticmethod
    def Draw():

        x_label = st.session_state.barx_label
        y_label = st.session_state.bary_label
        categories = st.session_state.barcategories
        values = st.session_state.barvalues
        width = st.session_state.barwidth
        height = st.session_state.barheight
        barwidth = st.session_state.barinnerwidth 
        barheight = st.session_state.barinnerheight 
        color = st.session_state.barcolor
        edgecolor = st.session_state.baredgecolor
        title = st.session_state.bartitle
        labelfontsize = st.session_state.barlabelfontsize
        
        fig1, ax1 = plt.subplots(figsize=(width, height))
        fig2, ax2 = plt.subplots(figsize=(width, height))
        
        if st.session_state.bargridis_1:
            ax1.grid(axis='y', linestyle='--', alpha=0.7)
        if st.session_state.bargridis_2:
            ax2.grid(axis='x', linestyle='--', alpha=0.7)
            
        ax1.bar(
            categories, 
            values, 
            color=color, 
            edgecolor=edgecolor, 
            width=barwidth
            ) 
        
        ax2.barh(
            categories, 
            values, 
            color=color, 
            edgecolor=edgecolor, 
            height=barheight
        )
        
        ax1.set_title(title, fontsize=labelfontsize)
        ax1.set_xlabel(x_label, fontsize=labelfontsize)
        ax1.set_ylabel(y_label, fontsize=labelfontsize)
        ax2.set_title(title, fontsize=labelfontsize)
        ax2.set_xlabel(y_label, fontsize=labelfontsize)
        ax2.set_ylabel(x_label, fontsize=labelfontsize)
        
        return fig1,fig2
    