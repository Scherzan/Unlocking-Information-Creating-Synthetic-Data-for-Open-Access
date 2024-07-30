import utils.fixed_params as fp
from utils.html_factory import CSSStyle, make_div, st_write_bs4

# Title
TITLE_P1 = "Unlocking Information 🔓 Creating Synthetic Data for Open Access"

BIG_TITLE_STYLE = CSSStyle(
    text_align="center",
    font_size="48px",
    line_height="58px",
    margin="20px 60px 10px 10px",
    font_weight=600,
)
BIG_TITLE_DIV = make_div(style=BIG_TITLE_STYLE)
BIG_TITLE_DIV.extend(
    [
        make_div(text=TITLE_P1)
    ]
)

# Author
AUTHOR_STYLE = CSSStyle(
    text_align="center",
    font_size="36px",
    line_height="36px",
    font_style="italic",
    margin_bottom="28px",
)
AUTHOR_DIV = make_div(style=AUTHOR_STYLE, text=fp.AUTHOR)


# main
def st_write_title():
    st_write_bs4(BIG_TITLE_DIV)
    st_write_bs4(AUTHOR_DIV)
    
