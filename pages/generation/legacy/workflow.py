import streamlit as st
import os
import fixed_params as fp
from utils.html_factory import make_img, st_write_bs4
from utils.helper_f import st_write_code_from_file



st.header("Workflow")
st.title("The Training Pipeline")

script_col, pipeline_col = st.columns([2, 1])

with script_col:
    with st.expander(label="💻 Download dataset", expanded=False):
        st.code(
            """
        wget https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip -O cats_and_dogs_filtered.zip
        unzip cats_and_dogs_filtered.zip -d data/raw
        rm cats_and_dogs_filtered.zip
            """,
            language="bash",
        )

    #st_write_code_from_file(code_filepath=os.path("playground.py"), language="python", expanded=False)
    with st.expander(label="playground.py", expanded=False):
        with open(f"/home/antonia/code/Unlocking-Information/playground.py", "r") as f:
            st.code(f.read())

    st.write("🚀 **Added pipeline and parameters path:**")
    #st_write_code_from_file(code_filepath=PIPELINE_PATH, language="yaml", expanded=False)
    #st_write_code_from_file(code_filepath=PARAMS_PATH, language="yaml", expanded=False)

with pipeline_col:
    st_write_bs4(make_img(src=fp.IMAGES_DIR / "Synthetic_Data_generation_process.svg"))