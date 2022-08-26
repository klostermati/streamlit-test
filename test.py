import streamlit as st
import pandas as pd
import numpy as np

@st.experimental_memo
def load_data():
    df = pd.DataFrame(np.random.randn(20, 4), columns=["a", "b", "c","d"])
    return df
    
chart_data = load_data()

st.title("Hello, I'm testing Streamlit")

st.line_chart(chart_data)