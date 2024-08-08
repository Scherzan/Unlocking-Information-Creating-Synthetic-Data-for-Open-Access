from sdv.constraints import create_custom_constraint_class


def is_valid(c_names, data):
    bmi = data[c_names[0]]
    weight = data[c_names[1]]
    height = data[c_names[2]]
    true_values = round(bmi, 0) == round(weight / round(height / 100) ** 2, 0)
    false_values = round(bmi, 0) != round(weight / round(height / 100) ** 2, 0)
    return (true_values) | (false_values)


BMI_Formulae = create_custom_constraint_class(is_valid_fn=is_valid)
