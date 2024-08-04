import streamlit as st

from utils.helper_f import local_css_from_str, str_css

local_css_from_str([str_css])

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "Our project learnings.💡",
        "So far so good. ✅",
        "Where to go next? 🧭",
        "Thank you. 💛",
    ],
)

with tab1:
    st.markdown("### Common issues in public sector applications")
    no_ds_team = st.checkbox("No in-house data science team")
    if no_ds_team:
        text = """
        That is ok, we can help. Still it would
        be ideal to build some expertise in the long run.
        """
        st.markdown(f'<p style="color:#1f449c">{text}</p>', unsafe_allow_html=True)

    no_data_access = st.checkbox("""No access to data
                                 due to privacy regulations""")
    if no_data_access:
        text_2 = """
        Not good, would be much easier with direct access.
        We can think about docker solutions or limited access
        to only small subsets for small group of people.
        """
        st.markdown(f'<p style="color:#1f449c">{text_2}</p>', unsafe_allow_html=True)

    no_hardware = st.checkbox("Know the users")
    if no_hardware:
        text_3 = """
        An absolute must. Make sure to know who the final
        users will be and what they want to use the data for.
        """
        st.markdown(f'<p style="color:#1f449c">{text_3}</p>', unsafe_allow_html=True)

with tab2:
    st.markdown("### Let's reflect on what we heard.")

    no_ds_team = st.checkbox("""We heard about synthetic data
                             and how to generate it.""")
    if no_ds_team:
        text = """
        Yep, quite easy. pip install SDV - load data - feed data into model
        - and use .sample method
        """
        st.markdown(f'<p style="color:#1f449c">{text}</p>', unsafe_allow_html=True)

    no_data_access = st.checkbox("""We looked at metrics and how
                                 to evaluate synthetic data quality.""")
    if no_data_access:
        text_2 = """
        Yes, but only superficially. The presented metrics
        would not be enough for a real world use case.
        """
        st.markdown(f'<p style="color:#1f449c">{text_2}</p>', unsafe_allow_html=True)

    apply = st.checkbox("What should you take with you?")
    if apply:
        t_33 = """3. We need to select our metrics
        and evaluation strategy according to the specific use case."""
        st.markdown(
            f'<p style="color:#1f449c";><strong>{t_33}</strong></p>',
            unsafe_allow_html=True,
        )

with tab3:
    st.markdown("### Where can I find more information?")
    col_a, col_b = st.columns(2)

    with col_a:
        st.write("")
        st.image("images/SDV.png", width=200)

    with col_b:
        st.write("")
        st.write("https://github.com/sdv-dev/SDV")
        st.write("https://docs.sdv.dev/sdv")


with tab4:
    st.markdown(
        """<h2 style='text-align: center; color:#1f449c;'>
                Happy Synthesizing 😃🧪</h2>""",
        unsafe_allow_html=True,
    )
    st.write("")
    st.write("Find me on:")
    st.write(
        "https://github.com/Scherzan/Unlocking-Information-Creating-Synthetic-Data-for-Open-Access",
    )
    st.write("https://www.linkedin.com/in/antonia-scherz-7b4740178")
    st.write("or at the buffet. 😋")
