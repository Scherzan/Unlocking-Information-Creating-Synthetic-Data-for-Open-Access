import streamlit as st
import pandas as pd

import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4
from pages.generation import get_data, get_synt_data
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata
from sdmetrics.reports.single_table import DiagnosticReport
import json 



# use my_metadata_dict in the SDMetrics library
# ranges, nan values, 
rpad_synth = pd.read_csv("synthetic_rpad.csv")
rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
model = CTGANSynthesizer.load('rpad_ep500_dsteps5.pkl')
with open('metadata_file.json') as f:
   metadata = json.load(f)

dg_report = DiagnosticReport()


st.header("Data Diagnostics")

code_col, output_col = st.columns([2, 1])

with code_col:
   with st.expander(label="Nan Values", expanded=False):
      st.code(
            """
            import pandas as pd
            import json 
            from sdmetrics.reports.single_table import DiagnosticReport

            rpad_synth = pd.read_csv("synthetic_rpad.csv")
            rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
            with open('metadata_file.json') as f:
            metadata = json.load(f)

            dg_report = DiagnosticReport()
            dg_report.generate(rpad_df, rpad_synth, metadata, verbose=True)
       
            """,
            language="python",
      )

with output_col:
   st.write(dg_report.generate(rpad_df, rpad_synth, metadata, verbose=True))