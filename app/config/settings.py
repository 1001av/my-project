import os
from dotenv import load_dotenv

load_dotenv()

DB_SERVER = "AKHILPC\\SQLEXPRESS"
DB_NAME = "SyntheticDataDB"
DB_DRIVER = "ODBC Driver 18 for SQL Server"

DB_TRUST_CERT = "yes"

CONNECTION_STRING = (
    "mssql+pyodbc://@AKHILPC\\SQLEXPRESS/SQLTutorial"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&Trusted_Connection=yes"
    "&TrustServerCertificate=yes"
)


