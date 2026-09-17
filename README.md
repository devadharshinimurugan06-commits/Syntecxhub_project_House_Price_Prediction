# Syntexchub Project - House Price Prediction

## 📌 Project Overview

This project is developed as part of the **Syntexchub Machine Learning Internship**.

The objective of this project is to build a **House Price Prediction system** using Machine Learning. The project uses housing property information such as area, bedrooms, bathrooms, location, furnishing status, property type, parking, garden availability, and distance from the city center to predict house prices.

The project follows the complete Machine Learning workflow:

**Data Loading → Data Cleaning → Exploratory Data Analysis → Feature Selection → Train/Test Split → Preprocessing → Model Training → Evaluation → Model Saving → Practical Prediction → Deployment**

---

## 🎯 Project Objective

The main objectives of this project are:

- Load and understand the housing dataset.
- Clean missing and duplicate data.
- Explore the important features.
- Select relevant features for prediction.
- Split the data into training and testing sets.
- Train a **Linear Regression** model.
- Evaluate the model using **RMSE and R² Score**.
- Interpret the model coefficients.
- Save the trained Machine Learning model.
- Perform practical house price predictions.
- Deploy the prediction application using Streamlit.

---

## 📊 Dataset Information

The original dataset contains:

- **7045 rows**
- **13 columns**

### Dataset Columns

| Column | Description |
|---|---|
| House_ID | Unique house identifier |
| Property_Code | Property identifier |
| Area_Sqft | Area of the house in square feet |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Age_Years | Age of the property |
| Location | Property location |
| Furnishing_Status | Furnishing status |
| Property_Type | Type of property |
| Parking_Spaces | Number of parking spaces |
| Garden_Available | Garden availability |
| Distance_To_City_Center_Km | Distance from city center |
| Price | House price (target variable) |

---

## 🧹 Data Cleaning

The following data cleaning steps were performed:

- Checked the dataset structure and data types.
- Checked missing values.
- Identified and removed duplicate rows.
- Handled inconsistent furnishing-status values.
- Standardized categorical values.
- Verified the cleaned dataset.

After removing duplicate rows, the dataset contains:

**7001 rows and 13 columns**

The target variable `Price` does not contain missing values.

---

## 🔍 Feature Selection

The following features were selected for the Machine Learning model:

```text
Area_Sqft
Bedrooms
Bathrooms
Age_Years
Location
Furnishing_Status
Property_Type
Parking_Spaces
Garden_Available
Distance_To_City_Center_Km
