from sqlalchemy import create_engine
import os
from db.models import Base

db_url = os.environ.get("DATABASE_URL", "sqlite://")

engine = create_engine(db_url, echo=True)

Base.metadata.create_all(engine)
