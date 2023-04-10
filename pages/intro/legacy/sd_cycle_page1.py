import streamlit as st

import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process.svg"))

with tab2:
   st.header("A dog")
   st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process_scaled.svg"))

with tab3:
   st.header("An owl")
   st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process_scaled_docker.svg"))

