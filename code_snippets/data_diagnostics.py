import pandas as pd
import json
from sdmetrics.reports.single_table import DiagnosticReport
from sdv.metadata import SingleTableMetadata
rpad_synth = pd.read_csv("synthetic_rpad.csv")
rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

with open('metadata_file.json') as f:
   metadata_dict = json.load(f)

metadata = SingleTableMetadata.load_from_dict(metadata_dict)

dg_report = DiagnosticReport()
dg_report.generate(rpad_df, rpad_synth, metadata, verbose=True)
         

        
        