from pathlib import Path

from loader import load_sales_data
from report import summarize_sales
from validator import (
    validate_required_columns,
    validate_not_empty,
)

import logging

logger = logging.getLogger(__name__)

DATA_FILE = Path("data/sample_sales.csv")

logging.basicConfig(
    level=logging.ERROR,
    format="%(name)s - %(levelname)s: %(message)s",
)

def main() -> None:
    try: 
        sales_data = load_sales_data(DATA_FILE)       
        validate_required_columns(sales_data)
        
        validate_not_empty(sales_data)
        
    
    except FileNotFoundError as error: 
        logger.error(f"Error: {error}")

    except ValueError as error: 
        logger.error(f"Validation Error: {error}")

    else: 
        summarize_sales(sales_data)

if __name__ == "__main__":
    main()