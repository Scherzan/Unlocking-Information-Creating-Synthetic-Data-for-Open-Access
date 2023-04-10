import streamlit as st

import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4


st.header("Generative Modeling")
st.write("## How do generative models create synthetic data?")
st.write("### pic missing general modeling behaviour")
with st.expander(label="playground.py", expanded=False):
    with open(f"/home/antonia/code/Unlocking-Information/playground.py", "r") as f:
        st.code(f.read())