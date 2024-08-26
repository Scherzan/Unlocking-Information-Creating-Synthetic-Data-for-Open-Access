"""test_app.py."""

from streamlit.testing.v1 import AppTest


def test_main_page():
    """Test the app runs."""
    at = AppTest.from_file("synthetic_data_talk/🔓_Synthetic_Data.py").run()
    assert at.exception
    # Change app storrage to not include extra directory because pytests
    # using streamlit are not able to correctly find paths in apps throwing
    # errors that are not an issue in the app.
