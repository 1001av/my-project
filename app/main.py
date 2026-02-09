print("MAIN FILE STARTED")

from .db.sql_connector import get_table_schema

if __name__ == "__main__":
    schema = get_table_schema("Customers")  # use a real table name
    print(schema)
