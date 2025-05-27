from sqlalchemy import Column, Integer, String, Text, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

# Bridge Tables

disease_species = Table(
    'disease_species', Base.metadata,
    Column('disease_id', ForeignKey('diseases.id'), primary_key=True),
    Column('species_id', ForeignKey('species.id'), primary_key=True)
)

disease_symptoms = Table(
    'disease_symptoms', Base.metadata,
    Column('disease_id', ForeignKey('diseases.id'), primary_key=True),
    Column('symptom_id', ForeignKey('symptoms.id'), primary_key=True)
)

disease_treatments = Table(
    'disease_treatments', Base.metadata,
    Column('disease_id', ForeignKey('diseases.id'), primary_key=True),
    Column('treatment_id', ForeignKey('treatments.id'), primary_key=True)
)

disease_preventions = Table(
    'disease_preventions', Base.metadata,
    Column('disease_id', ForeignKey('diseases.id'), primary_key=True),
    Column('prevention_id', ForeignKey('preventions.id'), primary_key=True)
)

# Main Tables

class Disease(Base):
    __tablename__ = 'diseases'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abbreviation = Column(String)
    region = Column(String)
    description = Column(Text)
    image_url = Column(String)

    species = relationship('Species', secondary=disease_species, back_populates='diseases')
    symptoms = relationship('Symptom', secondary=disease_symptoms, back_populates='diseases')
    treatments = relationship('Treatment', secondary=disease_treatments, back_populates='diseases')
    preventions = relationship('Prevention', secondary=disease_preventions, back_populates='diseases')


class Species(Base):
    __tablename__ = 'species'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    diseases = relationship('Disease', secondary=disease_species, back_populates='species')


class Symptom(Base):
    __tablename__ = 'symptoms'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text)

    diseases = relationship('Disease', secondary=disease_symptoms, back_populates='symptoms')


class Treatment(Base):
    __tablename__ = 'treatments'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    method = Column(Text)

    diseases = relationship('Disease', secondary=disease_treatments, back_populates='treatments')


class Prevention(Base):
    __tablename__ = 'preventions'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    method = Column(Text)

    diseases = relationship('Disease', secondary=disease_preventions, back_populates='preventions')
