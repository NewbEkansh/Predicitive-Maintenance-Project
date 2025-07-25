# Predicitive-Maintenance-Project
Predictive Maintenance for Turbofan Engines using Machine Learning
Project Overview
This project demonstrates an end-to-end machine learning pipeline for predictive maintenance. The primary goal is to predict the Remaining Useful Life (RUL) of turbofan engines based on their time-series sensor data. By accurately forecasting when an engine will fail, maintenance can be scheduled proactively, reducing operational costs and increasing safety.

This repository contains the complete Jupyter Notebook with data loading, preprocessing, model training, and evaluation for two different machine learning models: XGBoost and a Long Short-Term Memory (LSTM) neural network.

Dataset
This project utilizes the NASA Turbofan Engine Degradation Simulation Dataset. It's a widely used benchmark dataset in the field of predictive maintenance.

Source: NASA Prognostics Center of Excellence

Description: The dataset contains multivariate time-series data from 100 turbofan engines under normal-to-failure operating conditions. Each engine starts with a different degree of initial wear and manufacturing variation, but all are of the same type. The data includes 21 sensor readings, 3 operational settings, and the time in cycles.

Methodology
The project follows a structured machine learning workflow:

Data Loading & Cleaning: The raw .txt data is loaded into a pandas DataFrame, and appropriate column names are assigned. Any empty or irrelevant columns are dropped.

Feature Engineering: The crucial target variable, Remaining Useful Life (RUL), is calculated. This is done by determining the final operational cycle for each engine and then computing how many cycles remain at each point in its history.

Exploratory Data Analysis (EDA): Sensor data is visualized to identify trends and patterns as the engines approach failure. This step confirms that the sensor readings contain predictive signals.

Data Preprocessing:

Feature Selection: Sensor columns with no variance (constant values) are identified and removed.

Scaling: All feature values are normalized to a range between 0 and 1 using MinMaxScaler. This is a critical step for the optimal performance of neural networks.

Models and Results
Two models were built to predict the RUL:

1. XGBoost (Baseline Model)
A powerful gradient boosting model was used to establish a strong performance baseline.

Purpose: To provide a benchmark against which the more complex deep learning model can be compared.

Result: Achieved an RMSE of [Enter your XGBoost RMSE here, e.g., 25.43].

2. Long Short-Term Memory (LSTM) Network (AI Model)
An LSTM, a type of Recurrent Neural Network (RNN), was built to capture temporal dependencies in the time-series data.

Architecture: The model consists of two LSTM layers with Dropout for regularization, followed by a Dense output layer.

Why LSTM? LSTMs are specifically designed to learn from sequences, making them ideal for understanding the degradation patterns in sensor data over time.

Result: Achieved an RMSE of [Enter your LSTM RMSE here, e.g., 18.91]. The lower RMSE indicates a superior predictive performance compared to the baseline.

How to Use
Clone the Repository:

git clone https://github.com/your-username/your-repository-name.git

Open in Google Colab:

Upload the .ipynb notebook file to Google Colab.

The notebook includes commands to download the dataset directly from Kaggle, so no manual download is required.

Run the Cells:

Execute the cells sequentially from top to bottom. The notebook is self-contained and will handle all dependencies, data preparation, model training, and evaluation.
