
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