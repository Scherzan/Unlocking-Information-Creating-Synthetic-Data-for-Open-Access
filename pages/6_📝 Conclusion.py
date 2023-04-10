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

tab1, tab2, tab3, tab4 = st.tabs(["Recap", "Where to go?", "Keep in mind", "Thank you"])

with tab1: 
   st.write("Recap")

with tab2: 
   st.write("Where to go?")

with tab3: 
   st.write("Keep in mind")

with tab4: 
   st.write("Thank you")