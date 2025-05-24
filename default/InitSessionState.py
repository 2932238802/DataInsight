
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
        "regression_plot_predict":None
        
    }
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
