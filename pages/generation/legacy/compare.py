import streamlit as st
import pandas as pd

import fixed_params as fp
from pages.generation import get_data, get_synt_data
from utils.html_factory import make_img, st_write_bs4

st.header("Synthetic Data")

rpad_synth = get_synt_data()
st.write(rpad_synth.style.format(subset=['Age', 'BMI','Height', 'Weight', 'Length_of_Stay', 'Alvarado_Score', 'PA_Score'], formatter="{:.2f}")) #df.style.format(

st.header("Real Data")
with st.expander(label="Real Data", expanded=False):

    rpad_df = get_data()
    st.write(rpad_df.style.format(subset=['Age', 'BMI','Height', 'Weight', 'Length_of_Stay', 'Alvarado_Score', 'PA_Score'], formatter="{:.2f}")) #df.style.format(
