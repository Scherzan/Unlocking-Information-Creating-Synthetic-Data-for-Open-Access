import matplotlib.pyplot as plt
import streamlit as st
from sdmetrics.reports.single_table import QualityReport
from sdmetrics.reports.single_table import DiagnosticReport
 
# Create a circle at the center of the plot
def plot_circle(names, size, colors):
   my_circle = plt.Circle( (0,0), 0.7, color='white')
   plt.pie(size, labels=names, labeldistance=0.45, colors=colors)
   p = plt.gcf()
   p.gca().add_artist(my_circle)
   plt.show()

def st_write_code_from_file(file_name, expanded = True, *args, **kwargs) -> None:
    with st.expander(label=f" {file_name}", expanded=expanded):
        with open(f"/home/antonia/code/Unlocking-Information/{file_name}", "r") as f:
            st.code(f.read(), *args, **kwargs)

def load_reports(folder_name = ""):
    diagnostic_report = DiagnosticReport.load(f"pages/evaluation/{folder_name}/results/diagnostic_report.pkl")
    report_q = QualityReport.load(f"pages/evaluation/{folder_name}/results/quality_report.pkl")
    return diagnostic_report, report_q

def get_image_paths(folder_name = ""):
    path_len_of_stay_plt = f"pages/evaluation/{folder_name}/images/col_plot_len_stay.png"
    path_col_shapes_plt = f"pages/evaluation/{folder_name}/images/col_shapes.png"
    path_age_height_plt = f"pages/evaluation/{folder_name}/images/Age_Height_pair_plot.png"
    return path_len_of_stay_plt, path_col_shapes_plt, path_age_height_plt