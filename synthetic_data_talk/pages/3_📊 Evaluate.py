import json
from pathlib import Path

import pandas as pd
import streamlit as st
from sdv.metadata import SingleTableMetadata
from sdv.single_table import CTGANSynthesizer
from streamlit_echarts import st_pyecharts
from utils.chart_metrics import c
from utils.helper_f import get_image_paths, load_reports, local_css_from_str, str_css

local_css_from_str([str_css])


@st.cache_data
def get_eval_utils(
    synth_data_path="synthetic_rpad.csv",
    model_path="rpad_ep500_dsteps5.pkl",
    metadata_file="metadata_file.json",
):
    rpad_df = pd.read_excel(r"RPAD_data_small.xlsx", engine="openpyxl")
    rpad_synth = pd.read_csv(synth_data_path)
    model = CTGANSynthesizer.load(model_path)
    with Path.open(metadata_file) as f:
        metadata_dict = json.load(f)
    metadata = SingleTableMetadata.load_from_dict(metadata_dict)
    return rpad_df, rpad_synth, model, metadata


st.sidebar.title(":memo: Choose eval case")

with st.sidebar:
    genre = st.radio(
        "Synthetic data",
        ("default", "with metadata", "with constraints", "with tuning", "best setting"),
    )

    if genre == "default":
        diagnostic_report, report_q = load_reports("default")
        (
            path_len_of_height_plt,
            path_len_of_sex_plt,
            path_col_shapes_plt,
            path_age_height_plt,
            path_mng_severity_plt,
        ) = get_image_paths("default")
    if genre == "with metadata":
        diagnostic_report, report_q = load_reports("metadata")
        (
            path_len_of_height_plt,
            path_len_of_sex_plt,
            path_col_shapes_plt,
            path_age_height_plt,
            path_mng_severity_plt,
        ) = get_image_paths("metadata")
    if genre == "with constraints":
        diagnostic_report, report_q = load_reports("constraints")
        (
            path_len_of_height_plt,
            path_len_of_sex_plt,
            path_col_shapes_plt,
            path_age_height_plt,
            path_mng_severity_plt,
        ) = get_image_paths("constraints")
    if genre == "with tuning":
        diagnostic_report, report_q = load_reports("tuning")
        (
            path_len_of_height_plt,
            path_len_of_sex_plt,
            path_col_shapes_plt,
            path_age_height_plt,
            path_mng_severity_plt,
        ) = get_image_paths("tuning")
    if genre == "best setting":
        diagnostic_report, report_q = load_reports("best_setting")
        (
            path_len_of_height_plt,
            path_len_of_sex_plt,
            path_col_shapes_plt,
            path_age_height_plt,
            path_mng_severity_plt,
        ) = get_image_paths("best_setting")

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Many Metrics",
        "guide your SD evaluation",
        "e.g. statistical indicators",
        "and visual inspections.",
    ],
)

with tab1:
    st.markdown("### What metrics are there?")
    st.markdown(
        """###### Overview by Hernandez et al. 2021 \
                Standardised Metrics and Methods for \
                Synthetic Tabular Data Evaluation; TechRxiv; (edited)""",
    )
    st_pyecharts(c, height=500)

with tab2:
    st.markdown("### Evaluation strategy")
    st.image("images/eval_strategy.png")

with tab3:
    with st.expander(
        label="""SDV Quality Report includes statistical tests
                     and correlation analysis.""",
        expanded=True,
    ):
        st.write(report_q.get_score())
        st.write(report_q.get_properties())

    with st.expander(label="Column Shapes Details", expanded=False):
        st.write(report_q.get_details(property_name="Column Shapes"))

    with st.expander(label="Column Pair Trends", expanded=False):
        st.write(report_q.get_details(property_name="Column Pair Trends"))

with tab4:
    # missing metrics description
    st.markdown("### Visual inspection of single columns:")

    with st.expander(label="Numerical variable plot", expanded=False):
        st.image(path_len_of_height_plt)

    with st.expander(label="Categorical variable plot", expanded=False):
        st.image(path_len_of_sex_plt)

    st.markdown("### Visual inspection of column pairs:")

    with st.expander(label="Plotting 'Weight' and 'Height'", expanded=False):
        st.image(path_age_height_plt)

    with st.expander(label="Plotting 'Management' and 'Severity'", expanded=False):
        st.image(path_mng_severity_plt)
