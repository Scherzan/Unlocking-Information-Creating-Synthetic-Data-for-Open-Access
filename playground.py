#pip install sdv==1.0.0b1
#from sdv.tabular import CTGAN old
import pandas as pd
from sdv.lite import SingleTablePreset
from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata
from sdv.evaluation.single_table import evaluate_quality

rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=rpad_df)

str_col = ['Sex', 'Management', 'Severity']
int_col = ['ID','Length_of_Stay', 'Alvarado_Score', 'Paedriatic_Appendicitis_Score']
float_col = ['Age', 'BMI', 'Height', 'Weight']

for col in rpad_df:
    if col in int_col:
        # explain no needed to assign dtypes
        metadata.update_column(
        column_name=col,
        sdtype='numerical',
        computer_representation='Int64')
    elif col in float_col:
        #rpad_df[col] = rpad_df[col].astype('float')
        metadata.update_column(
        column_name=col,
        sdtype='numerical',
        computer_representation='Float')

model = CTGANSynthesizer(
    metadata,
   # name='FAST_ML'
)
model.fit(rpad_df)

synth_rpad = model.sample(num_rows=200)
print(synth_rpad.head(5))

quality_report = evaluate_quality(
    rpad_df,
    synth_rpad,
    metadata
)
