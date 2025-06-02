

import streamlit as st
from Ngrok import Ngrok
def RenderNgrok():
    
    if st.session_state.get("ngrok_tunnel_active", False):
        button_label = "⏹️ 关闭共享网址"
        button_help = "点击关闭 ngrok 内网穿透，停止公网访问"
        button_type = "secondary" 
    else:
        button_label = "🚀 启动共享网址"
        button_help = "点击启动 ngrok 内网穿透，生成公网访问此应用的 URL"
        button_type = "primary"
 
    st.button(
        label=button_label,
        key="ngrok_toggle_button", 
        on_click=Run,
        help=button_help,
        type=button_type,
        use_container_width=True
    )
    
    if st.session_state.get("ngrok_tunnel_active"):
        st.success("grok 启动成功!")
    
    if st.session_state.get("ngrok_error"):
        st.error(st.session_state.ngrok_error)
        
    
    

def Run():
    if not st.session_state.get("ngrok_tunnel_active", False):
        with st.spinner("正在启动 ..."):
            public_url = Ngrok.Ngrok.Connect()
            if public_url:
                st.success(st.session_state.ngrok_public_url)
            else:
                st.error("启动失败!")
                
    else:
        with st.spinner("正在关闭 ..."):
            success = Ngrok.Ngrok.ShutDown()
            if success:
                st.success("关闭成功！")
                
        
    