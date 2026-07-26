import pandas as pd
import logging

logger = logging.getLogger(__name__)

def summarize_sales(data: pd.DataFrame) -> None:
    """Print a basic summary of the sales data."""
    row_count = len(data)
    total_sales = data["sales_amount"].sum()

    print(f"Rows: {row_count}")
    print(f"Total sales: ${total_sales:,.2f}")
    logger.info("completed")