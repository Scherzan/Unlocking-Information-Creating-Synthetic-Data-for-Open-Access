import pandas as pd
from sdv.lite import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality

rpad_df = pd.read_excel(r"RPAD_data_small.xlsx", engine="openpyxl")

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=rpad_df)

model = CTGANSynthesizer(metadata)
model.fit(rpad_df)

synth_rpad = model.sample(num_rows=200)

quality_report = evaluate_quality(rpad_df, synth_rpad, metadata)
