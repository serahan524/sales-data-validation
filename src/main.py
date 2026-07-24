from pathlib import Path

from loader import load_sales_data
from report import summarize_sales
from validator import (
    validate_required_columns,
    validate_not_empty,
)


DATA_FILE = Path("data/sample_sales.csv")


def main() -> None:
    sales_data = load_sales_data(DATA_FILE)
    validate_required_columns(sales_data)
    validate_not_empty(sales_data)
    summarize_sales(sales_data)


if __name__ == "__main__":
    main()