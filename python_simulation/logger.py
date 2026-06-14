import os
import pandas as pd

CSV_FILE = "data/energy_log.csv"


def save_row(row):

    if os.path.exists(CSV_FILE):

        df = pd.read_csv(CSV_FILE)

        df = pd.concat(
            [df, pd.DataFrame([row])],
            ignore_index=True
        )

    else:

        df = pd.DataFrame([row])

    df.to_csv(
        CSV_FILE,
        index=False
    )