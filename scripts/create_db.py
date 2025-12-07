from backend.core.database import engine, Base
import backend.models.models

def create_all_tables():
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Tables created successfully.")

if __name__ == "__main__":
    create_all_tables()
