import uuid
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    first_name = Column(String())
    last_name = Column(String())
    email = Column(String())
    account_created = Column(DateTime())

class Notes(Base):
    __tablename__ = 'notes'

    id = Column(Integer(), primary_key=True)

    notes = Column(String())

class NoteCards(Base):
    __tablename__ = 'notecards'

    id = Column(Integer(), primary_key=True)

if __name__ == '__main__':
    engine = create_engine('')
    Base.metadata.create_all(engine)