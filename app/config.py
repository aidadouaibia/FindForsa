from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URI = os.getenv("DATABASE_URI")
DB_NAME = os.getenv("DB_NAME")
