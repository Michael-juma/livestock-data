import click
from lib.models import Disease, Species, Symptom, Treatment, Prevention
from lib.database import session

@click.group()
def cli():
    """Livestock Disease Management CLI"""
    pass

@cli.command()
@click.option('--name', prompt="Disease name")
@click.option('--abbreviation', prompt="Abbreviation")
@click.option('--region', prompt="Region")
@click.option('--description', prompt="Description")
@click.option('--image_url', prompt="Image URL")
@click.option('--species_ids', prompt="Comma-separated Species IDs (e.g. 1,2,3)")
@click.option('--symptom_ids', prompt="Comma-separated Symptom IDs")
@click.option('--treatment_ids', prompt="Comma-separated Treatment IDs")
@click.option('--prevention_ids', prompt="Comma-separated Prevention IDs")
def add_disease(name, abbreviation, region, description, image_url,
                species_ids, symptom_ids, treatment_ids, prevention_ids):
    """Add a disease with related details using IDs"""

    disease = Disease(
        name=name,
        abbreviation=abbreviation,
        region=region,
        description=description,
        image_url=image_url,
    )

    # Helper function to retrieve objects by ID
    def get_items_by_ids(model, ids):
        return session.query(model).filter(model.id.in_(ids)).all()

    try:
        species_ids = [int(i.strip()) for i in species_ids.split(",") if i.strip()]
        symptom_ids = [int(i.strip()) for i in symptom_ids.split(",") if i.strip()]
        treatment_ids = [int(i.strip()) for i in treatment_ids.split(",") if i.strip()]
        prevention_ids = [int(i.strip()) for i in prevention_ids.split(",") if i.strip()]
    except ValueError:
        click.echo(" Error: All ID inputs must be comma-separated integers.")
        return

    disease.species.extend(get_items_by_ids(Species, species_ids))
    disease.symptoms.extend(get_items_by_ids(Symptom, symptom_ids))
    disease.treatments.extend(get_items_by_ids(Treatment, treatment_ids))
    disease.preventions.extend(get_items_by_ids(Prevention, prevention_ids))

    session.add(disease)
    session.commit()
    click.echo(f"Disease '{disease.name}' added successfully with ID {disease.id}")

@cli.command()
@click.option('--id', prompt="Disease ID to delete", type=int)
def delete_disease(id):
    """Delete a disease by its ID"""
    disease = session.query(Disease).get(id)
    if not disease:
        click.echo(f" No disease found with ID {id}")
        return

    session.delete(disease)
    session.commit()
    click.echo(f"Disease with ID {id} deleted successfully.")

if __name__ == "__main__":
    cli()
