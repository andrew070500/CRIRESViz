from pathlib import Path

import camelot
import pickle

from common import MANUALS
from common import PREVIEW

def main():

    print(f"Reading {MANUALS.name}")

    tables = camelot.read_pdf(
        str(MANUALS),
        pages="90-93",
        flavor="stream",
    )

    print(f"Found {tables.n} tables.")

    PREVIEW.mkdir(exist_ok=True)

    for i, table in enumerate(tables):
        
        df = table.df

        filename = PREVIEW / f"{i:02d}_page{table.parsing_report['page']}.csv"
        df.to_csv(filename, index=False)

        pkl_filename = str(filename).replace(".csv", ".pkl")
        df.to_pickle(pkl_filename)
     

if __name__ == "__main__":
    main()
