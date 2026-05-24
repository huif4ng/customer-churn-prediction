# Customer Churn Prediction
This project predicts customer churn for a telecom company using the Telco Customer Churn dataset from Kaggle. The goal is to identify customers who are likely to leave the subscription service and understand the factors influencing churn.

## Project Overview
Customer churn is one of the biggest challenges for subscription-based businesses.  
In this project, I built a machine learning model to predict whether a customer will churn based on demographic information, account details, and service usage.

The project includes:

- Data cleaning & preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Model training & evaluation
- Churn prediction insights

## Dataset
[Telco Customer Churn](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)

### Features include:
- Customer demographics
- Internet services
- Contract type
- Payment method
- Monthly charges
- Total charges
- Tenure
- Churn status

## Exploratory Data Analysis
Overall Churn Rate: 26.54%

Users who churned are significantly different (t-test p-value < 0.05) from those who did not in terms of:
- Monthly Charges
- Total Charges
- Tenure --- churn rate is higher for th ose with lower tenures. (Pearson's correlation: -0.9)

There is a siginificant association (Chi-square p-value < 0.05) between Churn and:
- Senior Citizens --- churn rate 41.7%
- Partner --- Non-partners churn rate: 33.0%
- Dependents --- Non-dependents churn rate: 31.3%
- MultipleLines --- Those with multiple lines have a slightly higher churn rate: 28.6%
- InternetService --- Fiber optic highest churn rate: 41.9%
- OnlineSecurity --- Those without online security has highest churn rate: 41.8%
- OnlineBackup --- Those without online backup has highest churn rate: 40.0%
- DeviceProtection --- Those without device protection has highest churn rate: 40.0%
- TechSupport --- Those without tech support has highest churn rate: 41.6%
- StreamingTV --- Those without streaming TV has highest churn rate: 33.5%
- StreamingMovies --- Those without streaming movies has highest churn rate: 33.7%
- Contract --- Month-to-month contract has highest churn rate: 42.7%
- PaperlessBilling --- churn rate 33.6%
- PaymentMethod --- Electronic check has the highest churn rateL 45.3%

## Data Preprocessing
Steps performed:

1. Removed missing or invalid values
2. Converted categorical variables using encoding
3. Scaled numerical features
4. Split data into training and testing sets

## Machine Learning Models

Models tested:
- Logistic Regression
- Random Forest
- XGBoost

### Evaluation Metrics
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC Score

## Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC
|------|------|
| Logistic Regression | 80% | 65% | 55% | 59% | 84 %
| Random Forest | 79% | 63% | 50% | 56% | 82%
| XGBoost | 78% | 60% | 51% | 55% | 82%

Logistic regresion achieved the best overall performance for churn prediction.


## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/huif4ng/customer-churn-prediction.git
```

### 2. Download the dataset and place them in `data/` folder.

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Repository Structure
```bash
customer-churn-prediction/
│
├── data/
│   └── data.csv
│   └── sample_data.csv
│   
├── models/
│   └── churn_model.pkl
│   └── feature_names.pkl
│   └──scaler.pkl
│
├── notebooks/
│   └── 01_eda.ipynb
│   └── 02_models.ipynb
│
├── requirements.txt
├── README.md
└── .gitignore
├── app.py
```