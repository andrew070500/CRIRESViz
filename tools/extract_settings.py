import camelot
import pandas as pd

from criresviz.common import MANUALS, EXTRACTED


def main():

    tables = camelot.read_pdf(
        str(MANUALS),
        pages="all",
        flavor="lattice",
    )

    #
    # Temporary:
    # we'll inspect every table manually.
    #

    for i, table in enumerate(tables):

        df = table.df

        print("=" * 80)
        print(i)
        print(df.head())


if __name__ == "__main__":
    main()
