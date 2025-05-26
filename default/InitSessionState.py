
import streamlit as st

def InitSessionState():
    session_defaults = {
        'df': None, 
        'lrX': None,
        'lry': None,
        "lrcol_width":None,
        "lrcol_height":None,
        "lrtrained_model":None,
        "lrcol_grid_is":None,
        "lrcol_grid_alpha":None,
        "lrcol_scatter_color":None,
        "lrcol_scatter_alpha":None,
        "lrcol_plt_kind":None,      
        "lrcol_plt_color":None,
        "regression_plot":None,
        "regression_plot_predict":None,
        
        "hmcol_width":None,
        "hmcol_height":None,
        "hmlinewidths":None , # 线条宽度
        "hmannot":None,
        "hmcmap":None,
        "hmcenter":None,
        "hm":None,             # 热力图
        
        "ra":None,
        "rawidth":None,
        "raheight":None,
        "raselect_project":None,      # 选择的行
        "raselect_labels":None,
        "rafillalpha":None,
        "rafillcolor":None,
        "ralinewidth":None,
        "ralinecolor":None,
        "ratitle_name":None,
        
        "pietitle_name":None,
        "pieheight":None,
        "piewidth":None,
        "pielabels":None,
        "piesizes":None,
        "pieshadow":None,
        "piestartangle":None,
        "piecolor_theme":None,
        
        "bar_1":None,
        "bar_2":None,
        "barx_label":None,
        "bary_label":None,
        "barcategories":None,
        "barvalues":None,
        "barwidth":None,
        "barheight":None,
        "barinnerwidth":None,
        "barinnerheight":None,
        "barcolor":None,
        "baredgecolor":None,
        "bargridis_1":None,
        "bargridis_2":None
    }
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
