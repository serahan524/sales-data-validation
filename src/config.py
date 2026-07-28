import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

DATA_FILE=Path(os.environ["DATA_FILE"])

