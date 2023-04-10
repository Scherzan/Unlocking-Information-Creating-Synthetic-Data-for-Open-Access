
import streamlit as st
import matplotlib.pyplot as plt
import fixed_params as fp
from streamlit_ace import st_ace

st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
    </style>""", unsafe_allow_html=True)

@st.cache_data(persist=True)
def get_data():
   import pandas as pd
   rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
   rpad_df.rename(columns={'Paedriatic_Appendicitis_Score': 'PA_Score'}, inplace=True)
   return rpad_df

@st.cache_data(persist=True)
def get_synt_data():
   import pandas as pd
   rpad_synth = pd.read_csv("synthetic_rpad.csv")
   rpad_synth.rename(columns={'Paedriatic_Appendicitis_Score': 'PA_Score'}, inplace=True)
   return rpad_synth

rpad_synth = get_synt_data()
rpad_df = get_data()

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Use real data", "to model", "synthetic data", "And now?", 
                                  "Describe the data", "better", "and tune the model"])

with tab1:
   st.header("Data")
   st.title("Regensburg Pediatric Appendicitis Dataset")

   dtypes_df = rpad_df.dtypes.value_counts().to_frame('dtypes').reset_index()
   names = dtypes_df['index']
   sizes = dtypes_df['dtypes']
   colors = ['#cb6ce6', '#8c52ff', '#ff66c4']
   
   col_a, col_b = st.columns(2)
   with col_a:
      fig, ax = plt.subplots()
      my_circle = plt.Circle( (0,0), 0.7, color='white')
      ax.pie(sizes, labels=names, labeldistance=0.45, colors=colors)
      ax.add_artist(my_circle)
   
      st.pyplot(fig)
   
      st.write(f'data shape: {rpad_df.shape}')
   
   with col_b:
      df_info = rpad_df.isna().sum().to_frame('Missings').reset_index()
      df_info.index.set_names(['Column'])
      st.table(df_info)
   
   st.write(rpad_df.style.format(subset=['Age', 'BMI','Height', 'Weight', 'Length_of_Stay', 'Alvarado_Score', 'PA_Score'], formatter="{:.2f}")) #df.style.format(

with tab2:
   st.header("Workflow")

   with st.expander(label="playground.py", expanded=False):
        with open(f"/home/antonia/code/Unlocking-Information/playground.py", "r") as f:
            st.code(f.read())
   
   st.write("🚀 **Added pipeline and parameters path:**")

with tab3:
   st.header("Synthetic Data")

   st.write(rpad_synth.style.format(subset=['Age', 'BMI','Height', 'Weight', 'Length_of_Stay', 'Alvarado_Score', 'PA_Score'], formatter="{:.2f}")) #df.style.format(
   
   st.header("Real Data")
   with st.expander(label="Real Data", expanded=False):
       
       st.write(rpad_df.style.format(subset=['Age', 'BMI','Height', 'Weight', 'Length_of_Stay', 'Alvarado_Score', 'PA_Score'], formatter="{:.2f}")) #df.style.format(

with tab4:
   st.header("With evaluation")
   st.image("pages/generation/images/Synthetic_Data_generation_process.png")

INITIAL_CODE = """
import pandas as pd
from sdv.metadata import SingleTableMetadata

rpad_data = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=rpad_data)
#st.write(metadata.to_dict()) # instead of print(metadata.to_dict())

"""
##print(metadata.to_dict())
with tab5:
   st.header("Metadata describes the data structure.")
      
      # Spawn a new Ace editor
   code = st_ace(value=INITIAL_CODE,
                 language="python",
                 theme="dracula",
                 placeholder="st.header('Hello world!')")
   st.write(exec(code))

      
   # explain no need to assign dtypes in pandas dataframe -> sdv does thios for you
   with st.expander(label="Complete code example:", expanded=False):
     st.code("""
     from sdv.metadata import SingleTableMetadata
   
     metadata = SingleTableMetadata()
     metadata.detect_from_dataframe(data=rpad_df)

     str_col = ['Sex', 'Management', 'Severity']
     int_col = ['Length_of_Stay', 'Alvarado_Score', 'Paedriatic_Appendicitis_Score']
     float_col = ['Age', 'BMI', 'Height', 'Weight']
     
     for col in rpad_df:
         if col in int_col:
             metadata.update_column(
             column_name=col,
             sdtype='numerical',
             computer_representation='Int64')
         elif col in float_col:
             metadata.update_column(
             column_name=col,
             sdtype='numerical',
             computer_representation='Float')

     metadata.update_column(
         column_name='ID',
         sdtype='id',
         regex_format='[0-9]{4}')
     """, 
     language="python")


INITIAL_CODE_COMPLIANCE = """
import pandas as pd
df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

def calculate_bmi(weight_col, height_col):
   return weight_col/(height_col/100)**2

df['valid_check'] = round(df['BMI'],0) == round(calculate_bmi(df['Weight'], df['Height']),0)
#st.write(df['valid_check'].sum())
#st.write(df.shape)

"""  

INITIAL_CODE_CONSTRAINS = """
import pandas as pd
import json

from sdv.single_table import CTGANSynthesizer
from sdv.metadata import SingleTableMetadata

# import calculate_bmi

df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

def calculate_bmi(weight, height):
   return weight/(height/100)**2

df.drop(df[round(df['BMI'],0) != round(calculate_bmi(df['Weight'], df['Height']),0)].index, inplace=True)

with open('metadata_file.json') as f:
   metadata = SingleTableMetadata.load_from_dict(json.load(f))

model = CTGANSynthesizer(metadata)
model.load_custom_constraint_classes(
    filepath='example_custom_constraint.py',
    class_names=['BMI_Formulae']
)

bmi_constraint = {
    'constraint_class': 'BMI_Formulae',
    'constraint_parameters': {
        'column_names': ['BMI', 'Weight', 'Height']
    }
}

model.add_constraints([bmi_constraint])

# model.fit(df)
# st.write(model.sample(num_rows=10))

"""

CODE_BMI = """
def calculate_bmi(weight, height):
   return round(weight/(height/100)**2,0)

st.write(calculate_bmi(37,148))
"""
# beispiel überdenken
with tab6:
   st.header("Custom constraints help the model learn the value distributions within columns.")
   with st.expander(label="Checking for Constraints", expanded=True):
      col_a, col_b = st.columns(2)

      with col_a:
         rpad_df = get_data()
         st.dataframe(rpad_df[["Height", "Weight", "BMI"]][0:3])
      with col_b:
         code = st_ace(value=CODE_BMI,
                        language="python",
                        placeholder=""
                        )
    
         st.write(exec(code))

   
   with st.expander(label="Check compliance in the data", expanded=True):
       code = st_ace(value=INITIAL_CODE_COMPLIANCE,
                        language="python",
                        placeholder="import streamlit st.header('Hello world!')"
                        )
    
       st.write(exec(code))
   with st.expander(label="Define Custom Constraints in a example_custom_constraints.py File: ", expanded=False):
       with open("example_custom_constraint.py", "r") as f: #/home/antonia/code/Unlocking-Information/
          initial_code = f.read()
       st.code(str(initial_code), language="python")

   with st.expander(label="Load and Append Custom Constraint to Synthesizer", expanded=False):
       code = st_ace(value=INITIAL_CODE_CONSTRAINS,
                        language="python",
                        placeholder="import streamlit st.header('Hello world!')"
                        )
    
          
       st.write(exec(code))


with tab7:
   st.write("test")