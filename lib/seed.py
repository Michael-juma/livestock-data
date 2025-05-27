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
'''add 30 species here'''
cow = Species(name="Cow")
goat = Species(name="Goat")
chicken = Species(name="Chicken")
pig = Species(name="Pig")
sheep = Species(name="Sheep")
duck = Species(name="Duck")
horse = Species(name="Horse")
rabbit = Species(name="Rabbit")
turkey = Species(name="Turkey")
alpaca = Species(name="Alpaca")
llama = Species(name="Llama")
cat = Species(name="Cat")
dog = Species(name="Dog")
fish = Species(name="Fish")
bee = Species(name="Bee")


#  Add Symptoms

fever = Symptom(name="Fever", description="Elevated body temperature, often indicating infection or inflammation.")
cough = Symptom(name="Cough", description="Repetitive hacking sound caused by irritation in the respiratory tract.")
skin_rash = Symptom(name="Skin Rash", description="Irritated, red, or inflamed skin that may indicate allergies or parasites.")
blood_in_stool = Symptom(name="Blood in Stool", description="Presence of blood in feces, which can suggest internal bleeding or infections.")
weight_loss = Symptom(name="Weight Loss", description="Unexplained loss of body mass, often due to illness, parasites, or poor nutrition.")
lameness = Symptom(name="Lameness", description="Difficulty in walking or limping, usually caused by injury or hoof diseases.")
loss_of_appetite = Symptom(name="Loss of Appetite", description="Reduced desire to eat, often indicating discomfort or systemic illness.")
diarrhea = Symptom(name="Diarrhea", description="Frequent, loose or watery bowel movements, often caused by infection or dietary upset.")
constipation = Symptom(name="Constipation", description="Difficulty passing stool, which may indicate digestive issues.")
vomiting = Symptom(name="Vomiting", description="Ejection of stomach contents through the mouth due to gastrointestinal distress.")

# Add Treatments
antibiotics = Treatment(
    name="Antibiotics", method="Administer orally or via injection")
hydration = Treatment(name="Hydration Therapy",
                      method="Provide clean water and electrolyte solutions")

# Add Preventions
vaccination = Prevention(
    name="Vaccination", method="Routine immunization of livestock")
sanitation = Prevention(name="Improved Sanitation",
                        method="Keep pens clean to prevent infections")

# Add Disease
fmd = Disease(
    name="Foot-and-Mouth Disease",
    abbreviation="FMD",
    region="Worldwide",
    description="""Foot-and-Mouth Disease (FMD) is a highly contagious viral disease that affects cloven-hoofed animals such as cattle, pigs, sheep, goats, and wild animals like deer and antelope. It is caused by an aphthovirus of the family Picornaviridae and is characterized by fever and blister-like sores on the mouth, tongue, lips, and between the hooves.

FMD spreads rapidly through direct contact with infected animals, contaminated feed, water, equipment, and even through the air over short distances. Infected animals may exhibit lameness, drooling, reluctance to move, and loss of appetite. Though the mortality rate is low in adult animals, the disease can be fatal in young animals and causes severe production losses due to decreased milk yield, weight loss, and trade restrictions.

FMD does not typically infect humans but can cause serious economic impact due to outbreaks. Control measures include quarantines, movement restrictions, culling infected animals, and routine vaccination programs in endemic areas. Early detection and strict biosecurity are critical for containment.
""",
    image_url="https://example.com/fmd.jpg"
)
anthrax = Disease(
    name="Anthrax",
    abbreviation="ANTH",
    region="Worldwide",
    description="""Anthrax is a serious infectious disease caused by the bacterium *Bacillus anthracis*. It primarily affects livestock such as cattle, sheep, and goats, but can also infect humans who come into contact with infected animals or animal products. The bacterium forms durable spores that can survive in soil for decades and enter an animal’s body through ingestion, inhalation, or open wounds.

In animals, anthrax can cause sudden death with minimal signs. Symptoms may include high fever, difficulty breathing, convulsions, and swelling. In some cases, blood may ooze from the mouth, nose, or anus. In humans, anthrax manifests in cutaneous, inhalational, or gastrointestinal forms, each with varying symptoms and severity.

Anthrax is a zoonotic disease and is considered a potential biological weapon due to the resilience of its spores. Preventive measures include regular livestock vaccination in endemic areas and proper disposal of carcasses. Humans can be protected through occupational safety practices and, in certain cases, vaccines.
""",
    image_url="https://example.com/anthrax.jpg"
)
swine_erysipelas = Disease(
    name="Swine Erysipelas",
    abbreviation="SE",
    region="Worldwide",
    description="""Swine Erysipelas is a bacterial infection caused by *Erysipelothrix rhusiopathiae*, primarily affecting pigs. It can manifest in acute, subacute, or chronic forms, leading to a range of symptoms including fever, skin lesions, and arthritis. The disease is often associated with poor management practices and can result in significant economic losses in swine production.

In acute cases, affected pigs may exhibit sudden fever, lethargy, and skin lesions that can progress to diamond-shaped patches. Chronic infections can lead to arthritis and endocarditis, making early detection and treatment crucial.

Preventive measures include good hygiene practices, proper nutrition, and vaccination in high-risk herds. Treatment typically involves antibiotics, but prevention is the most effective strategy.
""",
    image_url="https://example.com/swine_erysipelas.jpg"
)
rabies = Disease(
    name="Rabies",
    abbreviation="RAB",
    region="Worldwide",
    description="""Rabies is a viral disease caused by the rabies virus, primarily affecting mammals, including livestock and humans. It is transmitted through the bite of an infected animal, most commonly dogs, bats, and wild carnivores. The virus attacks the central nervous system, leading to encephalitis and ultimately death if untreated.""",
    image_url="https://example.com/rabies.jpg"
)

# Add relationships
fmd.species.extend([cow, goat, sheep, pig, horse, llama, alpaca])
fmd.symptoms.extend([fever, skin_rash, cough, blood_in_stool, weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting])
fmd.treatments.extend([antibiotics])
fmd.preventions.extend([vaccination, sanitation])

anthrax.species.extend([cow, goat, chicken, pig, sheep,
                       duck, horse, rabbit, turkey, alpaca, llama, cat, dog])
anthrax.symptoms.extend([fever, cough, skin_rash, blood_in_stool, weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting])
anthrax.treatments.extend([antibiotics, hydration])
anthrax.preventions.extend([vaccination, sanitation])

swine_erysipelas.species.extend([pig])
swine_erysipelas.symptoms.extend([fever, skin_rash, cough, blood_in_stool, weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting])
swine_erysipelas.treatments.extend([antibiotics])
swine_erysipelas.preventions.extend([vaccination, sanitation])

rabies.species.extend([dog, cat, cow, goat, sheep, pig, horse])
rabies.symptoms.extend([fever, cough, skin_rash, blood_in_stool, weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting])
rabies.treatments.extend([antibiotics])
rabies.preventions.extend([vaccination, sanitation])

# Commit All to DB
session.add_all([cow, goat, chicken, pig, sheep, duck, horse, rabbit, turkey, alpaca, llama, cat,
                dog, fish, bee, fever, cough, skin_rash, blood_in_stool, weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting, antibiotics, hydration, vaccination, sanitation, fmd, anthrax, swine_erysipelas, rabies])
session.commit()

print("Sample data added successfully!")
