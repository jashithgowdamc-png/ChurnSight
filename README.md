# 📊 ChurnSight — AI-Powered Sales & Churn Analytics Dashboard

AI-powered sales analytics and customer churn prediction dashboard. 
Identifies at-risk customers with 83% ROC-AUC using Logistic Regression 
and visualizes key business KPIs across region, category, and segment.

---

## 🚀 Live Demo
> Run locally using the steps below

---

## 📌 Project Overview

ChurnSight is an end-to-end data science project that combines:
- **Sales Analytics** — interactive KPI dashboard with filters
- **Churn Prediction** — ML model to identify at-risk customers
- **Live Prediction** — real-time churn probability scoring

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas, NumPy | Data cleaning and feature engineering |
| Matplotlib, Seaborn | EDA and visualization |
| Scikit-learn | ML model training and evaluation |
| XGBoost | Model comparison |
| Plotly | Interactive dashboard charts |
| Streamlit | Web dashboard framework |
| Joblib | Model serialization |

---

## 📂 Project Structure

```
ChurnSight/
├── data/
│   ├── raw/          ← original datasets
│   └── processed/    ← cleaned datasets
├── notebooks/
│   └── eda.ipynb     ← EDA and ML training
├── models/
│   └── *.pkl         ← saved ML models
├── app/
│   ├── app.py        ← Sales Dashboard
│   └── pages/
│       ├── churn.py  ← Churn Analytics
│       └── predict.py← Live Prediction
├── requirements.txt
└── README.md
```

---

## 📊 Datasets

| Dataset | Source | Rows |
|---------|--------|------|
| Telco Customer Churn | [Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) | 7,032 |
| Superstore Sales | [Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) | 9,994 |

---

## 🤖 ML Models Comparison

| Model | Accuracy | ROC-AUC |
|-------|---------|---------|
| Logistic Regression | 79.53% | 83.28% 🏆 |
| Random Forest | 78.96% | 81.62% |
| XGBoost | 75.91% | 80.20% |

**Best Model → Logistic Regression (83.28% ROC-AUC)**

---

## 🔍 Key Insights

- Month-to-month contract customers churn at **42%** rate
- New customers (0-12 months tenure) are at **highest churn risk**
- Higher monthly charges correlate with **increased churn probability**
- **West region** generates highest revenue ($725K)
- **Technology category** is most profitable ($145K profit)
- Q4 consistently shows **highest sales spike** every year

---

## ⚙️ How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/jashithgowdamc-png/ChurnSight.git
cd ChurnSight
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Run the dashboard:**
```bash
cd app
streamlit run app.py
```

---

## 📈 Dashboard Pages

| Page | Description |
|------|-------------|
| 📊 Sales Dashboard | KPIs, revenue trends, regional performance |
| 🔴 Churn Analytics | Churn insights, contract analysis, feature importance |
| 🎯 Live Prediction | Real-time churn probability scoring |

---

## 👤 Author

**Jashith Gowda M C**
- LinkedIn: [linkedin.com/in/jashith-gowda-m-c-24479a310](https://linkedin.com/in/jashith-gowda-m-c-24479a310)
- GitHub: [github.com/jashithgowdamc-png](https://github.com/jashithgowdamc-png)
