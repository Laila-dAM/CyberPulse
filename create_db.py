from backend.core.database import Base, engine
from backend.models.metric import Metric
from backend.models.alert import Alert

Base.metadata.create_all(bind=engine)
print("Database created successfully!")
