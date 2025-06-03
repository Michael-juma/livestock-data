from lib.models import Disease  
from lib.database import session 

# Ask for user input
disease_name = input("Enter disease name: ")

# Query disease by name
disease = session.query(Disease).filter(Disease.name.ilike(f"%{disease_name}%")).first()

if not disease:
    print("Disease not found.")
else:
    print("\n========== Disease Details ==========")
    print(f"Name: {disease.name}")
    print(f"Abbreviation: {disease.abbreviation}")
    print(f"Region: {disease.region}")
    print(f"Description: {disease.description}")
    print(f"Image URL: {disease.image_url}")

    print("\n--- Species Affected ---")
    for sp in disease.species:
        print(f" - {sp.name}")

    print("\n--- Symptoms ---")
    for sym in disease.symptoms:
        print(f" - {sym.name}: {sym.description}")

    print("\n--- Treatments ---")
    for tr in disease.treatments:
        print(f" - {tr.name}: {tr.method}")

    print("\n--- Preventions ---")
    for pr in disease.preventions:
        print(f" - {pr.name}: {pr.method}")
