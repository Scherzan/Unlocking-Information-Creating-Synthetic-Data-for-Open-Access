import streamlit as st

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.write(""" outline: (5 min)
1. creating synthetic data -> notebook style ->
2. first tips and tricks when using data
3. advanced tricks adjusting to customized needs 
-> visuals zeigen eine metric - und wie sich diese verbessert bei implementierung der tricks
""")
         
# messgaes going through notebook:
# creating super simple -> creating good the issue
# demonstrate simplicity -> go from there -> want float 2 point etc ->


age = st.slider('How old are you? ❤️', 0, 130, 25)
st.write("I'm ", age, 'years old')


