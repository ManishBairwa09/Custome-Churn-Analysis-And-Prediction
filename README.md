# Customer Churn Analysis & Prediction 📉

ML project that predicts whether a customer will churn (leave) using classification models, with an interactive Streamlit web app.

## 🔍 Problem Statement
Telecom companies lose revenue when customers leave. This project predicts which customers are likely to churn so the company can take preventive action.

## 🚀 What it does
- Analyzes customer data (usage patterns, contract type, billing info)
- Trains and compares multiple ML classification models
- Predicts churn probability for new customers
- Interactive web app to input customer details and get instant prediction

## 🛠️ Tech Stack
| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas & NumPy | Data analysis & cleaning |
| Scikit-learn | ML models (Logistic Regression, Random Forest) |
| Matplotlib & Seaborn | Data visualization & EDA |
| Streamlit | Interactive web app |
| Jupyter Notebook | Experimentation & analysis |

## 📁 Project Structure
```
├── notebook.ipynb           # EDA + model training + evaluation
├── app.py                   # Streamlit web app
├── customer_churn_data.csv  # Dataset
├── model.pkl                # Trained ML model
├── scaler.pkl               # Feature scaler
└── Project_Report.pdf       # Detailed report
```

## ⚙️ How to Run
1. Clone the repo
2. Install dependencies:
```bash
pip install pandas numpy scikit-learn streamlit matplotlib seaborn
```
3. Run the app:
```bash
streamlit run app.py
```

## 📊 Models Used
- Logistic Regression
- Random Forest Classifier

## 🎯 Key Features
- Exploratory Data Analysis (EDA) with visualizations
- Feature engineering & preprocessing
- Model comparison & evaluation (Accuracy, Precision, Recall, F1)
- Deployed interactive prediction app via Streamlit
