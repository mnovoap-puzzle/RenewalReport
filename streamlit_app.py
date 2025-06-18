import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("Renewal_report_20250512(Sheet1).csv", encoding="ISO-8859-1")

# Title
st.title("📈 Renewal Report Dashboard")

# Sidebar filters
st.sidebar.header("🔍 Filters")

# Filter by Client
clients = st.sidebar.multiselect("Select Client(s)", df["Client Name"].unique(), default=df["Client Name"].unique())
df_filtered = df[df["Client Name"].isin(clients)]

# Filter by Product
products = st.sidebar.multiselect("Select Product(s)", df_filtered["Product"].unique(), default=df_filtered["Product"].unique())
df_filtered = df_filtered[df_filtered["Product"].isin(products)]

# Filter by Renewal Date range
df_filtered["End Date Renewal Date"] = pd.to_datetime(df_filtered["End Date Renewal Date"], errors='coerce')
min_date = df_filtered["End Date Renewal Date"].min()
max_date = df_filtered["End Date Renewal Date"].max()
date_range = st.sidebar.date_input("Renewal Date Range", [min_date, max_date])

df_filtered = df_filtered[
    (df_filtered["End Date Renewal Date"] >= pd.to_datetime(date_range[0])) &
    (df_filtered["End Date Renewal Date"] <= pd.to_datetime(date_range[1]))
]

# Show filtered data
st.subheader("📋 Filtered Data")
st.dataframe(df_filtered)

# Chart: Total amount per client
st.subheader("💰 Total Amount by Client")
st.bar_chart(df_filtered.groupby("Client Name")["Amount"].sum())

# Chart: Most contracted products
st.subheader("🧾 Most Contracted Products")
st.bar_chart(df_filtered["Product"].value_counts())

# Upcoming Renewals
st.subheader
