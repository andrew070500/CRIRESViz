import camelot
from criresviz.common import MANUALS, PREVIEW

DEBUG = False # Enable full PDF inspection.


"""
Extract the CRIRES+ settings tables from the ESO User Manual.

The extracted tables are saved as CSV and pickle files for inspection
and subsequent normalization.
"""

def main():
    """
    Extract the CRIRES+ settings tables from the User Manual.
    """

    if DEBUG:
        tables = camelot.read_pdf(
            str(MANUALS),
            pages="all",
            flavor="lattice",
        )
    
        for i, table in enumerate(tables):
    
            df = table.df
    
            print("=" * 80)
            print(f"Table {i} (page {table.parsing_report['page']})")
            print(df.head())



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

        pkl_filename = filename.with_suffix(".pkl")
        df.to_pickle(pkl_filename)
     

if __name__ == "__main__":
    main()
