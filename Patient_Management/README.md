# Patient Management System API

A lightweight, fully functional RESTful API built with [FastAPI](https://fastapi.tiangolo.com/) to manage and view patient data.

## Features

- View all patients.
- View details of a specific patient by their ID.
- Sort patient records based on specific attributes like `height`, `weight`, or `bmi` in ascending or descending order.

## Prerequisites

- Python 3.7+
- FastAPI
- Uvicorn (for running the server)

## Installation

1. Clone or download this repository.
2. Install the required dependencies:

   ```bash
   pip install fastapi uvicorn
   ```

## Usage

1. Navigate to the project directory:

   ```bash
   cd "d:/My Apps/languages/FastApi/Patient_Management"
   ```

2. Start the FastAPI server using `uvicorn`:

   ```bash
   uvicorn app:app --reload
   ```

3. The API will be available at: `http://127.0.0.1:8000`

### Interactive API Docs

FastAPI automatically generates interactive API documentation. Once the server is running, you can visit:
- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### 1. Root
- **URL:** `/`
- **Method:** `GET`
- **Description:** Welcome message.
- **Response:**
  ```json
  {"message": "Patient Management System Api"}
  ```

### 2. About
- **URL:** `/about`
- **Method:** `GET`
- **Description:** Information about the API.
- **Response:**
  ```json
  {"message": "A fully functional patient management system api"}
  ```

### 3. View All Patients
- **URL:** `/view`
- **Method:** `GET`
- **Description:** Retrieve all patient records from the `patient.json` file.

### 4. View Patient by ID
- **URL:** `/patient/{patient_id}`
- **Method:** `GET`
- **Description:** Retrieve the details of a specific patient by their `patient_id` (e.g., `P001`).
- **Response (Success):** Patient details object.
- **Response (Error - 404):** `{"detail": "Patient not found"}`

### 5. Sort Patients
- **URL:** `/sort`
- **Method:** `GET`
- **Description:** Sort the patient records by a specified metric.
- **Query Parameters:**
  - `sort_by` (required): The attribute to sort by. Allowed values: `height`, `weight`, `bmi`.
  - `order` (optional, default: `asc`): Sort order. Allowed values: `asc`, `desc`.
- **Response (Success):** A sorted list of patient objects.
- **Response (Error - 404):** Returned if an invalid `sort_by` or `order` parameter is provided.

## Data Source

The application loads its data from a local `patient.json` file located in the same directory. Ensure this file exists and is populated with valid patient data.
