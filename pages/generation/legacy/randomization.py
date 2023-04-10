import streamlit as st

import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4

tab1, tab2, tab3 = st.tabs(["Generative Modeling", "Metadata", "Controll Randomization"])

with tab1:
   st.header("Generative Modeling")
   st.write("## How do generative models create synthetic data?")
   st.write("### pic missing general modeling behaviour")
   #st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process.svg"))

with tab2:
   st.header("Metadata")
   st.write("## How to help the model with its task?")
   #st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process_scaled.svg"))

with tab3:
   st.header("Controll Randomization")
   st.write("## Can I make sure to always generate the same data and model?")
   #st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process_scaled_docker.svg"))