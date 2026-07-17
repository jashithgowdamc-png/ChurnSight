import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="ChurnSight",
    page_icon="📊",
    layout="wide"
)

@st.cache_data
def load_data():
    sales = pd.read_csv('../data/processed/sales_featured.csv')
    churn = pd.read_csv('../data/processed/churn_featured.csv')
    return sales, churn

sales, churn = load_data()
sales['Order Date'] = pd.to_datetime(sales['Order Date'])

st.title("📊 ChurnSight — Sales Analytics Dashboard")
st.markdown("---")
st.sidebar.title("ChurnSight")
st.sidebar.markdown("---")
st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=sales['Region'].unique(),
    default=sales['Region'].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=sales['Category'].unique(),
    default=sales['Category'].unique()
)

segment = st.sidebar.multiselect(
    "Select Segment",
    options=sales['Segment'].unique(),
    default=sales['Segment'].unique()
)

year = st.sidebar.multiselect(
    "Select Year",
    options=sorted(sales['Order Year'].unique()),
    default=sorted(sales['Order Year'].unique())
)

filtered = sales[
    (sales['Region'].isin(region)) &
    (sales['Category'].isin(category)) &
    (sales['Segment'].isin(segment)) &
    (sales['Order Year'].isin(year))
]
st.subheader("Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    label="Total Revenue",
    value=f"${filtered['Sales'].sum():,.0f}"
)
col2.metric(
    label="Total Profit",
    value=f"${filtered['Profit'].sum():,.0f}"
)
col3.metric(
    label="Total Orders",
    value=f"{filtered.shape[0]:,}"
)
col4.metric(
    label="Profit Margin",
    value=f"{(filtered['Profit'].sum() / filtered['Sales'].sum() * 100):.1f}%"
)

st.markdown("---")
st.subheader("Sales Performance")
col1, col2 = st.columns(2)

with col1:
    region_data = filtered.groupby('Region')['Sales'].sum().reset_index()
    fig = px.bar(
        region_data,
        x='Region',
        y='Sales',
        color='Region',
        title='Revenue by Region'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    cat_data = filtered.groupby('Category')['Profit'].sum().reset_index()
    fig = px.bar(
        cat_data,
        x='Category',
        y='Profit',
        color='Category',
        title='Profit by Category'
    )
    st.plotly_chart(fig, use_container_width=True)
col1, col2 = st.columns(2)

with col1:
    yearly = filtered.groupby('Order Year')['Sales'].sum().reset_index()
    fig = px.line(
        yearly,
        x='Order Year',
        y='Sales',
        markers=True,
        title='Revenue Trend by Year'
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    subcat = filtered.groupby('Sub-Category')['Sales'].sum().reset_index()
    subcat = subcat.sort_values('Sales', ascending=False).head(10)
    fig = px.bar(
        subcat,
        x='Sales',
        y='Sub-Category',
        orientation='h',
        title='Top 10 Sub-Categories'
    )
    st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.caption("ChurnSight — Built with Python & Streamlit")
    