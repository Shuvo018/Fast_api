# FastAPI 🚀

FastAPI is a modern, fast (high-performance) web framework for building APIs with Python.

It is built on top of:
- Starlette → for web handling
- Pydantic → for data validation

FastAPI is widely used for:
- REST APIs
- Machine Learning APIs
- Backend services
- Authentication systems
- Microservices

---

# What is FastAPI?

FastAPI is a Python framework that helps developers build APIs quickly and easily.

# Why FastAPI Matters?

<ul>
<li>Very fast</li>
<li>Beginner friendly</li>
<li>Easy to write</li>
<li>Supports async programming</li>
<li>Automatically generates Swagger API docs</li>
<li>Reduces bugs using type hints</li>
</ul>

## Benefits
✅ Fast development
✅ Clean code
✅ Easy testing
✅ Better performance
✅ Automatic validation

# What is Pydantic?

Pydantic is a Python library used for:

<ul>
<li>Data validation</li>
<li>Data parsing</li>
<li>Type checking</li>
</ul>

FastAPI uses Pydantic models to validate request data automatically.What is Pydantic?

Pydantic is a Python library used for:

<ul>
<li>Data validation</li>
<li>Data parsing</li>
<li>Type checking</li>
</ul>

FastAPI uses Pydantic models to validate request data automatically.

Example: If wrong data is sent, FastAPI automatically returns an error response.

``` python
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
```

# Create Virtual Environment (venv)
## Windows

```python -m venv venv```

## Activate venv:
```venv\Scripts\activate```

# Install FastAPI

## Install FastAPI and Uvicorn:
```pip install fastapi uvicorn```
## Run server:
```uvicorn main:app --reload```

# Open API Docs

## Swagger UI:
```http://127.0.0.1:8000/docs```

## ReDoc:
```http://127.0.0.1:8000/redoc```

Example:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}
