from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

USER = "medico"
PASSWORD = "medico"
DATABASE = "medico"
PORT = "5432"

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@localhost:{PORT}/{DATABASE}"

engine = create_engine(
    DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally: 
        db.close()

Base = declarative_base()


def recreate_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)