from dotenv import load_dotenv
import os

# Open the .env file and load everything in Python
load_dotenv()

# Read
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
DATABASE_URL = os.getenv("DATABASE_URL")
