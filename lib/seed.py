from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Disease, Species, Symptom, Treatment, Prevention

# Set up the database
engine = create_engine('sqlite:///lib/livestock.db')
Session = sessionmaker(bind=engine)
session = Session()

# Optional: Clear previous data
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Add Species
cow = Species(name="Cow")
goat = Species(name="Goat")
chicken = Species(name="Chicken")

#  Add Symptoms 
fever = Symptom(name="Fever", description="High body temperature")
cough = Symptom(name="Cough", description="Persistent coughing")
rash = Symptom(name="Skin Rash", description="Red, irritated skin")

# Add Treatments 
antibiotics = Treatment(name="Antibiotics", method="Administer orally or via injection")
hydration = Treatment(name="Hydration Therapy", method="Provide clean water and electrolyte solutions")

# Add Preventions
vaccination = Prevention(name="Vaccination", method="Routine immunization of livestock")
sanitation = Prevention(name="Improved Sanitation", method="Keep pens clean to prevent infections")

#Add Disease
fmd = Disease(
    name="Foot-and-Mouth Disease",
    abbreviation="FMD",
    region="Worldwide",
    description="A severe, highly contagious viral disease of livestock.",
    image_url="https://example.com/fmd.jpg"
)

# Add relationships
fmd.species.extend([cow, goat])
fmd.symptoms.extend([fever, rash])
fmd.treatments.extend([antibiotics])
fmd.preventions.extend([vaccination, sanitation])

#Commit All to DB 
session.add_all([cow, goat, chicken, fever, cough, rash, antibiotics, hydration, vaccination, sanitation, fmd])
session.commit()

print("Sample data added successfully!")
