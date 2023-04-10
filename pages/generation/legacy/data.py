import streamlit as st

from pages.generation import get_data
import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4
from utils.helper_f import *






    

#more_cats_and_dogs_clicked = st.button("Get cats and dogs !")
#
#N_CATS_AND_DOGS = 8
#col_dogs, col_cats = st.columns(2)
#
#with col_cats:
#    some_cats = dataset.loc[lambda df: df.label == "cats"].sample(N_CATS_AND_DOGS)
#    st.write("Some cats:")
#    st.image([row.image_path for row in some_cats.itertuples()], width=150)
#
#with col_dogs:
#    some_dogs = dataset.loc[lambda df: df.label == "dogs"].sample(N_CATS_AND_DOGS)
#    st.write("Some dogs:")
#    st.image([row.image_path for row in some_dogs.itertuples()], width=150)
#