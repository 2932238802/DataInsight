
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
        
        "ra_width":None,
        "ra_height":None,
        "raselect_poject":None,      # 选择的行
        "raselect_labels":None,
        "ra_fillalpha":None,
        "ra_fillcolor":None,
        "ra_linewidth":None,
        "ra_linecolor":None,
        "ra_title_name":None,
    }
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
