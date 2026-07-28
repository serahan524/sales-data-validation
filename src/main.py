import logging

from config import DATA_FILE
from loader import load_sales_data
from report import summarize_sales
from validator import (
    validate_required_columns,
    validate_not_empty,
)


logging.basicConfig(
    level=logging.INFO,
    format="%(name)s - %(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


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