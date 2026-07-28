from pathlib import Path

import pandas as pd
import logging

logger = logging.getLogger(__name__)


def load_sales_data(file_path: Path) -> pd.DataFrame:
    """Load sales data from a CSV file."""
    if not file_path.exists():
        raise FileNotFoundError(
            f"Sales data file not found: {file_path}"
        )
    logger.info("Sales data loaded successfully.")
    return pd.read_csv(file_path)