# 🔥 Algerian Forest Fire Prediction

This is a Machine Learning project designed to predict the Fire Weather Index (FWI) based on various meteorological metrics and indices. The model was trained and evaluated using the Algerian Forest Fires dataset.

## 🚀 Key Features

- **Data Exploration & Preprocessing**: Includes a comprehensive Jupyter Notebook (`algeriancleaning.ipynb`) focusing on Exploratory Data Analysis (EDA), handing missing values, and Feature Selection.
- **Machine Learning Architecture**: Built using a **Ridge Regression** model combined with a **Standard Scaler** pipeline to ensure accurate, scaled coefficient evaluations.
- **Dual User Interfaces**:
  - **Flask Web App:** A RESTful web application integrating standard HTML templates (`/templates`).
  - **Streamlit App:** A highly interactive, sleek, and modern frontend dashboard for making streamlined predictions.

## 📁 Project Structure

* `application.py` — The core Flask backend implementation.
* `streamlit_app.py` — The modern Streamlit interface.
* `algeriancleaning.ipynb` — The Data Cleaning and Model Training notebook.
* `ridge.pkl` / `scaler.pkl` — Pickled models for deployment.
* `Algerian_forest_fires_dataset_UPDATE.csv` — Full Dataset context.
* `templates/` — HTML templates for the Flask application.

## 💻 How to Run the Project

Ensure you have your environment set up and the necessary libraries installed (`pandas`, `numpy`, `scikit-learn`, `flask`, `streamlit`).

### 1. The Modern Streamlit App (Recommended)
This launches a beautiful, dynamic split-column interface.
```bash
streamlit run streamlit_app.py
```
**Access:** `http://localhost:8501`

### 2. The Flask Web Application
Because the main file is named `application.py`, you can run it as a regular python script:
```bash
python application.py
```
*(Alternatively, you can use: `flask --app application run`)*

**Access:** `http://127.0.0.1:5000`

## 📊 Dataset Inputs Explained

The model requires the following physical and circumstantial indices to form a prediction:
- **Temperature (°C)**, **RH (Relative Humidity %)**, **Ws (Wind Speed km/h)**, **Rain (mm)**
- **FFMC, DMC, ISI**: Fine Fuel Moisture Code, Duff Moisture Code, Initial Spread Index
- **Classes**: Categorical representation of states (Fire / Not Fire)
- **Region**: Represents the region of data capture (Bejaia or Sidi Bel-abbes)
