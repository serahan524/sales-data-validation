
from pathlib import Path

import pandas as pd



REQUIRED_COLUMNS = {
    "order_id",
    "customer_id",
    "sales_amount",
}


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