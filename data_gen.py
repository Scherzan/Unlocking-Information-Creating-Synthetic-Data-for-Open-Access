import pandas as pd
import numpy as np
#pip install sdv==1.0.0b1
#from sdv.tabular import CTGAN old
from sdv.single_table import CTGANSynthesizer

rpad_df = pd.read_excel(r'RPAD_data.xlsx', engine='openpyxl')
print(rpad_df.shape)
print(rpad_df.head(10))

#rpad_df = rpad_df[['Age', 'BMI', 'Sex', 'Height', 'Weight',
#                          'Length_of_Stay', 'Management', 'Severity',
#                          'Alvarado_Score', 'Paedriatic_Appendicitis_Score']]
#rpad_df.insert(0, 'ID', list(np.random.permutation(np.arange(1000,9999))[:len(rpad_df)]))
##rpad_df.to_excel(r'RPAD_data_small.xlsx')
#print(rpad_df.shape)
#rpad_df.head(10)
#
## work on rounding scheme age