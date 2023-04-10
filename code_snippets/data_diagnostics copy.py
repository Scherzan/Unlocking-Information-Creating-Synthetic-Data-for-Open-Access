import pandas as pd
import json
from sdv.evaluation.single_table import get_column_plot
from sdv.metadata import SingleTableMetadata
rpad_synth = pd.read_csv("synthetic_rpad.csv")
rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

with open('metadata_file.json') as f:
   metadata_dict = json.load(f)

metadata = SingleTableMetadata.load_from_dict(metadata_dict)



fig = get_column_plot(
    real_data=rpad_df,
    synthetic_data=rpad_synth,
    column_name='Length_of_Stay',
    metadata=metadata
)
    
fig.show()
         

        
        