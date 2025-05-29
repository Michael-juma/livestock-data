from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Base, Disease, Species, Symptom, Treatment, Prevention

engine = create_engine('sqlite:///lib/livestock.db')
Session = sessionmaker(bind=engine)
session = Session()


Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Add Species
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

# Add Symptoms
fever = Symptom(
    name="Fever", 
    description="Elevated body temperature, often indicating infection or inflammation."
)
cough = Symptom(
    name="Cough", 
    description="Repetitive hacking sound caused by irritation in the respiratory tract."
)
skin_rash = Symptom(
    name="Skin Rash", 
    description="Irritated, red, or inflamed skin that may indicate allergies or parasites."
)
blood_in_stool = Symptom(
    name="Blood in Stool", 
    description="Presence of blood in feces, which can suggest internal bleeding or infections."
)
weight_loss = Symptom(
    name="Weight Loss", 
    description="Unexplained loss of body mass, often due to illness, parasites, or poor nutrition."
)
lameness = Symptom(
    name="Lameness", 
    description="Difficulty in walking or limping, usually caused by injury or hoof diseases."
)
loss_of_appetite = Symptom(
    name="Loss of Appetite", 
    description="Reduced desire to eat, often indicating discomfort or systemic illness."
)
diarrhea = Symptom(
    name="Diarrhea", 
    description="Frequent, loose or watery bowel movements, often caused by infection or dietary upset."
)
constipation = Symptom(
    name="Constipation", 
    description="Difficulty passing stool, which may indicate digestive issues."
)
vomiting = Symptom(
    name="Vomiting", 
    description="Ejection of stomach contents through the mouth due to gastrointestinal distress."
)

# Bee-specific symptoms
paralysis = Symptom(
    name="Paralysis", 
    description="Loss of muscle function in wings or legs, often resulting from viral infections like Chronic Bee Paralysis Virus (CBPV)."
)
lethargy = Symptom(
    name="Lethargy", 
    description="A state of tiredness, weariness, fatigue, or lack of energy, often indicating illness or infection."
)
trembling = Symptom(
    name="Trembling", 
    description="Uncontrolled shaking of the bee's body or wings, typically seen in neurological or viral infections."
)
crawling = Symptom(
    name="Crawling Behavior", 
    description="Bees unable to fly, seen crawling near hive entrances, commonly associated with Deformed Wing Virus or Nosema."
)
distended_abdomen = Symptom(
    name="Distended Abdomen", 
    description="Swollen and bloated abdomen, often a sign of Nosema infection or dysentery."
)
dysentery = Symptom(
    name="Dysentery", 
    description="Excessive defecation inside or around the hive, typically due to poor nutrition, Nosema, or prolonged confinement."
)
discolored_larvae = Symptom(
    name="Discolored Larvae", 
    description="Larvae turning yellow, brown, or black, usually indicating brood disease like American or European Foulbrood."
)
mummified_larvae = Symptom(
    name="Mummified Larvae", 
    description="Dead larvae that dry out and resemble chalk, characteristic of Chalkbrood infection."
)
foul_odor = Symptom(
    name="Foul Odor", 
    description="Strong, unpleasant smell in the brood chamber, a classic sign of American Foulbrood."
)
sunken_cappings = Symptom(
    name="Sunken Cappings", 
    description="Depressed and sometimes perforated cell cappings over diseased brood, common in Foulbrood infections."
)
larval_twisting = Symptom(
    name="Larval Twisting", 
    description="Larvae appearing twisted or misaligned in their cells, often associated with European Foulbrood."
)
sac_like_larvae = Symptom(
    name="Sac-like Larvae", 
    description="Dead larvae resembling fluid-filled sacs, a hallmark symptom of Sacbrood Virus."
)
deformed_wings = Symptom(
    name="Deformed Wings", 
    description="Misshapen or crumpled wings in adult bees, typically caused by Deformed Wing Virus."
)
flightlessness = Symptom(
    name="Flightlessness", 
    description="Inability of adult bees to fly, frequently linked to wing deformities or neurological damage."
)
hairless_abdomen = Symptom(
    name="Hairless Abdomen", 
    description="Smooth, shiny thorax or abdomen due to loss of body hair, often seen in bees infected with CBPV."
)
reduced_flight_activity = Symptom(
    name="Reduced Flight Activity", 
    description="Fewer foraging trips or inactivity around the hive, commonly seen during illness or parasite infestation."
)
scattered_brood = Symptom(
    name="Scattered Brood Pattern", 
    description="Irregular brood layout with many empty cells, suggesting poor queen performance or disease."
)
larval_death_before_capping = Symptom(
    name="Larval Death Before Capping", 
    description="Larvae dying before being capped, a typical symptom of European Foulbrood."
)
abnormal_pupa = Symptom(
    name="Abnormal Pupa", 
    description="Pupae with missing or malformed body parts, possibly due to viral infections or pesticide exposure."
)
queen_rejection = Symptom(
    name="Queen Rejection", 
    description="Workers ejecting or attacking the queen, often following queen infection or exposure to stress."
)
sudden_collapse = Symptom(
    name="Sudden Colony Collapse", 
    description="Rapid disappearance of the worker population, commonly referred to as Colony Collapse Disorder (CCD)."
)
dead_brood = Symptom(
    name="Dead Brood",
    description="Brood that has died due to infection, often appearing discolored or sunken in the cell."
)
behavioral_changes = Symptom(
    name="Behavioral Changes",
    description="Unusual aggression, restlessness, or other abnormal behaviors often seen in animals infected with rabies."
)
excessive_salivation = Symptom(
    name="Excessive Salivation",
    description="Increased drooling or foaming at the mouth, commonly observed in rabies cases."
)
difficulty_swallowing = Symptom(
    name="Difficulty Swallowing",
    description="Trouble swallowing food or water, a symptom of rabies affecting the nervous system."
)
seizures = Symptom(
    name="Seizures",
    description="Sudden, uncontrolled electrical disturbances in the brain, leading to convulsions."
)
ataxia = Symptom(
    name="Ataxia",
    description="Loss of coordination or unsteady movements, often due to nervous system impairment."
)
excessive_vocalization = Symptom(
    name="Excessive Vocalization",
    description="Unusual or increased vocal sounds, such as barking, howling, or bellowing, seen in rabid animals."
)
swollen_udder = Symptom(
    name="Swollen Udder",
    description="Enlargement or inflammation of the udder, often associated with infection or mastitis."
)
joint_swelling = Symptom(
    name="Joint Swelling",
    description="Swelling of joints, which may indicate infection or inflammation, commonly seen in brucellosis."
)
bleeding_from_orifices = Symptom(
    name="Bleeding from Orifices",
    description="Bleeding from the mouth, nose, or anus, often seen in acute anthrax cases."
)
sudden_death = Symptom(
    name="Sudden Death",
    description="Unexpected and rapid death, sometimes the only sign of acute anthrax infection."
)
swelling = Symptom(
    name="Swelling",
    description="Swelling of the body or specific areas, such as the neck or abdomen, due to infection."
)
respiratory_distress = Symptom(
    name="Respiratory Distress",
    description="Difficulty breathing, which may occur in severe infections."
)
abortion = Symptom(
    name="Abortion",
    description="Premature expulsion of the fetus, a possible symptom in infected pregnant animals."
)
vesicles_in_mouth_and_feet = Symptom(
    name="Vesicles in Mouth and Feet",
    description="Blister-like lesions in the mouth and between the hooves, characteristic of FMD."
)
reluctance_to_move = Symptom(
    name="Reluctance to Move",
    description="Hesitation or refusal to move, often due to pain from lesions."
)
ulcers = Symptom(
    name="Ulcers",
    description="Open sores in the mouth or on the feet."
)
stomatitis = Symptom(
    name="Stomatitis",
    description="Inflammation of the mouth lining."
)
hoof_lesions = Symptom(
    name="Hoof Lesions",
    description="Lesions or sores on the hooves, leading to lameness."
)

# Animal Treatments
antibiotics = Treatment(
    name="Antibiotics", 
    method="Administer orally or via injection to combat bacterial infections."
)
hydration = Treatment(
    name="Hydration Therapy",
    method="Provide clean water and electrolyte solutions to restore fluid balance."
)
deworming = Treatment(
    name="Deworming", 
    method="Use anthelmintic drugs to eliminate internal parasites."
)
topical_ointment = Treatment(
    name="Topical Ointment", 
    method="Apply medicated cream to affected skin areas."
)
anti_inflammatory = Treatment(
    name="Anti-Inflammatory Drugs",
    method="Inject or administer orally to reduce swelling and pain."
)
pain_relief = Treatment(
    name="Pain Relief", 
    method="Use analgesics to alleviate pain symptoms."
)
wound_cleaning = Treatment(
    name="Wound Cleaning", 
    method="Clean with antiseptic solution and dress to prevent infection."
)
antipyretics = Treatment(
    name="Antipyretics", 
    method="Use fever reducers like paracetamol to lower high body temperature."
)
nutritional_supplements = Treatment(
    name="Nutritional Supplements", 
    method="Provide minerals and vitamins to boost immune function."
)
isolation = Treatment(
    name="Isolation", 
    method="Separate the sick animal to prevent disease spread."
)
supportive_care = Treatment(
    name="Supportive Care",
    method="Provide hydration, nutrition, and pain relief to support recovery."
)

# Bee Treatments
thymol_treatment = Treatment(
    name="Thymol Treatment", 
    method="Apply thymol-based products to control Varroa mites and fungal infections."
)
formic_acid = Treatment(
    name="Formic Acid Application", 
    method="Use formic acid pads or vapor to reduce mite infestations within the hive."
)
oxalic_acid = Treatment(
    name="Oxalic Acid Drip", 
    method="Drip or vaporize oxalic acid to manage Varroa destructor mites safely."
)
antiviral_probiotics = Treatment(
    name="Antiviral Probiotics", 
    method="Supplement hives with specific probiotics to boost immunity against viral infections."
)
queen_replacement = Treatment(
    name="Queen Replacement", 
    method="Replace failing or infected queens with healthy ones to restore colony health."
)
hive_relocation = Treatment(
    name="Hive Relocation", 
    method="Move the hive to a cleaner, stress-free environment to support recovery."
)
sugar_dusting = Treatment(
    name="Sugar Dusting", 
    method="Dust bees with powdered sugar to dislodge mites from their bodies."
)
essential_oils = Treatment(
    name="Essential Oils", 
    method="Administer oils like lemongrass or spearmint to support health and deter pests."
)
hive_disinfection = Treatment(
    name="Hive Disinfection", 
    method="Use acetic acid or heat treatment to disinfect empty hives before reuse."
)
protein_patties = Treatment(
    name="Protein Patties", 
    method="Provide protein supplements to support larval growth and general colony strength."
)
nosema_control = Treatment(
    name="Nosema Control", 
    method="Treat with fumagillin or herbal alternatives to reduce Nosema spore load."
)
brood_interruption = Treatment(
    name="Brood Cycle Interruption", 
    method="Temporarily remove brood to break mite reproduction cycles."
)
drone_trapping = Treatment(
    name="Drone Brood Trapping", 
    method="Use drone combs to trap and remove mites concentrated in drone brood."
)
thermal_treatment = Treatment(
    name="Thermal Hive Treatment", 
    method="Apply controlled heat to hives to eliminate mites without harming bees."
)
honey_frame_removal = Treatment(
    name="Honey Frame Removal", 
    method="Extract honey frames with potential contamination to prevent pathogen spread."
)
oxytetracycline = Treatment(
    name="Oxytetracycline",
    method="Administer oxytetracycline as an antibiotic treatment for bacterial infections such as European Foulbrood."
)
varroa_mite_control = Treatment(
    name="Varroa Mite Control",
    method="Implement integrated pest management strategies, including chemical and non-chemical methods, to control Varroa mite infestations."
)
antiviral_medications = Treatment(
    name="Antiviral Medications",
    method="Administer antiviral drugs or supportive therapies to reduce viral load and support recovery."
)

# Prevention Methods
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
    method="Providing balanced diets with essential nutrients to strengthen animals' immune systems and overall health."
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
movement_control = Prevention(
    name="Movement Control",
    method="Restrict movement of animals and enforce animal movement permits to prevent the spread of infectious diseases."
)

# Bee Prevention Methods
hive_inspection = Prevention(
    name="Hive Inspection",
    method="Regularly inspect hives for signs of disease or pests to enable early intervention."
)
apiary_hygiene = Prevention(
    name="Apiary Hygiene",
    method="Maintain cleanliness in and around the apiary to reduce the risk of disease transmission."
)
equipment_sterilization = Prevention(
    name="Equipment Sterilization",
    method="Sterilize beekeeping equipment between uses to prevent the spread of pathogens."
)
sourcing_from_healthy_hives = Prevention(
    name="Sourcing from Healthy Hives",
    method="Obtain bees and hive materials only from disease-free, reputable sources."
)
feeding_practices = Prevention(
    name="Feeding Practices",
    method="Provide supplemental feeding when natural forage is scarce to maintain colony health."
)
hive_spacing = Prevention(
    name="Hive Spacing",
    method="Space hives adequately to reduce stress and minimize disease transmission."
)
adequate_ventilation = Prevention(
    name="Adequate Ventilation",
    method="Ensure hives have proper ventilation to prevent moisture buildup and fungal diseases."
)
genetic_selection = Prevention(
    name="Genetic Selection",
    method="Breed or select bees with traits for disease resistance and hygienic behavior."
)
swarm_control = Prevention(
    name="Swarm Control",
    method="Implement management practices to prevent swarming, which can weaken colonies and spread disease."
)
pest_monitoring = Prevention(
    name="Pest Monitoring",
    method="Regularly monitor for pests such as Varroa mites to enable timely control measures."
)
hive_ventilation = Prevention(
    name="Hive Ventilation",
    method="Ensure proper airflow in the hive to reduce moisture and prevent disease."
)

# Diseases
fmd = Disease(
    name="Foot-and-Mouth Disease",
    abbreviation="FMD",
    region="Worldwide",
    description="""Foot-and-Mouth Disease (FMD) is a highly contagious viral disease that affects cloven-hoofed animals such as cattle, pigs, sheep, goats, and wild animals like deer and antelope. It is caused by an aphthovirus of the family Picornaviridae and is characterized by fever and blister-like sores on the mouth, tongue, lips, and between the hooves.

FMD spreads rapidly through direct contact with infected animals, contaminated feed, water, equipment, and even through the air over short distances. Infected animals may exhibit lameness, drooling, reluctance to move, and loss of appetite. Though the mortality rate is low in adult animals, the disease can be fatal in young animals and causes severe production losses due to decreased milk yield, weight loss, and trade restrictions.

FMD does not typically infect humans but can cause serious economic impact due to outbreaks. Control measures include quarantines, movement restrictions, culling infected animals, and routine vaccination programs in endemic areas. Early detection and strict biosecurity are critical for containment.""",
    image_url="https://example.com/fmd.jpg"
)

anthrax = Disease(
    name="Anthrax",
    abbreviation="ANTH",
    region="Worldwide",
    description="""Anthrax is a serious infectious disease caused by the bacterium *Bacillus anthracis*. It primarily affects livestock such as cattle, sheep, and goats, but can also infect humans who come into contact with infected animals or animal products. The bacterium forms durable spores that can survive in soil for decades and enter an animal's body through ingestion, inhalation, or open wounds.

In animals, anthrax can cause sudden death with minimal signs. Symptoms may include high fever, difficulty breathing, convulsions, and swelling. In some cases, blood may ooze from the mouth, nose, or anus. In humans, anthrax manifests in cutaneous, inhalational, or gastrointestinal forms, each with varying symptoms and severity.

Anthrax is a zoonotic disease and is considered a potential biological weapon due to the resilience of its spores. Preventive measures include regular livestock vaccination in endemic areas and proper disposal of carcasses. Humans can be protected through occupational safety practices and, in certain cases, vaccines.""",
    image_url="https://example.com/anthrax.jpg"
)

swine_erysipelas = Disease(
    name="Swine Erysipelas",
    abbreviation="SE",
    region="Worldwide",
    description="""Swine Erysipelas is a bacterial infection caused by *Erysipelothrix rhusiopathiae*, primarily affecting pigs. It can manifest in acute, subacute, or chronic forms, leading to a range of symptoms including fever, skin lesions, and arthritis. The disease is often associated with poor management practices and can result in significant economic losses in swine production.

In acute cases, affected pigs may exhibit sudden fever, lethargy, and skin lesions that can progress to diamond-shaped patches. Chronic infections can lead to arthritis and endocarditis, making early detection and treatment crucial.

Preventive measures include good hygiene practices, proper nutrition, and vaccination in high-risk herds. Treatment typically involves antibiotics, but prevention is the most effective strategy.""",
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
    description="""Bovine Tuberculosis is a chronic bacterial disease caused by Mycobacterium bovis, which primarily affects cattle but can infect a wide range of mammals, including humans. The bacteria spread through inhalation of infected aerosols or ingestion of contaminated feed and water. Infected animals may carry the disease asymptomatically for long periods, making it difficult to detect and control.

Clinically, signs include chronic coughing, weight loss, enlarged lymph nodes, and general weakness. In some animals, no signs are visible until the disease has progressed significantly. It often spreads insidiously within herds, increasing the risk of transmission to other animals and potentially to farm workers handling livestock.

BTB is a zoonotic disease and poses public health risks, especially in regions where milk is consumed unpasteurized. Surveillance, routine testing, and culling of infected animals are common control measures. Vaccines are under development but not yet widely available or effective in cattle populations.

Effective control requires strict biosecurity protocols, movement restrictions on affected herds, and proper carcass disposal. Regular veterinary inspections and education of livestock handlers are critical in minimizing disease incidence.""",
    image_url="https://example.com/btb.jpg"
)

brucellosis = Disease(
    name="Brucellosis",
    abbreviation="BRU",
    region="Worldwide",
    description="""Brucellosis is an infectious disease caused by bacteria of the genus Brucella, affecting cattle (B. abortus), sheep and goats (B. melitensis), pigs (B. suis), and occasionally other animals. It is a major cause of reproductive failure in livestock, with symptoms such as abortion, retained placenta, infertility, and orchitis in males.

The disease spreads through direct contact with infected reproductive fluids, ingestion of contaminated materials, or exposure to contaminated environments. Humans can contract the disease through raw dairy products or occupational exposure, leading to a condition known as undulant fever.

There is no treatment for infected livestock; eradication programs typically involve testing, culling, and vaccination. Vaccination of young animals has proven effective in controlling disease prevalence in endemic regions.

Brucellosis control requires comprehensive surveillance, public education, and intersectoral cooperation between animal and human health services. Proper handling of birth products and carcasses is crucial in preventing spread.""",
    image_url="https://example.com/brucellosis.jpg"
)

afb = Disease(
    name="American Foulbrood",
    abbreviation="AFB",
    region="Worldwide",
    description="""American Foulbrood (AFB) is a highly infectious and lethal bacterial disease affecting honeybee brood. It is caused by Paenibacillus larvae, a spore-forming bacterium that can remain viable in the environment for decades. The disease primarily targets larvae under three days old and rapidly destroys the colony if not contained.

Symptoms include sunken, perforated cappings over brood cells, a foul rotten odor, and a dark, gooey consistency of dead larvae. A hallmark sign is the formation of a stringy thread when a matchstick is inserted into the cell and withdrawn — known as the "ropy test."

AFB spreads through contaminated beekeeping equipment, robbing behavior, and drift between hives. There is no cure for the disease; control involves burning infected hives and equipment, and sometimes prophylactic antibiotics in regions where they are allowed.

Stringent biosecurity practices, regular hive inspections, and immediate action upon detection are essential to preventing large-scale outbreaks.""",
    image_url="https://example.com/afb.jpg"
)

efb = Disease(
    name="European Foulbrood",
    abbreviation="EFB",
    region="Worldwide (temperate regions)",
    description="""European Foulbrood (EFB) is a bacterial disease caused by Melissococcus plutonius that affects honeybee larvae. Unlike American Foulbrood, EFB typically impacts larvae before the cell is capped and tends to be less destructive, though it can severely weaken colonies.

Infected larvae appear twisted in their cells, yellowish or brown in color, and emit a sour odor. The disease is often associated with stress factors like poor nutrition or overcrowding, which makes colonies more susceptible.

EFB can be managed through improved hive management, feeding practices, and the use of antibiotics where permitted. Strong, well-fed colonies often recover naturally once environmental stressors are removed.

Regular monitoring, requeening with hygienic stock, and improved apiary hygiene are effective control measures.""",
    image_url="https://example.com/efb.jpg"
)

nosema = Disease(
    name="Nosema Disease",
    abbreviation="Nosema",
    region="Worldwide",
    description="""Nosema disease is caused by microsporidian parasites—Nosema apis and Nosema ceranae—that infect the midgut cells of adult bees. It results in dysentery, lethargy, reduced foraging, and colony decline. The disease often emerges during cooler, damp periods when bees are confined indoors.

Infected bees exhibit symptoms like swollen abdomens, inability to fly, and scattered dead bees around the hive entrance. Fecal streaks on the hive surface are also common. Nosema weakens immune function and shortens bee lifespan, leading to dwindling colony populations.

Treatment includes administering fumagillin (where legal) and improving hive ventilation and nutrition. Replacing old comb and reducing moisture in the hive are additional preventive strategies.

Routine monitoring, especially in early spring and fall, is critical to catch Nosema infections early before colony collapse.""",
    image_url="https://example.com/nosema.jpg"
)

chalkbrood = Disease(
    name="Chalkbrood",
    abbreviation="CB",
    region="Worldwide",
    description="""Chalkbrood is a fungal disease affecting honeybee larvae, caused by Ascosphaera apis. It thrives in cool, damp hive conditions and results in mummified larvae that resemble chalky white or gray pellets, often found at the hive entrance.

Larvae become infected after ingesting spores that germinate in the gut. As the fungus grows, it fills the larval body with a cotton-like mycelium, eventually killing it. Although not typically fatal to entire colonies, it can weaken them, reduce brood viability, and lower honey production.

Preventive strategies include improving hive ventilation, reducing moisture, and requeening with hygienic bee strains. Cleaning or replacing infected frames is also recommended.

The disease is often seasonal and can resolve when weather conditions improve and stress factors are minimized.""",
    image_url="https://example.com/chalkbrood.jpg"
)

sbv = Disease(
    name="Sacbrood Virus",
    abbreviation="SBV",
    region="Worldwide",
    description="""Sacbrood Virus (SBV) is a common viral disease in honeybee colonies, particularly affecting larvae. It prevents larvae from pupating properly, leaving them as fluid-filled sacs that dry into scale-like remains within the brood cells.

Symptoms include dead larvae with a rice-grain appearance, a lack of normal segmentation, and a stretched sac filled with clear fluid. The disease often coincides with stressful conditions like poor nutrition or weak colonies.

SBV is usually not fatal to entire colonies and can often be managed through improved colony strength, good nutrition, and hygienic queen lines. No direct treatment exists, but strong hives typically outgrow the infection.

Routine inspection and removing heavily infected brood combs help limit the spread of the virus.""",
    image_url="https://example.com/sbv.jpg"
)

dwv = Disease(
    name="Deformed Wing Virus",
    abbreviation="DWV",
    region="Worldwide",
    description="""Deformed Wing Virus (DWV) is a viral disease most commonly associated with Varroa mite infestations. It causes developmental deformities in adult bees, particularly shriveled or twisted wings, leading to impaired flight and early death.

The virus is transmitted primarily by Varroa destructor mites, which feed on bee fat bodies and spread the virus directly into their circulatory system. DWV weakens individual bees and leads to colony collapse if left unchecked.

No direct treatment exists for DWV, but controlling Varroa mite populations is the most effective management strategy. This can be achieved through mechanical, biological, or chemical interventions.

Regular mite monitoring, rotating treatments, and breeding mite-resistant bee strains are key to preventing DWV outbreaks.""",
    image_url="https://example.com/dwv.jpg"
)

# Establish relationships between diseases, species, symptoms, treatments, and preventions

# Foot-and-Mouth Disease relationships
fmd.species.extend([cow, goat, sheep, pig, horse, llama, alpaca])
fmd.symptoms.extend([
    fever, vesicles_in_mouth_and_feet, lameness, loss_of_appetite,
    excessive_salivation, reluctance_to_move, weight_loss, ulcers,
    stomatitis, hoof_lesions
])
fmd.treatments.extend([
    supportive_care, hydration, pain_relief, isolation,
    wound_cleaning, antipyretics, nutritional_supplements
])
fmd.preventions.extend([
    vaccination, quarantine, sanitation, biosecurity, movement_control,
    proper_nutrition, regular_health_checks, stress_reduction,
    proper_waste_management, good_husbandry_practices, prompt_treatment,
    vaccination_schedule, environmental_control
])

# Anthrax relationships
anthrax.species.extend([cow, goat, pig, sheep, horse, rabbit, alpaca, llama, cat, dog])
anthrax.symptoms.extend([
    fever, loss_of_appetite, lethargy, bleeding_from_orifices,
    sudden_death, swelling, respiratory_distress, abortion
])
anthrax.treatments.extend([antibiotics, isolation, hydration])
anthrax.preventions.extend([
    vaccination, quarantine, biosecurity, sanitation,
    proper_waste_management, environmental_control, rodent_control, clean_water
])

# Swine Erysipelas relationships
swine_erysipelas.species.extend([pig])
swine_erysipelas.symptoms.extend([fever, skin_rash, lameness, loss_of_appetite])
swine_erysipelas.treatments.extend([
    antibiotics, isolation, hydration, anti_inflammatory, pain_relief
])
swine_erysipelas.preventions.extend([
    vaccination, sanitation, quarantine, biosecurity, proper_nutrition,
    clean_water, regular_health_checks, prompt_treatment,
    good_husbandry_practices, vaccination_schedule, environmental_control,
    stress_reduction, proper_waste_management
])

# Rabies relationships
rabies.species.extend([dog, cat, cow, goat, sheep, pig, horse])
rabies.symptoms.extend([
    fever, behavioral_changes, excessive_salivation, paralysis,
    difficulty_swallowing, seizures, ataxia, excessive_vocalization
])
rabies.treatments.extend([isolation, supportive_care])
rabies.preventions.extend([
    vaccination, quarantine, biosecurity, regular_health_checks,
    prompt_treatment, vaccination_schedule, good_husbandry_practices,
    environmental_control
])

# Bovine Tuberculosis relationships
btb.species.extend([cow, goat, sheep, pig, horse])
btb.symptoms.extend([fever, cough, weight_loss, loss_of_appetite, lethargy])
btb.treatments.extend([antibiotics, isolation, supportive_care])
btb.preventions.extend([
    vaccination, sanitation, quarantine, biosecurity, proper_nutrition,
    clean_water, regular_health_checks, stress_reduction,
    proper_waste_management, good_husbandry_practices, prompt_treatment,
    rodent_control, environmental_control
])

# Brucellosis relationships
brucellosis.species.extend([cow, goat, sheep, pig])
brucellosis.symptoms.extend([
    fever, weight_loss, loss_of_appetite, lameness, abortion,
    swollen_udder, joint_swelling, lethargy
])
brucellosis.treatments.extend([
    antibiotics, isolation, supportive_care, anti_inflammatory,
    nutritional_supplements
])
brucellosis.preventions.extend([
    vaccination, sanitation, quarantine, biosecurity, proper_nutrition,
    regular_health_checks, good_husbandry_practices, rodent_control,
    prompt_treatment, vaccination_schedule
])

# American Foulbrood relationships
afb.species.extend([bee])
afb.symptoms.extend([
    discolored_larvae, mummified_larvae, foul_odor,
    sunken_cappings, larval_twisting
])
afb.treatments.extend([hive_disinfection, queen_replacement])
afb.preventions.extend([
    hive_inspection, apiary_hygiene, equipment_sterilization,
    sourcing_from_healthy_hives
])

# European Foulbrood relationships
efb.species.extend([bee])
efb.symptoms.extend([discolored_larvae, larval_twisting, foul_odor])
efb.treatments.extend([oxytetracycline, hive_relocation])
efb.preventions.extend([hive_inspection, apiary_hygiene, equipment_sterilization])

# Nosema relationships
nosema.species.extend([bee])
nosema.symptoms.extend([dysentery, crawling, distended_abdomen])
nosema.treatments.extend([nosema_control, protein_patties])
nosema.preventions.extend([feeding_practices, hive_ventilation, hive_spacing])

# Chalkbrood relationships
chalkbrood.species.extend([bee])
chalkbrood.symptoms.extend([mummified_larvae, discolored_larvae])
chalkbrood.treatments.extend([hive_relocation, hive_disinfection])
chalkbrood.preventions.extend([adequate_ventilation, genetic_selection, hive_spacing])

# Sacbrood Virus relationships
sbv.species.extend([bee])
sbv.symptoms.extend([sac_like_larvae, dead_brood, sunken_cappings])
sbv.treatments.extend([queen_replacement, hive_disinfection])
sbv.preventions.extend([apiary_hygiene, swarm_control, genetic_selection])

# Deformed Wing Virus relationships
dwv.species.extend([bee])
dwv.symptoms.extend([deformed_wings, paralysis, crawling])
dwv.treatments.extend([antiviral_medications, supportive_care])
dwv.preventions.extend([pest_monitoring, genetic_selection, hive_inspection])

# Add all objects to session
all_species = [cow, goat, chicken, pig, sheep, duck, horse, rabbit, turkey, alpaca, llama, cat, dog, fish, bee]

all_symptoms = [
    fever, cough, skin_rash, blood_in_stool, weight_loss, lameness, loss_of_appetite,
    diarrhea, constipation, vomiting, paralysis, lethargy, trembling, crawling,
    distended_abdomen, dysentery, discolored_larvae, mummified_larvae, foul_odor,
    sunken_cappings, larval_twisting, sac_like_larvae, deformed_wings, flightlessness,
    hairless_abdomen, reduced_flight_activity, scattered_brood, larval_death_before_capping,
    abnormal_pupa, queen_rejection, sudden_collapse, dead_brood, behavioral_changes,
    excessive_salivation, difficulty_swallowing, seizures, ataxia, excessive_vocalization,
    swollen_udder, joint_swelling, bleeding_from_orifices, sudden_death, swelling,
    respiratory_distress, abortion, vesicles_in_mouth_and_feet, reluctance_to_move,
    ulcers, stomatitis, hoof_lesions
]

all_treatments = [
    antibiotics, hydration, deworming, topical_ointment, anti_inflammatory,
    pain_relief, wound_cleaning, antipyretics, nutritional_supplements, isolation,
    supportive_care, thymol_treatment, formic_acid, oxalic_acid, antiviral_probiotics,
    queen_replacement, hive_relocation, sugar_dusting, essential_oils, hive_disinfection,
    protein_patties, nosema_control, brood_interruption, drone_trapping, thermal_treatment,
    honey_frame_removal, oxytetracycline, varroa_mite_control, antiviral_medications
]

all_preventions = [
    vaccination, sanitation, quarantine, biosecurity, proper_nutrition, vector_control,
    clean_water, regular_health_checks, stress_reduction, proper_waste_management,
    good_husbandry_practices, prompt_treatment, vaccination_schedule, rodent_control,
    environmental_control, movement_control, hive_inspection, apiary_hygiene,
    equipment_sterilization, sourcing_from_healthy_hives, feeding_practices,
    hive_spacing, adequate_ventilation, genetic_selection, swarm_control,
    pest_monitoring, hive_ventilation
]

all_diseases = [fmd, anthrax, swine_erysipelas, rabies, btb, brucellosis, afb, efb, nosema, chalkbrood, sbv, dwv]

# Add all objects to the session
session.add_all(all_species + all_symptoms + all_treatments + all_preventions + all_diseases)

# Commit the transaction
session.commit()

print("Sample data added successfully!")