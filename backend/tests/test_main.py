import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from main import Base, TouristLocation

DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    yield session
    session.query(TouristLocation).delete()
    session.commit()
    session.close()
    Base.metadata.drop_all(bind=engine)

def test_create_location(db_session):
    location = TouristLocation(
        name="Test Location",
        description="Test Description",
        temperature=20.0,
        humidity=50.0,
        elevation=1000.0,
        air_quality=90.0
    )
    db_session.add(location)
    db_session.commit()
    assert db_session.query(TouristLocation).filter_by(name="Test Location").first() is not None

def test_read_location(db_session):
    location = TouristLocation(
        name="Test Location",
        description="Test Description",
        temperature=20.0,
        humidity=50.0,
        elevation=1000.0,
        air_quality=90.0
    )
    db_session.add(location)
    db_session.commit()
    retrieved_location = db_session.query(TouristLocation).filter_by(name="Test Location").first()
    assert retrieved_location is not None
    assert retrieved_location.description == "Test Description"

def test_update_location(db_session):
    location = TouristLocation(
        name="Test Location",
        description="Test Description",
        temperature=20.0,
        humidity=50.0,
        elevation=1000.0,
        air_quality=90.0
    )
    db_session.add(location)
    db_session.commit()
    location.description = "Updated Description"
    db_session.commit()
    updated_location = db_session.query(TouristLocation).filter_by(name="Test Location").first()
    assert updated_location.description == "Updated Description"

def test_delete_location(db_session):
    location = TouristLocation(
        name="Test Location",
        description="Test Description",
        temperature=20.0,
        humidity=50.0,
        elevation=1000.0,
        air_quality=90.0
    )
    db_session.add(location)
    db_session.commit()
    db_session.delete(location)
    db_session.commit()
    deleted_location = db_session.query(TouristLocation).filter_by(name="Test Location").first()
    assert deleted_location is None
