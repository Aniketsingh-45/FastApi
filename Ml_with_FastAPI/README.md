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

- **`ml.py`**: The main FastAPI application. It exposes the `/predict` and `/health` endpoints.
- **`frontend.py`**: The Streamlit frontend application. It provides a user-friendly UI to input demographic data and makes a POST request to the FastAPI backend to fetch predictions.
- **`model/`**: Contains the machine learning model logic.
  - **`model.pkl`**: A serialized scikit-learn machine learning model trained to predict insurance premiums.
  - **`predict.py`**: Helper functions to load the model and generate predictions.
- **`schema/`**: Contains Pydantic models for data validation.
  - **`user_input.py`**: Defines the `UserInput` schema, which includes automated feature engineering using `@computed_field` for `age_group` and `lifestyle_risk`.

---

## 🚀 Getting Started

### Option A: Run with Docker (Recommended)

The easiest way to run the application is using Docker. The provided `Dockerfile` will automatically set up the environment and launch both the FastAPI backend and Streamlit frontend.

1. **Build the Docker image:**
   ```bash
   docker build -t aniketsingh0306/ml_with_fastapi .
   ```

2. **Run the container (exposing both ports):**
   ```bash
   docker run -p 8000:8000 -p 8501:8501 aniketsingh0306/ml_with_fastapi
   ```

Once running:
- **Frontend (Streamlit):** http://localhost:8501
- **Backend (FastAPI Docs):** http://localhost:8000/docs

---

### Option B: Run locally without Docker

#### 1. Install Dependencies

Make sure you are in your virtual environment, then install the required packages using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

*(Alternatively, you can manually install the required packages: `pip install fastapi uvicorn pydantic scikit-learn pandas streamlit requests`)*

#### 2. Run the FastAPI Backend

Open a terminal, navigate to the `Ml_with_FastAPI` folder, and start the Uvicorn server:

```bash
uvicorn ml:app --reload
```
The backend API will now be running at: `http://127.0.0.1:8000`
You can view the interactive API docs at: `http://127.0.0.1:8000/docs`

#### 3. Run the Streamlit Frontend

Open a **new, separate terminal** window (don't close the FastAPI one!), activate your virtual environment, navigate to the `Ml_with_FastAPI` folder, and start Streamlit:

```bash
streamlit run frontend.py
```
A browser window should automatically open to `http://localhost:8501` containing the beautiful frontend UI!

---

## 💡 How It Works

1. The user inputs their `Age`, `BMI`, `Smoker Status`, and `Region` into the Streamlit UI.
2. Streamlit packages this data into a JSON payload and sends it to `http://127.0.0.1:8000/predict`.
3. FastAPI receives the request, and validates the data types and constraints using the **Pydantic** schema defined in `schema/user_input.py`.
4. Pydantic `@computed_field` decorators automatically derive new features (`age_group` and `lifestyle_risk`).
5. The `model/predict.py` module transforms the data into a Pandas DataFrame and feeds it to the pre-trained model to make a prediction.
6. The predicted category string is returned to Streamlit and displayed gracefully to the user!
