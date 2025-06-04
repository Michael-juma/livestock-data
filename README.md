
#  Livestock Disease Management System

A command-line interface (CLI) tool and database backend for managing livestock diseases, symptoms, species affected, treatments, and preventions. Built using Python, SQLAlchemy ORM, and Click for CLI functionality.

---

## Features

- Add a disease with full details (description, species, symptoms, treatments, preventions)
- View disease details by ID or name
- Delete diseases by ID
- Extensible for future features like updates or listing all records

---

## Technologies Used

- **Python 3.8+**
- **SQLAlchemy**
- **SQLite3** (or any SQLAlchemy-supported database)
- **Click** (Python CLI framework)

---

## Project Structure
livestock-data/
├── lib/
│ ├── init.py
│ ├── cli.py # CLI commands
│ ├── models.py # ORM models (Disease, Species, Symptom, etc.)
│ ├── database.py # DB engine and session
├── migrations/ 
├── seed.py # Optional: Seeding database
├── README.md


---

##  Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Michael-juma/livestock-data.git
cd livestock-data
