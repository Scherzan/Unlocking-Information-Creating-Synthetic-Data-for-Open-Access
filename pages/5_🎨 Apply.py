import streamlit as st

st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
    </style>""", unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Common Issues", "Users Setting", "Your Setting"])

with tab1:
    st.write("Common Issues in Public Sector Applications")
    no_ds_team = st.checkbox("No in-house data science team.")
    no_data_access = st.checkbox("Cannot provide access to data due to privacy regulations.")
    no_hardware = st.checkbox("No GPUs available.")
    # implanced data, privacy concerns, quality for general purpose data

if no_ds_team:
    st.write("""
    That's ok, we can help. Still it would be ideal 
    to build some expertise in the long run. 
    """)

if no_data_access:
    st.write("""
    Not Good, would be much easier with direct access. 
    We can think about docker solutions or limited access 
    to only small subsets for small group of people.
    """)

if no_hardware:
    st.write("""
    Not acceptable for most cases. 
    Often public administrations cannot use common cloud solutions.
    At the same time they do not have sufficent infrastructure for training ml-models.
    Most cases a continious service to offer synthetic versions of new incoming data.
    Without hardware models cannot train and generate data efficiently. 
    Therefore GPU-Support is a necessary requirement for all synthetic data services.
    """)