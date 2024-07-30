
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_ace import st_ace
from utils.helper_f import local_css_from_str, str_css

# Load local CSS styles
local_css_from_str([str_css])

# Create tabs
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs(["Use real data","choose a model",                                              
                                              "to create",
                                              "synthetic data",
                                              "And now",
                                              "Describe the data",
                                              "better",
                                              "and tune it"])

# Cached data loading functions
@st.cache_data(persist=True)
def get_data():
    rpad_df = pd.read_excel(r'data/RPAD_data_small.xlsx', engine='openpyxl')
    rpad_df.rename(columns={'Paedriatic_Appendicitis_Score': 'PA_Score'},
                   inplace=True)
    return rpad_df


@st.cache_data(persist=True)
def get_synt_data():
    rpad_synth = pd.read_csv("data/synthetic_rpad.csv")
    rpad_synth.rename(columns={'Paedriatic_Appendicitis_Score': 'PA_Score'},
                      inplace=True)
    return rpad_synth


# Load data
rpad_synth = get_synt_data()
rpad_df = get_data()


# Display data visualization and summary
with tab1:

    st.markdown("### Regensburg Pediatric Appendicitis Dataset")
    dtypes_df = rpad_df.dtypes.value_counts().to_frame('dtypes').reset_index()
    names = dtypes_df['index']
    dtype_category = dtypes_df['dtypes']
    colors = ['#cb6ce6', '#8c52ff', '#ff66c4']

    # Organize slide in columns
    col_a, col_b = st.columns(2)

    with col_a:
        # Pie Chart for Data Types
        fig, ax = plt.subplots()
        my_circle = plt.Circle( (0,0), 0.7, color='white')
        ax.pie(dtype_category, labels=names, labeldistance=0.45, colors=colors)
        ax.add_artist(my_circle)
        st.pyplot(fig) 
        st.write(f'data shape: {rpad_df.shape}')

    with col_b:
        # Display missing values in table
        df_info = rpad_df.isna().sum().to_frame('Missings').reset_index()
        df_info.index.set_names(['Column'])
        st.table(df_info)

    st.write(rpad_df.style.format(subset=['Age', 'BMI','Height', 'Weight',
                                          'Length_of_Stay', 'Alvarado_Score',
                                          'PA_Score'], formatter="{:.2f}")) 

# Display SDV matrix on model types
with tab2:
    st.markdown("### What model choices do I have?")
    st.image("images/models.png")

# Code to generate synthetic data
with tab3:
    st.markdown("### Model and Code Workflow")
    with st.expander(label="Conditional Tabular GAN Model", expanded=True):
        st.image("images/ctgan_architecure.png")
    with st.expander(label="default.py", expanded=False):
        with open("utils/default.py", "r") as f:
            st.code(f.read())

# Display synthetic data
with tab4:
    st.markdown("### Synthetic Data")
    st.write(rpad_synth.style.format(subset=['Age', 'BMI',
                                             'Height', 'Weight',
                                             'Length_of_Stay',
                                             'Alvarado_Score',
                                             'PA_Score'],
                                     formatter="{:.2f}"))

with tab5:
    st.markdown("### How close are the synthetic samples to reality?")
    st.image("images/evaluation.png")

INITIAL_CODE = """
import pandas as pd
from sdv.metadata import SingleTableMetadata

rpad_data = pd.read_excel(r'data/RPAD_data_small.xlsx', engine='openpyxl')
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=rpad_data)
#st.write(metadata.to_dict()) # instead of print(metadata.to_dict())

"""

with tab6:
    st.header("Metadata describes the data structure.")

    # Spawn a new Ace editor
    code = st_ace(value=INITIAL_CODE,
                  language="python",
                  placeholder="st.header('Hello world!')")
    st.write(exec(code))

    # explain SDV assigns dtypes automatically
    with st.expander(label="Adapt metadata code example:", expanded=False):
        st.code("""
        from sdv.metadata import SingleTableMetadata

        metadata = SingleTableMetadata()
        metadata.detect_from_dataframe(data=rpad_df)

        metadata.update_column(
            column_name='ID',
            sdtype='id',
            regex_format='[0-9]{4}')
        """,
                language="python")


INITIAL_CODE_CONSTRAINS = """

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

"""

# beispiel überdenken
with tab7:
    st.header("""Custom constraints help the model learn the distributions
              of values within columns.""")
    with st.expander(label="Checking for constraints", expanded=True):
        col_a, col_b = st.columns(2)

        with col_a:
            rpad_df = get_data()
            st.dataframe(rpad_df[["Height", "Weight", "BMI"]][0:3])
        with col_b:
            st.code("weight/(height/100)**2", language="python")

    with st.expander(label="""Define custom constraints
                     in an example_custom_constraints.py
                     file: """,
                     expanded=False):
        with open("utils/example_custom_constraint.py", "r") as f:
            initial_code = f.read()
        st.code(str(initial_code), language="python")

    with st.expander(label="Load and append custom constraint to synthesizer",
                     expanded=False):
        st.code(INITIAL_CODE_CONSTRAINS, language="python")

with tab8:
    st.markdown("### What else can we do to improve?")
    st.button("Tune hyperparameters")
    st.button("Modify data transformation before training")
    st.button("Anonymize sensitive data")
    st.button("Define distribution of columns")
    st.button("Use conditions when sampling")
