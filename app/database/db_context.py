from sqlmodel import SQLModel, create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.core.settings import settings


engine = create_engine(
    f'postgresql+psycopg2://{settings.db_user}:{settings.db_password}@{
        settings.db_host}:{settings.db_port}/{settings.db_name}',
    connect_args={'options': '-csearch_path=notiflux'}
)
default_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine
    )
)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_database():
    db = default_session()
    try:
        yield db
    finally:
        db.close()
