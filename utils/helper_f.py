import matplotlib.pyplot as plt
import streamlit as st
from sdmetrics.reports.single_table import DiagnosticReport, QualityReport


# Create a circle at the center of the plot
def plot_circle(names, size, colors):
    my_circle = plt.Circle((0, 0), 0.7, color="white")
    plt.pie(size, labels=names, labeldistance=0.45, colors=colors)
    p = plt.gcf()
    p.gca().add_artist(my_circle)
    plt.show()


def st_write_code_from_file(file_name, expanded=True, *args, **kwargs) -> None:
    with st.expander(label=f" {file_name}", expanded=expanded):
        with open(f"/home/antonia/code/Unlocking-Information/{file_name}") as f:
            st.code(f.read(), *args, **kwargs)


def load_reports(folder_name=""):
    diagnostic_report = DiagnosticReport.load(
        f"pages/evaluation/{folder_name}/results/diagnostic_report.pkl"
    )
    report_q = QualityReport.load(
        f"pages/evaluation/{folder_name}/results/quality_report.pkl"
    )
    return diagnostic_report, report_q


def get_image_paths(folder_name=""):
    path_len_of_height_plt = (
        f"""pages/evaluation/{folder_name}/images/col_plot_height.png"""
    )

    path_len_of_sex_plt = f"""pages/evaluation/{folder_name}/images/col_plot_sex.png"""

    path_col_shapes_plt = f"""pages/evaluation/{folder_name}/images/col_shapes.png"""

    path_age_height_plt = (
        f"""pages/evaluation/{folder_name}/images/Weight_Height_pair_plot.png"""
    )

    path_mng_severity_plt = (
        f"""pages/evaluation/{folder_name}/images/Severity_Management_pair_plot.png"""
    )

    return (
        path_len_of_height_plt,
        path_len_of_sex_plt,
        path_col_shapes_plt,
        path_age_height_plt,
        path_mng_severity_plt,
    )


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def local_css_from_str(file_name_list):
    css_details = " ".join(file_name_list)
    st.markdown(f"<style>{css_details}</style>", unsafe_allow_html=True)


str_css = """
section[data-testid="stSidebar"][aria-expanded="true"] {
    width: 10% !important;
}

section[data-testid="stSidebar"][aria-expanded="false"] {
    width: 10% !important;
}

.block-container {
    max-width: 1000px;
    padding-top: 5rem;
    padding-bottom: 0rem;
    padding-left: 1rem;
    padding-right: 1rem;
}
"""

str_selectbox_text = """
div[data-testid="stExpander"] div[role="button"] p {
    font-size: 1.5rem;
}
"""
