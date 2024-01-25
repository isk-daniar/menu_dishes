from dotenv import load_dotenv
import os

load_dotenv()

SQL_ENGINE = os.environ.get("SQL_ENGINE")
SQL_DATABASE = os.environ.get("SQL_DATABASE")
SQL_USER = os.environ.get("SQL_USER")
SQL_PASSWORD = os.environ.get("SQL_PASSWORD")
SQL_HOST = os.environ.get("SQL_HOST")
SQL_PORT = os.environ.get("SQL_PORT")



