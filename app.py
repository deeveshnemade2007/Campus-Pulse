
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="CampusPulse",
    page_icon="⚡",
    layout="wide"
)

# Load dataset
df = pd.read_csv("data/campus_data.csv")

# Dashboard heading
st.title("⚡ CampusPulse")
st.subheader("Smart Campus Electricity Usage Analyzer")
st.caption("Demonstration using simulated electricity data.")

# Building filter
building_list = ["All Buildings"] + sorted(
    df["Building"].unique().tolist()
)

selected_building = st.selectbox(
    "Select a building",
    building_list
)

if selected_building == "All Buildings":
    filtered_df = df.copy()
else:
    filtered_df = df[
        df["Building"] == selected_building
    ]

# Calculate metrics
total_usage = filtered_df["Electricity_kWh"].sum()
average_usage = filtered_df["Electricity_kWh"].mean()
highest_usage = filtered_df["Electricity_kWh"].max()
lowest_usage = filtered_df["Electricity_kWh"].min()

# Display summary metrics
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Usage", f"{total_usage:,.0f} kWh")
col2.metric("Average Usage", f"{average_usage:.1f} kWh/day")
col3.metric("Highest Reading", f"{highest_usage} kWh")
col4.metric("Lowest Reading", f"{lowest_usage} kWh")

st.divider()

# Daily electricity consumption
st.subheader("📈 Daily Electricity Consumption")

daily_usage = filtered_df.groupby("Day")[
    "Electricity_kWh"
].sum()

fig1, ax1 = plt.subplots(figsize=(10, 4))
daily_usage.plot(kind="line", marker="o", ax=ax1)
ax1.set_xlabel("Day")
ax1.set_ylabel("Electricity (kWh)")
ax1.grid(True, alpha=0.3)
plt.tight_layout()
st.pyplot(fig1)
plt.close(fig1)

# Compare buildings
st.subheader("🏢 Building-wise Comparison")

building_usage = df.groupby("Building")[
    "Electricity_kWh"
].mean().sort_values(ascending=False)

fig2, ax2 = plt.subplots(figsize=(9, 4))
building_usage.plot(kind="bar", ax=ax2)
ax2.set_xlabel("Building")
ax2.set_ylabel("Average Daily Usage (kWh)")
ax2.tick_params(axis="x", rotation=25)
plt.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

st.divider()

# Unusual consumption alerts
st.subheader("🚨 High Electricity Usage Alerts")

usage_limit = st.number_input(
    "Set daily usage alert limit (kWh)",
    min_value=1,
    value=150,
    step=10
)

alerts = filtered_df[
    filtered_df["Electricity_kWh"] > usage_limit
]

if alerts.empty:
    st.success("No readings exceed your selected limit.")
else:
    st.warning(f"{len(alerts)} reading(s) exceed the limit.")
    st.dataframe(alerts, use_container_width=True)

# Potential savings calculator
st.subheader("🌱 Potential Electricity Savings")

saving_percent = st.slider(
    "Target reduction in electricity usage (%)",
    min_value=0,
    max_value=50,
    value=10
)

potential_savings = total_usage * saving_percent / 100

col1, col2 = st.columns(2)
col1.metric("Current Total", f"{total_usage:,.0f} kWh")
col2.metric("Potential Savings", f"{potential_savings:,.1f} kWh")

st.caption(
    "All readings and savings estimates are simulated. "
    "This dashboard does not measure real college electricity."
)

with st.expander("View Dataset"):
    st.dataframe(filtered_df, use_container_width=True)
