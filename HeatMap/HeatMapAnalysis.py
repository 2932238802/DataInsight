
import seaborn as se
import streamlit as st
import matplotlib.pyplot as plt
class HeatMapAnalysis:
    
    @staticmethod
    
    def DrawHM(
        width,
        height,
        df,
        annot,
        cmap,
        center,
        linewidths,
        linecolor
    ):
        """
        Args:
            width (_type_): 热力图的宽度
            height (_type_): 热力图的高度
            df (_type_): 数据
            annot (_type_): 是否显示数值
            cmap (_type_): 选择颜色样式
            center (_type_): 是不是需要居中
            linewidths (_type_): 线条宽度
            linecolor (_type_): 线条颜色
        Returns:
            返回图表
        """
        fig, ax = plt.subplots(figsize=(width, height))
        se.heatmap(
            data =  df,
            annot= annot,
            cmap= cmap,
            center = center,
            linewidths=linewidths,
            linecolor= linecolor,
        )
        return fig