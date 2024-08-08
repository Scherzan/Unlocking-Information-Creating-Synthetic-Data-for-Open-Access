import streamlit as st
from utils.helper_f import local_css_from_str, str_css, str_selectbox_text

# Load local CSS Style
local_css_from_str([str_css, str_selectbox_text])

# Define tab labels
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
    [
        "I am",
        "talking about",
        "synthetic data,",
        "when to use it,",
        "why to use it",
        "and how to generate it.",
    ],
)

# Tab 1: About Me
with tab1:
    col_a, col_b = st.columns(2)

    with col_a:
        st.write("### This is Me")
        st.write(
            """
        🏷️: Antonia Scherz \n
        🏠: Berlin \n
        🏢: PD - Berater der öffentlichen Hand \n
        🧭: Consultant/Data Scientist \n
        """,
        )
        st.image("images/anto_scherz.jpg")
        st.write(
            """LinekdIn:
                 [https://www.linkedin.com/in/antonia-scherz-7b4740178](%s)" %
                 "https://www.linkedin.com/in/antonia-scherz-7b4740178""",
        )

    with col_b:
        st.write("### Project experience:")

        st.write(
            """
        🪄 prototyping ml-applications and exploring their value
                 for the public sector \n
        🪄 synthesize public administration data for scientific use
        """,
        )

# Tab 2: Introduction
with tab2:
    st.markdown("### We will be looking at synthetic tabular data.")
    st.text("")
    st.write("📋 Demo exercise on how to generate and evaluate data.")
    st.text("")
    st.write("📊 Overview on metrics and evaluation strategies.")
    st.text("")
    st.write("❗Learnings from our synthetic data project")

# Tab 3: Value of Synthetic Data
with tab3:
    st.markdown(
        """### Synthetic data aims to remove any identifiable
                personal information from the dataset.""",
    )
    st.write(
        "<style>div.block-container{padding-top:2rem;}</style>",
        unsafe_allow_html=True,
    )
    st.image("images/rd_to_std.png", width=650)

# Tab 4: Use Cases
with tab4:
    with st.expander(label="What is Synthetic Data used for?", expanded=False):
        st.write("... as an alternative to real data.")
        st.write("... for (predictive) analysis.")
        st.write("... for software testing.")

# Tab 5: Difference Anonymization
with tab5:
    st.markdown(
        """### Synthetic data differs from anonymization
                in that it retains the original data.""",
    )
    st.image("images/bilder_anon.png")

# Tab 6: Generating Synthetic Data
with tab6:
    st.markdown("### One needs real data to generate synthetic data models.")
    st.image("images/generation.png", width=700)
