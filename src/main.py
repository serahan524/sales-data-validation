from pathlib import Path

import pandas as pd


DATA_FILE = Path("data/sample_sales.csv")


def load_sales_data(file_path: Path) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    return pd.read_csv(file_path)


def summarize_sales(data: pd.DataFrame) -> None:
    """Print a basic summary of the sales data."""
    row_count = len(data)
    total_sales = data["sales_amount"].sum()

    print(f"Rows: {row_count}")
    print(f"Total sales: ${total_sales:,.2f}")


def main() -> None:
    sales_data = load_sales_data(DATA_FILE)
    summarize_sales(sales_data)


if __name__ == "__main__":
    main()