import streamlit as st
import utils.fixed_params as fp
from utils.title import st_write_title


# Streamlit webpage properties
st.set_page_config(
    page_title=fp.CONFERENCE_NAME,
    page_icon=str(fp.CONFERENCE_LOGO_PATH),
    initial_sidebar_state="expanded",
    layout="wide"
)


st.markdown("""
    <style>
      section[data-testid="stSidebar"][aria-expanded="true"]{
        width: 10% !important;
      }
      section[data-testid="stSidebar"][aria-expanded="false"]{
        width: 10% !important;
      }
           .css-18e3th9 {
          padding-top: 0rem;
          padding-bottom: 10rem;
          padding-left: 5rem;
          padding-right: 5rem;
      }
      css-1d391kg {
          padding-top: 3.5rem;
          padding-right: 1rem;
          padding-bottom: 3.5rem;
          padding-left: 1rem;
      }
    </style>""", unsafe_allow_html=True)

st_write_title()

col_1, col_2, col_3 = st.columns(3)

with col_2:
    st.image(fp.CONFERENCE_LOGO_PATH, width=200)
