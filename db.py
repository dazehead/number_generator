import os
from sqlalchemy import create_engine, text
import pandas as pd


class Database:
    def __init__(self):
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT", "1433")
        self.db = os.getenv("DB_NAME")
        self.driver = "ODBC+Driver+18+for+SQL+Server"

    def get_engine(self):
        url = (
            f"mssql+pyodbc://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}?driver={self.driver}"
            "&TrustServerCertificate=yes"
        )
        return create_engine(url, pool_pre_ping=True, fast_executemany=True)

    def get_table_from_db(self) -> list[dict]:
        """Return click_metrics as list of plain python dicts"""
        sql = text(""" SELECT * FROM click_metrics;""")
        with self.get_engine().begin() as conn:
            rows = conn.execute(sql).mappings().all()
        return [dict(r) for r in rows]
    
    def get_table_df(self) -> pd.DataFrame:
        """Same data, but as a Pandas Dataframe"""
        plain = self.get_table_from_db
        return pd.DataFrame(plain)
    
    def overwrite_click_metrics(self, rows: list[dict])-> None:
        """replaces all rows in the sql server database"""
        if not rows:
            raise ValueError('rows cannot be empty')
        
        insert_sql = text(
            "INSERT INTO click_metrics (counter, number) VALUES (:counter, :number);"
        )
        with self.get_engine().begin() as conn:
            conn.execute(text("TRUNCATE TABLE click_metrics;"))
            conn.execute(insert_sql, rows)