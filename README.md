# FastAPI Patient Management API 🚀

A hands-on learning project for building REST APIs with **FastAPI** and **Pydantic** in Python. This repo covers core FastAPI concepts — routing, path/query parameters, data validation, custom validators, nested models, serialization, and computed fields — all applied to a patient management use case.

---

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                        CLIENT / FRONTEND                        │
│              (Browser, Postman, curl, React App)                │
└────────────────────────────┬────────────────────────────────────┘
                             │  HTTP Request (GET / POST / PUT)
                             ▼
┌─────────────────────────────────────────────────────────────────┐
│                     FASTAPI APPLICATION                         │
│                                                                 │
│   ┌─────────────┐    ┌──────────────┐    ┌──────────────────┐  │
│   │   Router    │───▶│  Pydantic    │───▶│  Business Logic  │  │
│   │  (Routes)   │    │  Validation  │    │  (Endpoints)     │  │
│   └─────────────┘    └──────────────┘    └────────┬─────────┘  │
│                                                   │             │
│   ┌──────────────────────────────────────────────▼──────────┐  │
│   │              Middleware / Exception Handlers             │  │
│   │         (HTTPException 400 / 404, Error Responses)      │  │
│   └──────────────────────────────────────────────────────────┘  │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                         BACKEND / DATA                          │
│                                                                 │
│              patients.json  ◀──▶  json.load() / json.dump()    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
                              │
                              │  JSON Response
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                    AUTOMATIC API DOCS                           │
│         Swagger UI → http://127.0.0.1:8000/docs                 │
│         ReDoc      → http://127.0.0.1:8000/redoc                │
└─────────────────────────────────────────────────────────────────┘
```

**Flow:** The client sends an HTTP request → FastAPI routes it to the correct endpoint → Pydantic validates the incoming data → business logic runs (reads/writes `patients.json`) → a JSON response is returned. If validation fails, FastAPI automatically sends a structured `422` error — no extra code needed.

---

## 📁 Project Structure

```
Fast_api/
│
├── main.py                # Core REST API — routing, path & query params, JSON data
├── main02.py              # Extended API examples
├── fast_api_pydantic.py   # Pydantic BaseModel with Field constraints & type checks
├── field_validator.py     # Custom @field_validator decorators (email, name, age)
├── model_validator.py     # Cross-field @model_validator logic
├── nested_models.py       # Nested Pydantic models
├── computed_fields.py     # @computed_field for derived properties (e.g., BMI)
├── serialization.py       # model_dump() / model_dump_json() serialization
├── patients.json          # Sample patient data store
├── Fast_api_doc.docx      # Project documentation
└── venv14/                # Virtual environment
```

---

## ✨ Features

| Feature | File | Description |
|---|---|---|
| REST Routing | `main.py` | GET endpoints with path & query parameters |
| JSON Data Store | `main.py` | Read/write patient records from `patients.json` |
| Patient Sorting | `main.py` | Sort patients by `height`, `weight`, or `bmi` (asc/desc) |
| Pydantic Models | `fast_api_pydantic.py` | Strict type validation with `Field`, `EmailStr`, `AnyUrl` |
| Field Validators | `field_validator.py` | `@field_validator` for email domains, name casing, age range |
| Model Validators | `model_validator.py` | Cross-field validation with `@model_validator` |
| Nested Models | `nested_models.py` | Nested Pydantic models for complex schemas |
| Computed Fields | `computed_fields.py` | `@computed_field` for auto-derived values like BMI |
| Serialization | `serialization.py` | `model_dump()` and `model_dump_json()` for output control |

---

## ⚡ Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/Shuvo018/Fast_api.git
cd Fast_api
```

### 2. Create & Activate a Virtual Environment

```bash
# Create
python -m venv venv14

# Activate (Windows)
venv14\Scripts\activate

# Activate (macOS/Linux)
source venv14/bin/activate
```

### 3. Install Dependencies

```bash
pip install fastapi uvicorn pydantic[email]
```

### 4. Run the Server

```bash
uvicorn main:app --reload
```

---

## 🌐 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/` | Health check — Hello World |
| `GET` | `/about` | About message |
| `GET` | `/view` | List all patients |
| `GET` | `/patient/{patient_id}` | Get a specific patient by ID (e.g., `P001`) |
| `GET` | `/sort?sort_by=bmi&order=asc` | Sort patients by `height`, `weight`, or `bmi` |

### Example Request

```bash
curl http://127.0.0.1:8000/patient/P001
```

### Example Sort Request

```bash
curl "http://127.0.0.1:8000/sort?sort_by=weight&order=desc"
```

---

## 📖 API Documentation

FastAPI automatically generates interactive API docs — no extra setup needed.

| UI | URL |
|---|---|
| **Swagger UI** | http://127.0.0.1:8000/docs |
| **ReDoc** | http://127.0.0.1:8000/redoc |

---

## 🔍 Pydantic Concepts Covered

Pydantic is a Python library used for:

<ul>
<li>Data validation</li>
<li>Data parsing</li>
<li>Type checking</li>
</ul>

FastAPI uses Pydantic models to validate request data automatically.

Example: If wrong data is sent, FastAPI automatically returns an error response.



### Basic Model with Field Constraints (`fast_api_pydantic.py`)

```python
from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: Annotated[str, Field(max_length=50)]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=1, lt=25)
    weight: Annotated[float, Field(gt=1, strict=True)]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]
```

### Custom Field Validators (`field_validator.py`)

```python
from pydantic import field_validator

@field_validator('email')
@classmethod
def email_validator(cls, value):
    valid_domains = ['gmail.com', 'yahoo.com']
    domain = value.split('@')[-1]
    if domain not in valid_domains:
        raise ValueError('Not a valid domain')
    return value

@field_validator('name')
@classmethod
def transform_name(cls, value):
    return value.upper()  # Auto-capitalize names

@field_validator('age', mode='before')
@classmethod
def validate_age(cls, value):
    if 0 < value < 100:
        return value
    raise ValueError('Age must be between 0 and 100')
```

---

## 🛠️ Tech Stack

- **[FastAPI](https://fastapi.tiangolo.com/)** — Modern Python web framework
- **[Pydantic v2](https://docs.pydantic.dev/)** — Data validation using Python type hints
- **[Uvicorn](https://www.uvicorn.org/)** — ASGI server
- **Python 3.10+**

---

## 📚 What I Learned

This project covers the FastAPI + Pydantic learning path:

1. Setting up a FastAPI project and running it with Uvicorn
2. Defining routes with `@app.get()` and returning JSON responses
3. Using **path parameters** (`/patient/{patient_id}`) and **query parameters** (`/sort?sort_by=bmi`)
4. Reading and serving data from a JSON file
5. Using `HTTPException` for proper 404/400 error handling
6. Building **Pydantic models** with `BaseModel`, `Field`, `EmailStr`, and `AnyUrl`
7. Writing **`@field_validator`** decorators for custom field-level rules
8. Writing **`@model_validator`** for cross-field (multi-field) validation
9. Working with **nested Pydantic models**
10. Using **`@computed_field`** to auto-derive values like BMI
11. Serializing models with `model_dump()` and `model_dump_json()`

---

## 📄 License

This project is open-source and available for learning purposes.

---

*Built with ❤️ while learning FastAPI*
