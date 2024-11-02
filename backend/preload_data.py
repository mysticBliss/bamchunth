from sqlalchemy.orm import sessionmaker
from main import TouristLocation, engine

Session = sessionmaker(bind=engine)
session = Session()

# Preload data for Pahalgam
pahalgam = TouristLocation(
    name="Pahalgam",
    description="A scenic hill station in Jammu and Kashmir",
    temperature=15.0,
    humidity=60.0,
    elevation=2740.0,
    air_quality=95.0
)
session.add(pahalgam)

# Preload data for Sonamarg
sonamarg = TouristLocation(
    name="Sonamarg",
    description="A picturesque hill station in Jammu and Kashmir",
    temperature=10.0,
    humidity=55.0,
    elevation=2740.0,
    air_quality=90.0
)
session.add(sonamarg)

session.commit()
session.close()
