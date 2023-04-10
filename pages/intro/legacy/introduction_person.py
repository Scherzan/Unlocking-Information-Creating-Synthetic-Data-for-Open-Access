import streamlit as st

from fixed_params import AUTHOR, IMAGES_DIR

import streamlit as st

col_a, col_b, col_c = st.columns(3)

with col_a:
    st.write("### Installation and Usage")

    st.code("pip install streamlit", language="bash")
    st.code("streamlit run streamlit_demo.py", language="bash")
    st.code("import streamlit as st", language="python")

    st.write("### Display")

    st.code('st.write("Hello 👋")', language="python")
    st.code('st.latex("e^{i\pi} + 1 = 0")', language="python")
    st.code('st.markdown("**Mark**_down_")', language="python")

    st.write("### Display Media")
    st.code('st.image("https://http.cat/200")')
    st.code("st.audio(...)")
    st.code("st.video(...)")

with col_b:
    st.write("### Display data")
    st.code('st.json({"foo": "bar", "fu": "ba"})')
    st.code(
        """
df = pd.DataFrame({
    "name": ["Alice", "Bob", "Cathy"],
    "age": [20, 31, 42],
}).assign(older_than_30=lambda df: df.age > 30)
st.dataframe(df)
    """
    )
    st.code('st.metric("My metric", 42, 2)')

    st.write("### Interactive widgets")
    st.code(
        """
cat_or_dog = st.selectbox(
    label="Pick one",
    options=["cats", "dogs"],
)
st.write("You selected:", cat_or_dog)
    """
    )
    st.code(
        """
chosen_value = st.slider('Pick a number', 0, 100)
st.write("You selected:", chosen_value)
    """
    )
    st.code(
        """
img = st.file_uploader("Upload an image")
if img:
    st.image(img, caption="The pic you Uploaded !")
    """
    )
    st.code(
        """
img = st.camera_input("Take a picture")
if img:
    st.image(img, caption="The pic you just took !")
    """
    )

with col_c:
    st.write("### ⭐ Demo !")

    with st.expander("### ⭐ Demo (click to see the code)", expanded=False):
        st.code(
            """
st_code = st.text_area("Enter streamlit code:")
try:
    exec(st_code)
except Exception as e:
    st.error(f"Error: {e}")
        """
        )

    st_code = st.text_area(label="Enter streamlit code:", height=280)
    try:
        exec(st_code)
    except Exception as e:
        st.error(f"Error: {e}")



#col_a, _, col_b = st.columns([5, 1, 5])
#
#with col_a:
#    st.markdown("## About me 🙋‍♀️")
#    st.write(f"I am {AUTHOR}")
#    st.write("based in Berlin, ")
#    st.write("fun fact")
#
#    #TWITTER = make_div()
#    #TWITTER.extend(
#    #    [
#    #        make_img(src=IMAGES_DIR / "twitter-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
#    #        make_div(text="@AntoineToubhans", style=CSSStyle(display="inline")),
#    #    ]
#    #)
#    #st_write_bs4(TWITTER)
##
#    #LINKEDIN = make_div()
#    #LINKEDIN.extend(
#    #    [
#    #        make_img(src=IMAGES_DIR / "linkedin-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
#    #        make_div(text="/antoine-toubhans", style=CSSStyle(display="inline")),
#    #    ]
#    #)
#    #st_write_bs4(LINKEDIN)
##
#    #GITHUB = make_div()
#    #GITHUB.extend(
#    #    [
#    #        make_img(src=IMAGES_DIR / "github-logo.png", style=CSSStyle(height="30px", margin="0 5px 5px 0")),
#    #        make_div(text="/AntoineToubhans", style=CSSStyle(display="inline")),
#    #    ]
#    #)
#    #st_write_bs4(GITHUB)
#
#with col_b:
#    st.write("Dummz")
#    #st.image(IMAGES_DIR / "PyConDE_PyDataBer_circle_trans_500.png")
#    #ME_IMG = make_img(
#    #    src=IMAGES_DIR / "moi.jpeg",
#    #    style=CSSStyle(
#    #        width="50%",
#    #        border_radius="50%",
#    #        margin_bottom="40px",
#    #    ),
#    #)
#    #st_write_bs4(ME_IMG)
#
#col_c, _, col_d = st.columns([5, 1, 5])
#
#with col_c:
#    st.markdown("### About my Work:")
#    st.write("in Berlin, for")
#    st.image(str(IMAGES_DIR / "PyConDE_PyDataBer_circle_trans_500.png"), width=200)
#
#with col_d:
#    st.markdown("### About Me")
#    st.write("- Background in Economics and Information Systems")
#    st.write("- 👨‍💻 Consultant - ML-Engineer")
#    st.write("- Topics Synthetic Data and (ML)-Tools for Public Administrations")
#    st.write("- Intrest in Data Science for Public Good")
#
#