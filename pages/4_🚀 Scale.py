import streamlit as st
import time
import pandas as pd
from stqdm import stqdm

st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
    </style>""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Using Ray", "Handling imbalanced Data"])

with tab1:

    with st.expander(label="Show Code: Combine Ray and SDV", expanded=False):
       st.code(
            """
            from sdv.evaluation.single_table import get_column_pair_plot

            fig = get_column_pair_plot(
                real_data=rpad_df,
                synthetic_data=new_data,
                column_names=['Age', 'Height'],
                metadata=metadata)
                
            fig.show()
            """,
            language="python",
       )    
    col_a, col_b = st.columns(2)
   
    with col_a:
       st.write( """
       data shape:    (782, 11) \n
       model:         CTGANSynthesizer \n
       epochs:        300 \n
       Other Factors: No additional discriminator steps
       """)
    
    with col_b:
       if st.button('StartTraining Simulation'):

          progress_text_ray = "Training with Ray."
          progress_text_gpu = "Training with GPU (default)."
          progress_text_cpu = "Training with CPU (don't aks.)."
          my_bar_ray = st.progress(0, text=progress_text_ray)
          my_bar_gpu = st.progress(0, text=progress_text_gpu)
          my_bar_cpu = st.progress(0, text=progress_text_cpu)
          
          for percent_complete in range(0,100, 1):
              time.sleep(0.1)
              my_bar_cpu.progress(percent_complete + 1, text=progress_text_cpu)
              if percent_complete <= 50:
                 my_bar_gpu.progress(percent_complete *2, text=progress_text_gpu)
              if percent_complete <= 25:
                 my_bar_ray.progress(percent_complete * 4, text=progress_text_ray)
       else:
          st.write('No training simulation run')

with tab2:
   st.code("""
   conditional sampling
   """)
       

