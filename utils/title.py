import fixed_params as fp
from utils.html_factory import CSSStyle, make_div, make_img, st_write_bs4



# Title
TITLE_P1 = "Unlocking Information - "
TITLE_P2 = "Creating Synthetic Data for Open Access."

BIG_TITLE_STYLE = CSSStyle(
    text_align="center",
    font_size="58px",
    line_height="64px",
    margin="40px 80px 60px 80px",
    font_weight=700,
)
BIG_TITLE_DIV = make_div(style=BIG_TITLE_STYLE)
BIG_TITLE_DIV.extend(
    [
        make_div(text=TITLE_P1),
        make_div(text=TITLE_P2),
    ]
)

# Author
AUTHOR_STYLE = CSSStyle(
    text_align="center",
    font_size="48px",
    line_height="48px",
    font_style="italic",
    margin_bottom="40px",
)
AUTHOR_DIV = make_div(style=AUTHOR_STYLE, text="Antonia Scherz")


# Conf Logo
BIG_LOGO_STYLE = CSSStyle(
    text_align="center",
    width="80%",
    margin_left="auto",
    margin_right="auto",
    display="block",
)

BIG_LOGO_IMG = make_img(
    style=BIG_LOGO_STYLE,
    src=fp.CONFERENCE_LOGO_PATH,
)


# main
def st_write_title():
    st_write_bs4(BIG_TITLE_DIV)
    st_write_bs4(AUTHOR_DIV)
    st_write_bs4(BIG_LOGO_IMG)
