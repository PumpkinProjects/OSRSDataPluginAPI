import os
from dotenv_vault import load_dotenv

load_dotenv(".env")

origins = os.getenv("ORIGINS").split(",")

print(origins)
print(type(origins))