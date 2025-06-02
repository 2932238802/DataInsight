
import random
import numpy as np
import math
import streamlit as st
class SA:
    
    @staticmethod
    def SArun():
        initial_temp = st.session_state.sa_initial_temp
        bounds = st.session_state.sa_bound
        final_temp:float = st.session_state.sa_final_temp
        cooling_rate:float = st.session_state.sa_cooling_rate
        max_iter_per_temp:int = st.session_state.sa_max_iter_per_temp         # 每次的迭代次数
        initial_step_scale:float = st.session_state.sa_initial_step_scale     # 最初步长所占比例
        func = st.session_state.equation
        
        min_x,max_x = bounds
        current_temp = initial_temp
        
        current_x = random.uniform(min_x, max_x)
        current_y = func(current_x)
        
        best_x = current_x
        best_y = current_y
        
        while current_temp > final_temp:
            
            for _ in range(max_iter_per_temp):
                
                step_scale = (max_x - min_x) * initial_step_scale
                
                # 扰动随机数
                temp_ratio = (current_temp / max(final_temp, 1e-9))
                perturbed =random.uniform(-step_scale,step_scale)*temp_ratio
                
                neighbor_x = current_x + perturbed
                neighbor_x = max(min_x, min(max_x, neighbor_x))
                
                try:
                    neighbor_y = func(neighbor_x)
                    
                    if  np.isnan(neighbor_y) or np.isinf(neighbor_y) :
                        neighbor_y = float('inf')
                
                except Exception:
                    neighbor_y = float('inf')
                    continue
                
                delta_e = neighbor_y - current_y

                if delta_e < 0: 
                    current_x = neighbor_x
                    current_y = neighbor_y
                    if current_y < best_y:
                        best_x = current_x
                        best_y = current_y
                else: 
                    if random.uniform(0, 1) < math.exp(-delta_e / current_temp):
                        current_x = neighbor_x
                        current_y = neighbor_y
                    
            current_temp *= cooling_rate 

        if np.isinf(best_y): 
            return None, None

        return best_x, best_y

    