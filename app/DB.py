import mysql.connector
import os

db_config = {
    "host": os.getenv("DB_HOST", "mysql"),
    "user": os.getenv("DB_USER", "user"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "database": os.getenv("DB_NAME", "database")
}

def get_connection():
    return mysql.connector.connect(**db_config)