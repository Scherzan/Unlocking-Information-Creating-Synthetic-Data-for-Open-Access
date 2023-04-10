from sdv.constraints import create_custom_constraint_class



def is_valid(column_names, data):
    # replace with your custom logic
    bmi_column = data[column_names[0]]
    weight_column = data[column_names[1]]
    height_column = data[column_names[2]]
    true_values = round(bmi_column,0) == round(weight_column/round(height_column/100)**2,0)
    false_values = round(bmi_column,0) != round(weight_column/round(height_column/100)**2,0)
    return (true_values) | (false_values)


BMI_Formulae = create_custom_constraint_class(
    is_valid_fn=is_valid
)