import streamlit as st
from streamlit_extras.echo_expander import echo_expander

st.markdown("# Generate Synthetic Data")
st.sidebar.markdown("# Generate Synthetic Data")
st.sidebar.markdown("## Get Started")
st.sidebar.markdown("## Tips and Tricks")

st.write(""" outline: (5 min)
1. creating synthetic data -> notebook style ->
2. first tips and tricks when using data
3. advanced tricks adjusting to customized needs 
-> visuals zeigen eine metric - und wie sich diese verbessert bei implementierung der tricks
""")
         
# messgaes going through notebook:
# creating super simple -> creating good the issue
# demonstrate simplicity -> go from there -> want float 2 point etc ->

st.markdown("## Get Started")

with echo_expander(code_location="below", label="Simple Dataframe example"):
    # load dependencies
    import pandas as pd
    from sdv.lite import SingleTablePreset
    from sdv.metadata import SingleTableMetadata
    from sdv.evaluation.single_table import evaluate_quality
    
    # read data
    rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')

st.write(rpad_df.head(5))

with echo_expander(code_location="below", label="Create synthetic verison"):    
    # create metadata
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=rpad_df)
    
    # initialize and train model
    model = SingleTablePreset(
        metadata,
        name='FAST_ML'
    )
    model.fit(rpad_df)
    
    # create synthetic data
    synth_rpad = model.sample(num_rows=200)
    
    # get initial evaluation score
    quality_report = evaluate_quality(
        rpad_df,
        synth_rpad,
        metadata
    )

st.write(f'Overall Quality Score: {round(quality_report.get_score() * 100, 2)}%\n')
st.write(f'Properties:  \n Columns Shapes: {round(quality_report.get_properties().iloc[0]["Score"] * 100, 2)}%  \n',
         f'Column Pair Trends: {round(quality_report.get_properties().iloc[1]["Score"] * 100, 2)}%\n') 

st.markdown("### What does the data look like? 👀")
st.write(synth_rpad.head(5))

with echo_expander(code_location="below", label="Get Column Metrics"):    
    
    # get column metrics
    fig_col_shapes = quality_report.get_visualization('Column Shapes')

st.image('col_shapes.png')

with echo_expander(code_location="below", label="Compare Distributions Columnwise"):    
    from sdv.evaluation.single_table import get_column_plot

    # compare distributions on columns
    fig = get_column_plot(
        real_data=rpad_df,
        synthetic_data=synth_rpad,
        column_name='Management',
        metadata=metadata
    )
    #fig.show()

st.image('rvss_management.png')

st.markdown("### Let's check a numeric variable")
st.image('Length_of_Stay.png')










