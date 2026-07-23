from pathlib import Path

import pandas as pd


DATA_FILE = Path("data/sample_sales.csv")
REQUIRED_COLUMNS = {
    "order_id",
    "customer_id",
    "sales_amount"
}


def load_sales_data(file_path: Path) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    if not file_path.exists():
        raise FileNotFoundError(
            f"Sales data file not found: {file_path}"
        )
     
    return pd.read_csv(file_path)

def validate_required_columns(data: pd.DataFrame) -> None:
    """Validate all required columns from a CSV file"""
    missing_columns = REQUIRED_COLUMNS - set(data.columns)

    if "sales_amount" not in data.columns: 
        raise ValueError(
            f"Required column not found: {sorted(missing_columns)} "
        )


def validate_not_empty(data:pd.DataFrame) -> None:
    """Validate that the sales data contains at least one row."""
    if data.empty:
        raise ValueError("Sales data is empty")


def summarize_sales(data: pd.DataFrame) -> None:
    """Print a basic summary of the sales data."""
    row_count = len(data)
    total_sales = data["sales_amount"].sum()

    print(f"Rows: {row_count}")
    print(f"Total sales: ${total_sales:,.2f}")


def main() -> None:
    sales_data = load_sales_data(DATA_FILE)
    validate_required_columns(sales_data)
    validate_not_empty(sales_data)
    summarize_sales(sales_data)


if __name__ == "__main__":
    main()