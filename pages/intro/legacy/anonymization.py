import streamlit as st
import streamlit_book as stb

import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4


st.title("What I am going to show you today")
st_write_bs4(make_img(src=fp.IMAGES_DIR / "anonymization_faces.svg"))
#st.image("images/Synthetic_Data_generation_process.svg")

st.write("### Another approach: build an entire experiment tracking system with small bricks")