# FastAPI Product Management API

## Overview
This project is a **FastAPI-based Product Management API** that connects to an **Oracle Database** using SQLAlchemy and cx_Oracle.

## Features
- CRUD operations for Product management
- Uses **FastAPI** for API development
- **SQLAlchemy** ORM for database interactions
- **Pydantic** for request validation
- **Oracle Database** as the backend

## Prerequisites
- Python 3.8 or higher
- Oracle Database installed or accessible
- Oracle Instant Client (for cx_Oracle support)
- Git

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Yogesh-p-079/your-project.git
cd your-project
```

### 2. Set Up Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install --upgrade pip
pip install fastapi uvicorn sqlalchemy pydantic cx_Oracle
```

### 4. Set Up Database Connection
Modify `database.py` with your Oracle Database credentials:
```python
DATABASE_URL = "oracle+cx_oracle://username:password@localhost:1521/XEPDB1"
```

### 5. Run the Application
```bash
uvicorn main:app --reload
```
API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## Project Structure
```
/your-project
│-- main.py         # FastAPI entry point
│-- config.py       # Configuration settings
│-- database.py     # Database connection setup
│-- models.py       # ORM models for SQLAlchemy
│-- schemas.py      # Pydantic schemas for request validation
│-- crud.py         # CRUD operations for database
│-- setup.sh        # Setup script
│-- README.md       # Project documentation
```

## API Endpoints
- **List Products**: `GET /product/list` (with pagination)
- **Get Product Info**: `GET /product/{pid}/info`
- **Add Product**: `POST /product/add`
- **Update Product**: `PUT /product/{pid}/update`

## Troubleshooting
- **ModuleNotFoundError: No module named 'cx_Oracle'**
  ```bash
  pip install cx_Oracle
  ```
- **Database connection issues**
  Ensure Oracle Database is running and credentials are correct.

## License
This project is open-source under the MIT License.
