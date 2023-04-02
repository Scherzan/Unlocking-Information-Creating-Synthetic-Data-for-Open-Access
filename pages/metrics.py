import streamlit as st
import pandas as pd
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.markdown("# Evaluate your Data")
st.sidebar.markdown("# What does good data generation look like?")

st.write(""" outline: (5 min)
1. evaluating synthetic data metrik dashboard anzeigen mit jeweils highlighten was du brauchst
(metriken einzeln durchgehen und erklären) -> simple metriken (software testing)
2. advanced metriken für utility und statostische ähnlichkeit -> auf verschiedene modelle eingehen
3. wissenschafts outlook -> zusammenfassen was es über sdv hinaus gibt -> dashboard was das zeigt
""")

rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
synthetic_rpad = pd.read_csv('synthetic_rpad.csv')

pr_real = rpad_df.profile_report()
#pr_synthetic = synthetic_rpad.profile_report()

st_profile_report(pr_real)

