import streamlit as st

import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4

tab1, tab2, tab3 = st.tabs(["Model Overview", "Model Comparison"])

with tab1:
   st.header("Model Overview")
   #st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process.svg"))

with tab2:
   st.header("Model Comparison")
   #st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process_scaled.svg"))
