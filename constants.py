import os 
from chromadb.config import Settings 

#Define the chroma settings 
CHROMA_SETTINGS = Settings(
    chroma_db_impl = 'duckdb+parquet',
    persist_directory = "db",
    anonymized_telemetry = False
)