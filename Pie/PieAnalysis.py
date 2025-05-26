
import streamlit as st
def PieAnalysis():
    
    df = st.session_state.df
    
    labels,sizes = st.columns(2)
    with labels:
        st.session_state.pielabels = st.selectbox(
            label = "选择对应的标签列",
            options= df.columns,
            index=0,
            key = "pie_labels",
        )
    
    with sizes:
        st.session_state.pielabels = st.selectbox(
            label = "选择对应的数据列",
            options= df.columns,
            index=0,
            key = "pie_sizes",
        )