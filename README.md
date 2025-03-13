# FastAPI Project with Oracle Database

## Overview
This project is built using **FastAPI** and connects to an **Oracle Database** for backend operations.

## Features
- FastAPI for building APIs
- Oracle database connection using SQLAlchemy and cx_Oracle
- CRUD operations for managing data
- Modular structure with `main.py`, `config.py`, `database.py`, `crud.py`, `schemas.py`, and `models.py`
- Dependency management with virtual environments

## Installation & Setup

### Prerequisites
- Python (>= 3.8)
- Oracle Database (installed or accessible)
- Oracle Instant Client (for cx_Oracle support)

### Steps to Set Up
1. Clone the repository:
   ```bash
   git clone https://github.com/Yogesh-p-079/FastAPI.git
   cd FastAPI
   ```

2. Run the setup script:
   ```bash
   chmod +x setup.sh
   ./setup.sh
   ```

### Manual Setup (If Not Using setup.sh)
1. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install --upgrade pip
   pip install fastapi uvicorn pydantic sqlalchemy cx_Oracle requests
   ```

3. Set up the database connection in `database.py`:
   ```python
   DATABASE_URL = "oracle+cx_oracle://username:password@localhost:1521/XEPDB1"
   ```

4. Run the FastAPI application:
   ```bash
   uvicorn main:app --reload
   ```
   The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Structure
```
/FastAPI
│-- main.py         # FastAPI entry point
│-- config.py       # Configuration settings
│-- database.py     # Database connection setup
│-- models.py       # ORM models for SQLAlchemy
│-- schemas.py      # Pydantic schemas for request validation
│-- crud.py         # CRUD functions for database operations
│-- setup.sh        # Setup script
│-- README.md       # Project documentation
```

## API Documentation
- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Troubleshooting
- **ModuleNotFoundError: No module named 'cx_Oracle'**
  ```bash
  pip install cx_Oracle
  ```
- **Database connection issues**
  Ensure Oracle Database is running and credentials are correct.

## License
This project is open-source under the MIT License.
