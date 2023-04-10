import streamlit as st
import pandas as pd
import json 


import fixed_params as fp
from utils.helper_f import load_reports, get_image_paths
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata


st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
    </style>""", unsafe_allow_html=True)


@st.cache_data
def get_eval_utils(synth_data_path = "synthetic_rpad.csv", model_path = 'rpad_ep500_dsteps5.pkl',
                   metadata_file="metadata_file.json"):
    rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
    rpad_synth = pd.read_csv(synth_data_path)
    model = CTGANSynthesizer.load(model_path)
    with open(metadata_file) as f:
       metadata_dict = json.load(f)
    metadata = SingleTableMetadata.load_from_dict(metadata_dict)
    return rpad_df, rpad_synth, model, metadata

st.sidebar.title(":memo: Chose Eval Setting")
   
   
with st.sidebar:

    genre = st.radio(
        "Synthetic Data",
        ('default', 'with metadata', 'with constraints', 'with tuning',  'best setting')) #'conditional sampling',
    
    if genre == 'default':
        diagnostic_report, report_q = load_reports('default')
        path_len_of_stay_plt, path_col_shapes_plt, path_age_height_plt = get_image_paths('default')
    if genre == 'with metadata':
        diagnostic_report, report_q = load_reports('metadata')
        path_len_of_stay_plt, path_col_shapes_plt, path_age_height_plt = get_image_paths('metadata')
    if genre == 'with constraints':
        diagnostic_report, report_q = load_reports('constraints')
        path_len_of_stay_plt, path_col_shapes_plt, path_age_height_plt = get_image_paths('constraints')
    if genre == 'with tuning':
        diagnostic_report, report_q = load_reports('tuning')
        path_len_of_stay_plt, path_col_shapes_plt, path_age_height_plt = get_image_paths('tuning')
    if genre == 'best setting':
        diagnostic_report, report_q = load_reports('best_setting')
        path_len_of_stay_plt, path_col_shapes_plt, path_age_height_plt = get_image_paths('best_setting')

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Fidelity: Data Diagnostics", "Fidelity: 1D - Data Quality", "Fidelity: 2D - Data Quality", "Fidelity: 3D - Data Quality", "Utility", "Privacy"])



with tab1:

   st.header("Data Diagnostics")
   
   with st.expander(label="Show Code: Diagnostic Report", expanded=False):
      st.code( # write to file
        """
        from sdmetrics.reports.single_table import DiagnosticReport

        dg_report = DiagnosticReport()
        dg_report.generate(rpad_df, rpad_synth, metadata, verbose=True)
        
        """,
        language="python",
        )

   st.write(diagnostic_report.get_results())   

   with st.expander(label="Show Code: Value Range", expanded=False):
      st.code( 
        """
        from sdv.evaluation.single_table import get_column_plot

        fig = get_column_plot(
         real_data=rpad_df,
         synthetic_data=rpad_synth,
         column_name='Length_of_Stay',
         metadata=metadata
        )
    
        fig.show() 
        
        """,
        language="python",
        )
   
   st.image(path_len_of_stay_plt)
  

with tab2:
   # missing metrics description
   
   with st.expander(label="Show Code: Quality Report", expanded=False):
      st.code(
           """
           from sdv.evaluation.single_table import evaluate_quality

           quality_report = evaluate_quality(rpad_df, rpad_synth, metadata, verbose=True) 
           """,
           language="python",
      )
   
   
   st.write("### Quality Report Summary")

   st.write(report_q.get_score())
   st.write(report_q.get_properties())
   st.image(path_col_shapes_plt)

with tab3:
   
   # missing metrics description
   with st.expander(label="Show Code: 2D Column Comparison", expanded=False):
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
   st.write("### Compare Distribution Across Columns")
   
   st.image(path_age_height_plt)   

with tab4:
   st.write("Hotellings T")
   st.write('detection metric')

with tab5:
   st.write("Regression Problem")
   st.write('Classification Problem')
   
