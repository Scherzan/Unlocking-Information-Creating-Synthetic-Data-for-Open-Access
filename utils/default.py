import pandas as pd
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer
from sdv.evaluation.single_table import evaluate_quality

rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=rpad_df)

model = CTGANSynthesizer(metadata)
model.fit(rpad_df)

synth_data = model.sample(num_rows=rpad_df.shape[0])
