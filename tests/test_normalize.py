import pandas as pd

from tools.normalize_settings import (
    classify_row,
    RowType,
)


def test_setting_row():

    row = pd.Series([
        "Y1029",
        "949.556 - 955.964",
        "956.425 - 962.541",
        "962.963 - 968.753",
        "59",
    ])

    assert classify_row(row) == RowType.SETTING
    
    
def test_order_row():

    row = pd.Series([
        "",
        "965.933 - 972.448",
        "972.924 - 979.130",
        "979.573 - 985.463",
        "58",
    ])

    assert classify_row(row) == RowType.ORDER
    
    
def test_metadata_row():

    row = pd.Series([
        "Published on:",
        "",
        "",
        "",
        "",
    ])

    assert classify_row(row) == RowType.METADATA


if __name__ == "__main__":

    test_setting_row()
    test_order_row()
    test_metadata_row()

    print("All tests passed.")
