from sqlalchemy import create_engine, inspect
from app.config.settings import (
    DB_SERVER,
    DB_NAME,
    DB_DRIVER,
    DB_TRUST_CERT
)

def get_engine():
    connection_string = (
        f"mssql+pyodbc://@{DB_SERVER}/{DB_NAME}"
        f"?driver={DB_DRIVER}"
        f"&TrustServerCertificate={DB_TRUST_CERT}"
    )

    return create_engine(connection_string)

def get_table_schema(table_name, schema="dbo"):
    engine = get_engine()
    inspector = inspect(engine)
    return inspector.get_columns(table_name, schema=schema)
