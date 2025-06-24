from sqlalchemy import Table, Column, Integer, String
from backend.db import metadata

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("telegram_id", Integer, unique=True),
    Column("username", String),
)
