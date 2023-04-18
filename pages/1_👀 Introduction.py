#from fixed_params import AUTHOR, IMAGES_DIR
import utils.fixed_params as fp
import streamlit as st
from utils.helper_f import local_css_from_str, str_css, str_selectbox_text

local_css_from_str([str_css, str_selectbox_text])

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["I am", "talking about", "synthetic data,", "when to use it,", "why to use it", "and how to generate it."])

with tab1:
   col_a, col_b= st.columns(2)
   
   with col_a:
       #st.header("It's me")
       st.write("### This is Me")
   
       st.write("""
       🏷️: Antonia Scherz \n
       🏠: Berlin \n
       🏢: PD - Berater der öffentlichen Hand \n
       🧭: Consultant/Data Scientist \n
       """)
       st.image("images/anto_scherz.jpg")
       #st.write("LinekdIn: [https://www.linkedin.com/in/antonia-scherz-7b4740178](%s)" % "https://www.linkedin.com/in/antonia-scherz-7b4740178")
          
   with col_b:
       st.write("### Project experience:")
   
       st.write("""
       🪄 prototyping ml-applications and exploring their value for the public sector \n
       🪄 synthesize public administration data for scientific use 
       """)
   
       #options = st.multiselect(
       #    'My env',
       #    ['Python', 'Streamlit', 'Docker', 'PyTorch', "PyTest", "SDV", "Ray(tune)"],
       #    ['Python', 'Streamlit', 'Docker', 'PyTorch', "PyTest", "SDV", "Ray(tune)"])
       #st.write("")
       #st.write("Github: [https://github.com/Scherzan](%s)" % "https://github.com/Scherzan")

# R; Stata; Plotly
       

with tab2:
   st.markdown("### We will be looking at synthetic tabular data.")
   st.text("")
   #st.write("🎛️ How to control synthetic data quality for your own usecase.")
   #st.text("")
   st.write("📋 Demo exercise on how to generate and evaluate data.")
   st.text("")
   st.write("📊 Overview on metrics and evaluation strategies.")
   st.text("")
   st.write("❗Learnings from our synthetic data project")

with tab3:
   st.markdown("### Synthetic data aims to remove any identifiable personal information from the dataset.")
   st.write('<style>div.block-container{padding-top:2rem;}</style>', unsafe_allow_html=True)
   st.image("images/rd_to_std.png", width=650)

with tab4:
   with st.expander(label="What is Synthetic Data used for?", expanded=False):
      st.write("... as an alternative to real data.")
      st.write("... for (predictive) analysis.")
      st.write("... for software testing.")

with tab5:
   st.markdown("### Synthetic data differs from anonymization in that it retains the original data.")
   st.image("images/bilder_anon.png")

   
with tab6:
   st.markdown("### One needs real data to generate synthetic data models.")
   st.image("images/generation.png",width=700)


















