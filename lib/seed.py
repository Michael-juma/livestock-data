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

fever = Symptom(
    name="Fever", description="Elevated body temperature, often indicating infection or inflammation.")
cough = Symptom(
    name="Cough", description="Repetitive hacking sound caused by irritation in the respiratory tract.")
skin_rash = Symptom(
    name="Skin Rash", description="Irritated, red, or inflamed skin that may indicate allergies or parasites.")
blood_in_stool = Symptom(
    name="Blood in Stool", description="Presence of blood in feces, which can suggest internal bleeding or infections.")
weight_loss = Symptom(
    name="Weight Loss", description="Unexplained loss of body mass, often due to illness, parasites, or poor nutrition.")
lameness = Symptom(
    name="Lameness", description="Difficulty in walking or limping, usually caused by injury or hoof diseases.")
loss_of_appetite = Symptom(
    name="Loss of Appetite", description="Reduced desire to eat, often indicating discomfort or systemic illness.")
diarrhea = Symptom(
    name="Diarrhea", description="Frequent, loose or watery bowel movements, often caused by infection or dietary upset.")
constipation = Symptom(
    name="Constipation", description="Difficulty passing stool, which may indicate digestive issues.")
vomiting = Symptom(
    name="Vomiting", description="Ejection of stomach contents through the mouth due to gastrointestinal distress.")

# Add Treatments
antibiotics = Treatment(
    name="Antibiotics", method="Administer orally or via injection to combat bacterial infections.")
hydration = Treatment(name="Hydration Therapy",
                      method="Provide clean water and electrolyte solutions to restore fluid balance.")
deworming = Treatment(
    name="Deworming", method="Use anthelmintic drugs to eliminate internal parasites.")
# vaccination = Treatment(name="Vaccination", method="Administer vaccines to prevent viral and bacterial infections.")
topical_ointment = Treatment(
    name="Topical Ointment", method="Apply medicated cream to affected skin areas.")
anti_inflammatory = Treatment(name="Anti-Inflammatory Drugs",
                              method="Inject or administer orally to reduce swelling and pain.")
pain_relief = Treatment(
    name="Pain Relief", method="Use analgesics to alleviate pain symptoms.")
wound_cleaning = Treatment(
    name="Wound Cleaning", method="Clean with antiseptic solution and dress to prevent infection.")
antipyretics = Treatment(
    name="Antipyretics", method="Use fever reducers like paracetamol to lower high body temperature.")
nutritional_supplements = Treatment(
    name="Nutritional Supplements", method="Provide minerals and vitamins to boost immune function.")
isolation = Treatment(
    name="Isolation", method="Separate the sick animal to prevent disease spread.")

# Preventive Measures
vaccination = Prevention(
    name="Vaccination",
    method="Routine immunization of livestock with appropriate vaccines to build immunity against common infectious diseases."
)

sanitation = Prevention(
    name="Improved Sanitation",
    method="Regular cleaning and disinfecting of animal pens, equipment, and feeding areas to reduce the risk of infections."
)

quarantine = Prevention(
    name="Quarantine",
    method="Isolating new or sick animals from the healthy herd for a specified period to prevent the spread of contagious diseases."
)

biosecurity = Prevention(
    name="Biosecurity Measures",
    method="Implementing strict controls on farm access, visitor hygiene, and equipment to minimize disease introduction."
)

proper_nutrition = Prevention(
    name="Proper Nutrition",
    method="Providing balanced diets with essential nutrients to strengthen animals’ immune systems and overall health."
)

vector_control = Prevention(
    name="Vector Control",
    method="Using insecticides, traps, and environmental management to reduce populations of disease-carrying insects and parasites."
)

clean_water = Prevention(
    name="Clean Water Supply",
    method="Ensuring access to clean and safe drinking water to prevent waterborne diseases."
)

regular_health_checks = Prevention(
    name="Regular Health Checks",
    method="Frequent veterinary inspections and monitoring to detect and manage diseases early."
)

stress_reduction = Prevention(
    name="Stress Reduction",
    method="Providing comfortable housing and minimizing overcrowding to reduce stress-related susceptibility to diseases."
)

proper_waste_management = Prevention(
    name="Proper Waste Management",
    method="Safe disposal and treatment of animal waste to prevent contamination of the environment and disease spread."
)

good_husbandry_practices = Prevention(
    name="Good Husbandry Practices",
    method="Following best management practices including proper handling, housing, and care of livestock."
)

prompt_treatment = Prevention(
    name="Prompt Treatment",
    method="Early identification and treatment of sick animals to prevent disease progression and transmission."
)

vaccination_schedule = Prevention(
    name="Adherence to Vaccination Schedule",
    method="Strictly following recommended vaccination timings to ensure continuous immunity."
)

rodent_control = Prevention(
    name="Rodent Control",
    method="Controlling rodent populations that can act as disease reservoirs on farms."
)

environmental_control = Prevention(
    name="Environmental Control",
    method="Maintaining optimal temperature, humidity, and ventilation in animal housing to reduce disease risk."
)

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
btb = Disease(
    name="Bovine Tuberculosis",
    abbreviation="BTB",
    region="Worldwide",
    description="""
Bovine Tuberculosis is a chronic bacterial disease caused by Mycobacterium bovis, which primarily affects cattle but can infect a wide range of mammals, including humans. The bacteria spread through inhalation of infected aerosols or ingestion of contaminated feed and water. Infected animals may carry the disease asymptomatically for long periods, making it difficult to detect and control.

Clinically, signs include chronic coughing, weight loss, enlarged lymph nodes, and general weakness. In some animals, no signs are visible until the disease has progressed significantly. It often spreads insidiously within herds, increasing the risk of transmission to other animals and potentially to farm workers handling livestock.

BTB is a zoonotic disease and poses public health risks, especially in regions where milk is consumed unpasteurized. Surveillance, routine testing, and culling of infected animals are common control measures. Vaccines are under development but not yet widely available or effective in cattle populations.

Effective control requires strict biosecurity protocols, movement restrictions on affected herds, and proper carcass disposal. Regular veterinary inspections and education of livestock handlers are critical in minimizing disease incidence.
""",
    image_url="https://example.com/btb.jpg"
)



brucellosis = Disease(
    name="Brucellosis",
    abbreviation="BRU",
    region="Worldwide",
    description="""
Brucellosis is an infectious disease caused by bacteria of the genus Brucella, affecting cattle (B. abortus), sheep and goats (B. melitensis), pigs (B. suis), and occasionally other animals. It is a major cause of reproductive failure in livestock, with symptoms such as abortion, retained placenta, infertility, and orchitis in males.

The disease spreads through direct contact with infected reproductive fluids, ingestion of contaminated materials, or exposure to contaminated environments. Humans can contract the disease through raw dairy products or occupational exposure, leading to a condition known as undulant fever.

There is no treatment for infected livestock; eradication programs typically involve testing, culling, and vaccination. Vaccination of young animals has proven effective in controlling disease prevalence in endemic regions.

Brucellosis control requires comprehensive surveillance, public education, and intersectoral cooperation between animal and human health services. Proper handling of birth products and carcasses is crucial in preventing spread.
""",
    image_url="https://example.com/brucellosis.jpg"
)

afb = Disease(
    name="American Foulbrood",
    abbreviation="AFB",
    region="Worldwide",
    description="""
American Foulbrood (AFB) is a highly infectious and lethal bacterial disease affecting honeybee brood. It is caused by Paenibacillus larvae, a spore-forming bacterium that can remain viable in the environment for decades. The disease primarily targets larvae under three days old and rapidly destroys the colony if not contained.

Symptoms include sunken, perforated cappings over brood cells, a foul rotten odor, and a dark, gooey consistency of dead larvae. A hallmark sign is the formation of a stringy thread when a matchstick is inserted into the cell and withdrawn — known as the "ropy test."

AFB spreads through contaminated beekeeping equipment, robbing behavior, and drift between hives. There is no cure for the disease; control involves burning infected hives and equipment, and sometimes prophylactic antibiotics in regions where they are allowed.

Stringent biosecurity practices, regular hive inspections, and immediate action upon detection are essential to preventing large-scale outbreaks.
""",
    image_url="https://example.com/afb.jpg"
)

efb = Disease(
    name="European Foulbrood",
    abbreviation="EFB",
    region="Worldwide (temperate regions)",
    description="""
European Foulbrood (EFB) is a bacterial disease caused by Melissococcus plutonius that affects honeybee larvae. Unlike American Foulbrood, EFB typically impacts larvae before the cell is capped and tends to be less destructive, though it can severely weaken colonies.

Infected larvae appear twisted in their cells, yellowish or brown in color, and emit a sour odor. The disease is often associated with stress factors like poor nutrition or overcrowding, which makes colonies more susceptible.

EFB can be managed through improved hive management, feeding practices, and the use of antibiotics where permitted. Strong, well-fed colonies often recover naturally once environmental stressors are removed.

Regular monitoring, requeening with hygienic stock, and improved apiary hygiene are effective control measures.
""",
    image_url="https://example.com/efb.jpg"
)

nosema = Disease(
    name="Nosema Disease",
    abbreviation="Nosema",
    region="Worldwide",
    description="""
Nosema disease is caused by microsporidian parasites—Nosema apis and Nosema ceranae—that infect the midgut cells of adult bees. It results in dysentery, lethargy, reduced foraging, and colony decline. The disease often emerges during cooler, damp periods when bees are confined indoors.

Infected bees exhibit symptoms like swollen abdomens, inability to fly, and scattered dead bees around the hive entrance. Fecal streaks on the hive surface are also common. Nosema weakens immune function and shortens bee lifespan, leading to dwindling colony populations.

Treatment includes administering fumagillin (where legal) and improving hive ventilation and nutrition. Replacing old comb and reducing moisture in the hive are additional preventive strategies.

Routine monitoring, especially in early spring and fall, is critical to catch Nosema infections early before colony collapse.
""",
    image_url="https://example.com/nosema.jpg"
)

chalkbrood = Disease(
    name="Chalkbrood",
    abbreviation="CB",
    region="Worldwide",
    description="""
Chalkbrood is a fungal disease affecting honeybee larvae, caused by Ascosphaera apis. It thrives in cool, damp hive conditions and results in mummified larvae that resemble chalky white or gray pellets, often found at the hive entrance.

Larvae become infected after ingesting spores that germinate in the gut. As the fungus grows, it fills the larval body with a cotton-like mycelium, eventually killing it. Although not typically fatal to entire colonies, it can weaken them, reduce brood viability, and lower honey production.

Preventive strategies include improving hive ventilation, reducing moisture, and requeening with hygienic bee strains. Cleaning or replacing infected frames is also recommended.

The disease is often seasonal and can resolve when weather conditions improve and stress factors are minimized.
""",
    image_url="https://example.com/chalkbrood.jpg"
)

sbv = Disease(
    name="Sacbrood Virus",
    abbreviation="SBV",
    region="Worldwide",
    description="""
Sacbrood Virus (SBV) is a common viral disease in honeybee colonies, particularly affecting larvae. It prevents larvae from pupating properly, leaving them as fluid-filled sacs that dry into scale-like remains within the brood cells.

Symptoms include dead larvae with a rice-grain appearance, a lack of normal segmentation, and a stretched sac filled with clear fluid. The disease often coincides with stressful conditions like poor nutrition or weak colonies.

SBV is usually not fatal to entire colonies and can often be managed through improved colony strength, good nutrition, and hygienic queen lines. No direct treatment exists, but strong hives typically outgrow the infection.

Routine inspection and removing heavily infected brood combs help limit the spread of the virus.
""",
    image_url="https://example.com/sbv.jpg"
)

dwv = Disease(
    name="Deformed Wing Virus",
    abbreviation="DWV",
    region="Worldwide",
    description="""
Deformed Wing Virus (DWV) is a viral disease most commonly associated with Varroa mite infestations. It causes developmental deformities in adult bees, particularly shriveled or twisted wings, leading to impaired flight and early death.

The virus is transmitted primarily by Varroa destructor mites, which feed on bee fat bodies and spread the virus directly into their circulatory system. DWV weakens individual bees and leads to colony collapse if left unchecked.

No direct treatment exists for DWV, but controlling Varroa mite populations is the most effective management strategy. This can be achieved through mechanical, biological, or chemical interventions.

Regular mite monitoring, rotating treatments, and breeding mite-resistant bee strains are key to preventing DWV outbreaks.
""",
    image_url="https://example.com/dwv.jpg"
)


#relationships
fmd.species.extend([cow, goat, sheep, pig, horse, llama, alpaca])
fmd.symptoms.extend([fever, skin_rash, cough, blood_in_stool, weight_loss,
                    lameness, loss_of_appetite, diarrhea, constipation, vomiting])
fmd.treatments.extend([antibiotics, hydration, deworming, topical_ointment, anti_inflammatory,
                      pain_relief, wound_cleaning, antipyretics, nutritional_supplements, isolation])
fmd.preventions.extend([vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control, clean_water, regular_health_checks,
                       stress_reduction, proper_waste_management, good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control, environmental_control])

anthrax.species.extend([cow, goat, chicken, pig, sheep,
                       duck, horse, rabbit, turkey, alpaca, llama, cat, dog])
anthrax.symptoms.extend([fever, cough, skin_rash, blood_in_stool, weight_loss,
                        lameness, loss_of_appetite, diarrhea, constipation, vomiting])
anthrax.treatments.extend([antibiotics, hydration, deworming, topical_ointment, anti_inflammatory,
                          pain_relief, wound_cleaning, antipyretics, nutritional_supplements, isolation])
anthrax.preventions.extend([vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control, clean_water, regular_health_checks,
                           stress_reduction, proper_waste_management, good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control, environmental_control])

swine_erysipelas.species.extend([pig])
swine_erysipelas.symptoms.extend([fever, skin_rash, cough, blood_in_stool,
                                 weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting])
swine_erysipelas.treatments.extend([antibiotics, hydration, deworming, topical_ointment, anti_inflammatory,
                                   pain_relief, wound_cleaning, antipyretics, nutritional_supplements, isolation])
swine_erysipelas.preventions.extend([vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control, clean_water, regular_health_checks,
                                    stress_reduction, proper_waste_management, good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control, environmental_control])

rabies.species.extend([dog, cat, cow, goat, sheep, pig, horse])
rabies.symptoms.extend([fever, cough, skin_rash, blood_in_stool, weight_loss,
                       lameness, loss_of_appetite, diarrhea, constipation, vomiting])
rabies.treatments.extend([antibiotics, hydration, isolation])
rabies.preventions.extend([vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control, clean_water, regular_health_checks,
                          stress_reduction, proper_waste_management, good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control, environmental_control])
btb.species.extend([cow, goat, sheep, pig, horse])
btb.symptoms.extend([fever, cough, skin_rash, blood_in_stool, weight_loss,
                    lameness, loss_of_appetite, diarrhea, constipation, vomiting])
btb.treatments.extend([antibiotics, hydration, deworming, topical_ointment, anti_inflammatory,
                      pain_relief, wound_cleaning, antipyretics, nutritional_supplements, isolation])
btb.preventions.extend([vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control, clean_water, regular_health_checks,
                       stress_reduction, proper_waste_management, good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control, environmental_control])

brucellosis.species.extend([cow, goat, sheep, pig])
brucellosis.symptoms.extend([fever, cough, skin_rash, blood_in_stool, weight_loss,
                             lameness, loss_of_appetite, diarrhea, constipation, vomiting])
brucellosis.treatments.extend([antibiotics, hydration, deworming, topical_ointment, anti_inflammatory,
                               pain_relief, wound_cleaning, antipyretics, nutritional_supplements, isolation])
brucellosis.preventions.extend([vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control, clean_water, regular_health_checks,
                                stress_reduction, proper_waste_management, good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control, environmental_control])
#specify for bees only
afb.species.extend([bee])


# Commit All to DB
session.add_all([cow, goat, chicken, pig, sheep, duck, horse, rabbit, turkey, alpaca, llama, cat,
                dog, fish, bee, fever, cough, skin_rash, blood_in_stool, weight_loss, lameness, loss_of_appetite, diarrhea, constipation, vomiting, antibiotics, hydration, vaccination, sanitation, fmd, anthrax, swine_erysipelas, rabies, btb, brucellosis])
session.commit()

print("Sample data added successfully!")
