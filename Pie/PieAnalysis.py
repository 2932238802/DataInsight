
import matplotlib.pyplot as plt
import streamlit as st
class PieAnalysis:
    
    @staticmethod
    def Draw():
        
        width = st.session_state.piewidth
        height = st.session_state.pieheight
        
        fig, ax = plt.subplots(figsize=(width, height)) 
        
        sizes = st.session_state.piesizes
        labels = st.session_state.pielabels
        shadow = st.session_state.pieshadow
        startangle = st.session_state.piestartangle
        pietitlename = st.session_state.pietitle_name
        df = st.session_state.df
        
        ax.pie(
            df[sizes],
            labels=df[labels],
            # colors=color,
            autopct='%1.1f%%',  
            shadow=shadow,        
            startangle=startangle
        )
        
        ax.legend()
        
        ax.axis('equal')
        ax.set_title(f"{pietitlename}")
        return fig
        
        