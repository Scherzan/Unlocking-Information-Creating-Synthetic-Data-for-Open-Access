from functools import partial
from typing import Literal

import streamlit as st
from bs4 import BeautifulSoup

TAG = Literal["div", "a", "span", "img"]


class CSSStyle:
    """Enforce custom styling defined in CSS code."""

    def __init__(self, **kwargs):
        """_Initiate Class to set custom CSS styles."""
        for key, value in kwargs.items():
            setattr(self, self._format_css_key(key), value)

    def _to_str(self):
        """Turn parametrized statements into plain string for streamlit.

        to evaluate and render in app UI.

        Returns
        -------
            _type_: string with custom css code for adapted style elements.

        """
        return "; ".join([f"{key}: {value}" for key, value in self.__dict__.items()])

    __str__ = __repr__ = _to_str

    @staticmethod
    def _format_css_key(key):
        """Handle underscore in css format statements.

        Args:
        ----
            key (str): Variable with string value for intendet format specifications.

        Returns:
        -------
            str: string value with underscore replaced with hyphen

        """
        return key.replace("_", "-")


def make_tag(
    name: TAG,
    style: CSSStyle | None = None,
    text: str | None = None,
) -> BeautifulSoup:
    new_tag = (
        BeautifulSoup().new_tag(name, style=str(style))
        if style
        else BeautifulSoup().new_tag(name)
    )

    if text:
        new_tag.append(text)

    return new_tag


make_div = partial(make_tag, name="div")


def st_write_bs4(soup: BeautifulSoup):
    st.write(soup.__repr__(), unsafe_allow_html=True)
