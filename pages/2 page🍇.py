import streamlit as st

st.markdown("# Page 3 🍇")
st.sidebar.markdown("# Page 3 🍇")

st.write(""" outline: (5 min)
1. evaluating synthetic data metrik dashboard anzeigen mit jeweils highlighten was du brauchst
(metriken einzeln durchgehen und erklären) -> simple metriken (software testing)
2. advanced metriken für utility und statostische ähnlichkeit -> auf verschiedene modelle eingehen
3. wissenschafts outlook -> zusammenfassen was es über sdv hinaus gibt -> dashboard was das zeigt
""")

option = st.selectbox(
    'How would you like to be contacted? ',
    ('Email', 'Home phone', 'Mobile phone'))

st.write('You selected:', option)

st.write(st.session_state["shared"])
