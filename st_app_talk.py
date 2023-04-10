import streamlit as st
import fixed_params as fp



# Streamlit webpage properties
st.set_page_config(
    page_title=fp.CONFERENCE_NAME,
    page_icon=str(fp.CONFERENCE_LOGO_PATH),
    layout="wide",
)


st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
    </style>""", unsafe_allow_html=True)



