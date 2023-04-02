import streamlit as st
from streamlit_extras.echo_expander import echo_expander

st.markdown("# Generate better Data")
st.sidebar.markdown("# Better Data")

st.write(""" outline: (5 min)
1. evaluating synthetic data metrik dashboard anzeigen mit jeweils highlighten was du brauchst
(metriken einzeln durchgehen und erklären) -> simple metriken (software testing)
2. advanced metriken für utility und statostische ähnlichkeit -> auf verschiedene modelle eingehen
3. wissenschafts outlook -> zusammenfassen was es über sdv hinaus gibt -> dashboard was das zeigt
""")

with echo_expander(code_location="below", label="Working with Metdata"):
    # load dependencies
    import pandas as pd
    #from sdv.lite import SingleTablePreset
    from sdv.single_table import CTGANSynthesizer
    from sdv.metadata import SingleTableMetadata
    
    # read data
    rpad_df = pd.read_excel(r'RPAD_data_small.xlsx', engine='openpyxl')
    
    # create metadata
    metadata = SingleTableMetadata()
    metadata.detect_from_dataframe(data=rpad_df)
    
with echo_expander(code_location="below", label="Show Metdata"):
    python_dict = metadata.to_dict()

st.write(list(python_dict.items())[:5])


with echo_expander(code_location="below", label="Modify Metadata"):
    from sdv.evaluation.single_table import evaluate_quality

    # ⚡ 📣 Specify SDV Metadata 📣 ⚡
    int_col = ['ID', 'Length_of_Stay', 'Alvarado_Score', 'Paedriatic_Appendicitis_Score']
    float_col = ['Age', 'BMI', 'Height', 'Weight']
    
    for col in rpad_df:
        if col in int_col:
            # explain no needed to assign dtypes
            metadata.update_column(
            column_name=col,
            sdtype='numerical',
            computer_representation='Int64')
        elif col in float_col:
            #rpad_df[col] = rpad_df[col].astype('float')
            metadata.update_column(
            column_name=col,
            sdtype='numerical',
            computer_representation='Float')

python_dict = metadata.to_dict()
st.write(list(python_dict.items())[:5])

with echo_expander(code_location="below", label="Train with new Metadata"):    
    # initialize and train model
    model = CTGANSynthesizer(
        metadata,
        #name='FAST_ML'
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

st.markdown("### What does the data look like? 👀")
st.write(synth_rpad.head(5))


#with echo_expander(code_location="below", label="Get Column Metrics"):    
#    
#    # get column metrics
#    fig_col_shapes = quality_report.get_visualization('Column Shapes')
#
#st.image('col_shapes.png')

st.markdown("### Let's check Length_of_Stay again")
st.image('Length_of_Stay.png')
