# FastAPI Projects Repository

This repository contains my FastAPI applications and experiments. It serves as a collection of different APIs I've built using the FastAPI framework.

## Repository Structure

- **`main.py`**: A simple, introductory FastAPI application featuring basic endpoints (`/` and `/about`).
- **`Patient_Management/`**: A more comprehensive project that implements a fully functional REST API for managing patient data. It reads from a JSON file and includes endpoints for viewing and sorting patients.
- **`pydantic/`**: A collection of scripts demonstrating various features of the Pydantic data validation library, from basic models to advanced custom validators and serialization.
- **`myenv/`**: The local Python virtual environment used for managing project dependencies.

## Prerequisites

To run the applications in this repository, you'll need:

- Python 3.7+
- [FastAPI](https://fastapi.tiangolo.com/)
- [Uvicorn](https://www.uvicorn.org/)

You can install the required packages using pip:

```bash
pip install fastapi uvicorn
```

## Running the Applications

### 1. Basic Application (`main.py`)
This script contains a basic "Hello World" style API with an about route.

To run it, navigate to the root directory (`FastApi`) and execute:

```bash
uvicorn main:app --reload
```
- Access the API at: `http://127.0.0.1:8000`
- Access the About endpoint at: `http://127.0.0.1:8000/about`

### 2. Patient Management API
This is a more robust application that manages patient information. 

To run it, navigate to the `Patient_Management` directory:

```bash
cd Patient_Management
uvicorn app:app --reload
```

For more detailed information on its specific endpoints and features, see the [Patient Management README](./Patient_Management/README.md).

## Interactive Documentation

One of the great features of FastAPI is that it automatically generates interactive API documentation. For any running application, you can view the docs at:

- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`
