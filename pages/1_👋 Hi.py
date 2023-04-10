#from fixed_params import AUTHOR, IMAGES_DIR
import fixed_params as fp
import streamlit as st

st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
    </style>""", unsafe_allow_html=True)


tab1, tab2, tab3, tab4 = st.tabs(["I am", "talking about", "synthetic data", "generation."])

with tab1:
   col_a, col_b, col_c = st.columns(3)
   
   with col_a:
       #st.header("It's me")
       st.write("### This is Me")
   
       st.code("Name: Antonia Scherz", language="python")
       st.code("Base: Berlin", language="bash")
       st.code("Work: PD - Berater der Öffentlichen Hand", language="python")
       st.code("Position: Consultant/ML-Engineer", language="python")
       st.code("Without Python I would be.. ", language="python")
       st.code("Flying Pole Aeralist ", language="python")
       st.image("images/anto_scherz.jpg")   
   with col_b:
       st.write("### This is my Experience:")
   
       st.code("Work: Create Public Administration Synthetic Data for Scientific Use", language="bash")
       st.code("Work: Distribute Software Tools for Centralized Usage ", language="python")
       st.code("Voluntary: Visualize World Wide Debt Indicators on Interactive Map for erlassjahr.de", language="bash")
       st.code("Education: Prediction of Appliance Level Energy Load ", language="python")
   
   with col_c:
       st.write("### These are my Skills:")
       st.code("Python", language="bash")

with tab2:
   st.header("Talking About")
   st.write("How to for the talk.")
   st.write("Introduce Outline")

with tab3:
   st.header("Synthetic Data")
   st.image("pages/intro/images/synthetic_data_content.png")
   
with tab4:
   st.header("Cycle withput evaluation")
   st.image("pages/intro/images/Synthetic_Data_generation_process.png")


















