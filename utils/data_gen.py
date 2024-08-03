import pandas as pd

rpad_df = pd.read_excel(r"RPAD_data.xlsx", engine="openpyxl")
print(rpad_df.shape)
print(rpad_df.head(10))
