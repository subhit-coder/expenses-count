import streamlit as st
import pandas as pd
import csv
from datetime import datetime

FILE_NAME = "expenses.csv"

# Function to add expense
def add_expense(date, category, amount, notes):
    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, notes])

# Function to load expenses
def load_expenses():
    try:
        df = pd.read_csv(FILE_NAME, names=["Date", "Category", "Amount", "Notes"])
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=["Date", "Category", "Amount", "Notes"])

# 🎨 Page Styling
st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="centered")

st.markdown(
    """
    <style>
    body {
        background: linear-gradient(to right, #1f4037, #99f2c8);
        color: white;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stTextInput>div>input, .stNumberInput>div>input, .stTextArea>div>textarea {
        border-radius: 8px;
        border: 2px solid #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
st.sidebar.title("💼 Expense Tracker")
menu = st.sidebar.radio("Navigate", ["➕ Add Expense", "📋 View Expenses", "💰 Summary"])

# Add Expense Page
if menu == "➕ Add Expense":
    st.title("➕ Add New Expense")
    date = st.date_input("📅 Select Date")
    category = st.selectbox("🏷️ Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("💰 Amount", min_value=0.0, format="%.2f")
    notes = st.text_area("📝 Notes")

    if st.button("Add Expense"):
        add_expense(date.strftime("%Y-%m-%d"), category, amount, notes)
        st.success("✅ Expense added successfully!")

# View Expenses Page
elif menu == "📋 View Expenses":
    st.title("📋 All Expenses")
    df = load_expenses()
    if df.empty:
        st.warning("⚠️ No expenses found yet!")
    else:
        # ✅ FIX: no background_gradient
        st.dataframe(df)

# Summary Page
elif menu == "💰 Summary":
    st.title("💰 Total Summary")
    df = load_expenses()
    if df.empty:
        st.warning("⚠️ No expenses found yet!")
    else:
        total = df["Amount"].astype(float).sum()
        st.metric("Total Spent", f"₹{total:.2f}")

