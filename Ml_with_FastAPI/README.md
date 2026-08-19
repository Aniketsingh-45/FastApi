# 🏥 Machine Learning with FastAPI & Streamlit

This project demonstrates how to serve a Machine Learning model using **FastAPI** for the backend API and **Streamlit** for a beautiful, interactive frontend user interface.

## 🌟 Overview

The application predicts an **Estimated Health Insurance Premium Category** (e.g., Low, Medium, High) based on user demographics and health information.

### Tech Stack
- **FastAPI**: High-performance backend API serving the ML model.
- **Streamlit**: Interactive frontend dashboard.
- **Scikit-Learn**: Machine learning library used for the predictive model.
- **Pydantic**: Robust data validation for API requests.
- **Pandas**: Data manipulation and feature structuring.

---

## 📂 Project Structure

- **`ml.py`**: The FastAPI backend application. It loads a pre-trained scikit-learn pipeline (`model.pkl`), defines the `UserInput` schema using Pydantic, creates computed features (like `lifestyle_risk` and `age_group`), and exposes a `/predict` POST endpoint.
- **`frontend.py`**: The Streamlit frontend application. It provides a user-friendly UI to input demographic data and makes a POST request to the FastAPI backend to fetch predictions.
- **`model.pkl`**: A serialized scikit-learn machine learning model trained to predict insurance premiums.

---

## 🚀 Getting Started

### 1. Install Dependencies

Make sure you are in your virtual environment, then install the required packages:

```bash
pip install fastapi uvicorn pydantic scikit-learn pandas streamlit requests
```

*(Note: The `model.pkl` provided requires `scikit-learn` version 1.9.0 or the version it was originally trained on).*

### 2. Run the FastAPI Backend

Open a terminal, navigate to the `Ml_with_FastAPI` folder, and start the Uvicorn server:

```bash
cd Ml_with_FastAPI
uvicorn ml:app --reload
```
The backend API will now be running at: `http://127.0.0.1:8000`
You can view the interactive API docs at: `http://127.0.0.1:8000/docs`

### 3. Run the Streamlit Frontend

Open a **new, separate terminal** window (don't close the FastAPI one!), activate your virtual environment, navigate to the `Ml_with_FastAPI` folder, and start Streamlit:

```bash
cd Ml_with_FastAPI
streamlit run frontend.py
```
A browser window should automatically open to `http://localhost:8501` containing the beautiful frontend UI!

---

## 💡 How It Works

1. The user inputs their `Age`, `BMI`, `Smoker Status`, and `Region` into the Streamlit UI.
2. Streamlit packages this data into a JSON payload and sends it to `http://127.0.0.1:8000/predict`.
3. FastAPI receives the request, validates the data types and constraints using **Pydantic**.
4. Pydantic `@computed_field` decorators automatically derive new features (`age_group` and `lifestyle_risk`).
5. The model transforms the data into a Pandas DataFrame and makes a prediction.
6. The predicted category string is returned to Streamlit and displayed gracefully to the user!
