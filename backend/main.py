from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

app = FastAPI()

# Database setup
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database model
class TouristLocation(Base):
    __tablename__ = "tourist_locations"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    elevation = Column(Float)
    air_quality = Column(Float)

# Create tables
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Pydantic models for request and response
class TouristLocationCreate(BaseModel):
    name: str
    description: str
    temperature: float
    humidity: float
    elevation: float
    air_quality: float

class TouristLocationResponse(BaseModel):
    id: int
    name: str
    description: str
    temperature: float
    humidity: float
    elevation: float
    air_quality: float

# API endpoints
@app.post("/locations/", response_model=TouristLocationResponse)
def create_location(location: TouristLocationCreate, db: Session = Depends(get_db)):
    db_location = TouristLocation(**location.dict())
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@app.get("/locations/{location_id}", response_model=TouristLocationResponse)
def read_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(TouristLocation).filter(TouristLocation.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    return db_location

@app.get("/locations/", response_model=list[TouristLocationResponse])
def read_locations(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    locations = db.query(TouristLocation).offset(skip).limit(limit).all()
    return locations

@app.put("/locations/{location_id}", response_model=TouristLocationResponse)
def update_location(location_id: int, location: TouristLocationCreate, db: Session = Depends(get_db)):
    db_location = db.query(TouristLocation).filter(TouristLocation.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    for var, value in vars(location).items():
        setattr(db_location, var, value)
    db.add(db_location)
    db.commit()
    db.refresh(db_location)
    return db_location

@app.delete("/locations/{location_id}", response_model=TouristLocationResponse)
def delete_location(location_id: int, db: Session = Depends(get_db)):
    db_location = db.query(TouristLocation).filter(TouristLocation.id == location_id).first()
    if db_location is None:
        raise HTTPException(status_code=404, detail="Location not found")
    db.delete(db_location)
    db.commit()
    return db_location
