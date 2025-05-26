
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class RadarAnalysis:
    
    @staticmethod
    def Validate(select_project_name: str) -> bool:
        if 'df' not in st.session_state or st.session_state.df is None:
            st.error("数据尚未加载 (st.session_state.df is None)。")
            return False
        
        if 'raselect_labels' not in st.session_state or not st.session_state.raselect_labels:
            st.error("尚未选择雷达图的属性 (st.session_state.raselect_labels is empty)。")
            return False

        df_copy = st.session_state.df.copy()
        project_column_name = df_copy.columns[0]
        selected_attributes = st.session_state.raselect_labels
        project_row_df = df_copy[df_copy[project_column_name] == select_project_name]

        if project_row_df.empty:
            st.warning(f"项目 '{select_project_name}' 在数据中未找到")
            return False

        project_data = project_row_df.iloc[0]

        for attribute_label in selected_attributes:
            if attribute_label not in project_data.index:
                st.warning(f"项目 '{select_project_name}' 缺少属性 '{attribute_label}'。")
                return False
            value = project_data[attribute_label]
            if pd.isna(value):
                st.warning(f"项目 '{select_project_name}' 的属性 '{attribute_label}' 的值为空")
                return False
        
            if not isinstance(value, (int, float, np.number)):
                st.warning(f"项目 '{select_project_name}' 的属性 '{attribute_label}' 的值 ('{value}') 不是有效的数字类型。")
                return False
        return True
    
    
    @staticmethod
    def Draw(
        # 尺寸 宽
        width: int,
        # 尺寸 高
        height:int,
        # 标签
        labels: list,
        # 数据
        stats: list,
        # 标题名字
        titlename:str,
        # 线的颜色
        linecolor:str,
        
        linewidth:float,
        
        fill_alpha,
        # 填充颜色
        fill_color:str
             ):
        
        # 绘制图像
        angles = np.linspace(0,2*np.pi,len(labels),endpoint=False).tolist()
        
        stats += stats[:1]
        angles += angles[:1]
        
        fig,ax = plt.subplots(
            figsize=(width,height),
            subplot_kw=dict(polar = True)
            )
        
        ax.plot(angles,stats,color = linecolor,linewidth = linewidth)
        ax.fill(angles,stats,color = fill_color,alpha = fill_alpha)
        ax.set_yticklabels([])
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels)
        plt.title(titlename)
        return fig
        
        
    
    