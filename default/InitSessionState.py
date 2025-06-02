
import streamlit as st

def InitSessionState():
    session_defaults = {
        
        'current_expression':"",      # 用户输入表达式
        'sa_bound':(0.00,100.00),          
        'equation':None,              # 最终形成表达式
        "equation":None,
        'sa_cooling_rate':None,
        'sa_initial_temp':None,       # 初始化温度
        'sa_final_temp':None,         # 最终温度
        'sa_initial_step_scale':None, # 初始衰减步长
        'sa_max_iter_per_temp':None,  # 迭代次数
        
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
        "hmlinewidths":None ,         # 线条宽度
        "hmannot":None,
        "hmcmap":None,
        "hmcenter":None,
        "hm":None,                    # 热力图
        
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
        "bargridis_2":None,
        
        # 内网穿透
        "ngrok_tunnel_active":None,
        "ngrok_public_url":None,
        "ngrok_error":None
    }
    
    for key, value in session_defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
