import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
from sklearn.preprocessing import LabelEncoder

st.set_page_config(
    page_title="ChurnSight - Churn Analytics",
    page_icon="🔴",
    layout="wide"
)

@st.cache_data
def load_data():
    churn = pd.read_csv(r'C:\Users\jashi\OneDrive\Desktop\ChurnSight\data\processed\churn_featured.csv')
    return churn

churn = load_data()

st.title("🔴 ChurnSight — Churn Analytics")
st.markdown("---")


#ENCODE FOR MODEL
le = LabelEncoder()
churn_encoded = churn.copy()
cat_cols = churn_encoded.select_dtypes(include='object').columns.tolist()
cat_cols = [col for col in cat_cols if col != 'tenure_group']
for col in cat_cols:
    churn_encoded[col] = le.fit_transform(churn_encoded[col].astype(str))


#KPI CARDS
total_customers = churn.shape[0]
churned = churn['Churn'].sum()
churn_rate = (churned / total_customers * 100)
retained = total_customers - churned

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", f"{total_customers:,}")
col2.metric("Churned Customers", f"{churned:,}")
col3.metric("Churn Rate", f"{churn_rate:.1f}%")
col4.metric("Retained Customers", f"{retained:,}")

st.markdown("---")


#CHURN CHARTS ROW 1
st.subheader("Churn Insights")
col1, col2 = st.columns(2)

with col1:
    churn_counts = churn['Churn'].value_counts().reset_index()
    churn_counts.columns = ['Churn', 'Count']
    churn_counts['Churn'] = churn_counts['Churn'].map({0: 'No Churn', 1: 'Churn'})
    fig = px.pie(
        churn_counts,
        names='Churn',
        values='Count',
        color_discrete_sequence=['green', 'red'],
        title='Churn Distribution'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    contract_churn = churn.groupby('Contract')['Churn'].mean().reset_index()
    contract_churn['Churn'] = contract_churn['Churn'] * 100
    fig = px.bar(
        contract_churn,
        x='Contract',
        y='Churn',
        color='Contract',
        title='Churn Rate by Contract Type (%)'
    )
    st.plotly_chart(fig, use_container_width=True)


#CHURN CHARTS ROW 2
col1, col2 = st.columns(2)

with col1:
    tenure_churn = churn.groupby('tenure_group')['Churn'].mean().reset_index()
    tenure_churn['Churn'] = tenure_churn['Churn'] * 100
    fig = px.bar(
        tenure_churn,
        x='tenure_group',
        y='Churn',
        color='tenure_group',
        title='Churn Rate by Tenure Group (%)'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(
        churn,
        x='Churn',
        y='MonthlyCharges',
        color='Churn',
        color_discrete_map={0: 'green', 1: 'red'},
        title='Monthly Charges vs Churn'
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")


#FEATURE IMPORTANCE
st.subheader("Top Factors Driving Churn")

model = joblib.load(r'C:\Users\jashi\OneDrive\Desktop\ChurnSight\models\logistic_regression.pkl')

X = churn_encoded.drop(columns=['Churn', 'tenure_group'])
importance = pd.Series(
    abs(model.coef_[0]),
    index=X.columns
).sort_values(ascending=False).head(10).reset_index()
importance.columns = ['Feature', 'Importance']

fig = px.bar(
    importance,
    x='Importance',
    y='Feature',
    orientation='h',
    color='Importance',
    title='Top 10 Features Driving Churn'
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("ChurnSight — Built with Python & Streamlit")