# Predictive Maintenance for Aerospace Engines using Machine Learning

## 🚀 Project Overview

This project demonstrates a comprehensive, end-to-end machine learning workflow for predicting the **Remaining Useful Life (RUL)** of turbofan engines. The goal is to move from reactive to predictive maintenance, enabling proactive repairs to reduce costs and prevent catastrophic failures.

The project involved a systematic progression of models, starting with a baseline `RandomForest`, improving with `XGBoost`, and finally implementing a sequential `LSTM` network. Models were trained and validated on the NASA CMAPS datasets (`FD001` and the more complex `FD002`) to ensure robustness.

This repository contains:
* The complete **Google Colab Notebook** (`.ipynb`) with the entire data processing and model training pipeline.
* A full-stack web application (**Flask backend** + **HTML/JS frontend**) to demonstrate the model's functionality.
* The saved, trained model file (`rul_model.pkl`).

## 🔧 Technical Stack

* **Languages:** Python
* **Libraries:** pandas, scikit-learn, XGBoost, TensorFlow/Keras, joblib
* **Web Framework:** Flask
* **Frontend:** HTML, Tailwind CSS, JavaScript

## 📈 Key Results & Performance

The models were evaluated using the R-squared (R²) metric. Higher is better. The progression of model performance clearly shows the impact of using more advanced algorithms and feature engineering.

| Model                   | Dataset (Complexity) | R² Score |
| ----------------------- | -------------------- | -------- |
| RandomForest (Baseline) | FD001 (Simple)       | 65%      |
| **XGBoost (Optimized)** | **FD001 (Simple)** | **87%** |
| LSTM                    | FD001 (Simple)       | 86%      |
| **XGBoost (Optimized)** | **FD002 (Complex)** | **73%** |
| LSTM                    | FD002 (Complex)      | 71%      |

**Conclusion:** The optimized XGBoost model with advanced feature engineering provided the best performance on both datasets, demonstrating its robustness. The LSTM also performed at a high level, confirming that sequential models are a strong alternative for this type of time-series data.

## 💻 How to Run the Web Application

### 1. Prerequisites

* Python 3.x
* Git

### 2. Setup

Clone the repository and install the required packages.

```bash
# Clone the repository
git clone [https://github.com/your-username/Predictive-Maintenance-Project.git](https://github.com/your-username/Predictive-Maintenance-Project.git)
cd Predictive-Maintenance-Project

# Create and activate a virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`

# Install dependencies
pip install flask flask-cors joblib numpy pandas scikit-learn xgboost
```

### 3. Run the Application

You need to run the Flask backend server.

```bash
# From the project's root directory
python app.py
```

The server will start on `http://127.0.0.1:5000`.

### 4. Use the Predictor

Open your web browser and navigate to **`http://127.0.0.1:5000`**. You can now input sensor values to get a live RUL prediction from the model.
