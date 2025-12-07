from backend.core.database import Base, engine
from backend.models import models

Base.metadata.create_all(bind=engine)
print("Database created successfully")
