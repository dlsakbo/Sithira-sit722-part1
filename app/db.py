from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import settings

# SQLAlchemy database engine and session
engine = create_engine(settings.postgresql://sit722_part_1_3ik2_user:wZzM9Q9zjcL9K81ee6Kc0DX7sYEm0HYe@dpg-cr0tukjqf0us73ffs7i0-a.oregon-postgres.render.com/sit722_part_1_3ik2)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
