from pathlib import Path
import pandas as pd
import urllib
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv


script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent[0]

load_dotenv(project_root / ".env")

data_path = project_root / "data" / "raw" / "dynamic_supply_chain_logistics_dataset.csv"

db_host = os.getenv("SQL_SERVER_HOST","localhost")
db_port = os.getenv("SQL_SERVER_PORT", "1433")

