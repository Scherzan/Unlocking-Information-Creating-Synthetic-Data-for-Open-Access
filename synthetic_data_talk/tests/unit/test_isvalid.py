import pandas as pd

from synthetic_data_talk.utils.example_custom_constraint import is_valid


def test_is_valid():
    test_data = {
        "bmi": [97, 97],
        "height": [60, 60],
        "weight": [35, 35],
    }

    data = pd.DataFrame.from_dict(test_data)

    calculation = is_valid(["bmi", "height", "weight"], data)

    assert calculation.all()
