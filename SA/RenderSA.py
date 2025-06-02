
import streamlit as st
from EquationEditor import RenderEditor 


from SA.SA import SA
def RenderSA():
    RenderEditor.RenderEditor()
    
    st.session_state.sa_initial_temp = st.number_input(
        label="输入初始温度",
        key = "initial_temp",
        value= st.session_state.sa_initial_temp if "sa_final_temp" in st.session_state and st.session_state.sa_initial_temp is not None else 0.00
    )
    
    (min,max) = st.session_state.sa_bound
    max = st.number_input(
        label="请输入x变化最大值",
        key = "bounds_max",
        value = float(max) if float(max) is not None else 0.00,
        step=0.01,
    )
    
    min = st.number_input(
        label="请输入x变化最小值",
        key = "bounds_min",
        value= float(min) if float(min) is not None else 0.00,
        step=0.01,
    )
    
    st.session_state.sa_bound = (min,max)
    
    
    st.session_state.sa_final_temp = st.number_input(
        label= "输入截至的最终温度",
        key = "finaltemp",
        value= st.session_state.sa_final_temp if "sa_final_temp" in st.session_state and st.session_state.sa_final_temp is not None else 0.00
    )
    
    st.session_state.sa_cooling_rate = st.number_input(
        label = "请输入初始衰减速率",
        key = "coolingrate",
        max_value=1.0,
        min_value=0.0,
        value= st.session_state.sa_cooling_rate if "sa_final_temp" in st.session_state and st.session_state.sa_cooling_rate is not None else 0.00
    )
    
    st.session_state.sa_initial_step_scale = st.number_input(
        label = "请输入初始步长所占比例",
        key = "initialstepscale",
        max_value=1.0,
        min_value=0.0,
        value= st.session_state.sa_initial_step_scale if "sa_final_temp" in st.session_state and st.session_state.sa_initial_step_scale is not None else 0.00
        
    )
    
    st.session_state.sa_max_iter_per_temp  = st.number_input(
        label = "请输入每个温度需要迭代的次数",
        key = "maxiterpertemp",
        value= st.session_state.sa_max_iter_per_temp if "sa_final_temp" in st.session_state and st.session_state.sa_max_iter_per_temp is not None else 0.00
        
    )
    
    st.button(
        label="开始迭代运行",
        on_click=run
    )
    
def run():
    if "equation" in st.session_state and st.session_state.equation is not None:
        best_x, best_y = SA.SArun()
        if best_x is not None and best_y is not None:
                st.success(f"模拟退火完成！找到了最优解：")
                st.write(f"最优的 x 值是: {best_x:.3f}")
                st.write(f"对应的最优 y 值 (函数最小值) 是: {best_y:.3f}")
                st.balloons() 
        else:
                st.warning("模拟退火未能找到有效的解。")
    
    else:
        st.warning("在正式分析有效值的时候，请你先进行表达式的生成~")


