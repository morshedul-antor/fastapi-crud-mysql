from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = "mysql+mysqlconnector://root@localhost:3306/crud"

# Create a sqlite engine instance
engine = create_engine(DATABASE_URL)

# Create a DeclarativeMeta instance
Base = declarative_base()

