import streamlit as st
import pandas as pd
import datetime
from crypto_data import fetch_crypto_data
from streamlit_autorefresh import st_autorefresh

# Auto-refresh the dashboard every 60 seconds (60000 milliseconds)
st_autorefresh(interval=60000, key="datarefresh")

st.title("Cryptocurrency Dashboard")
st.markdown("Real-time crypto market data from CoinGecko. Data is stored historically.")

# Sidebar controls
vs_currency = st.sidebar.selectbox("Currency", options=["usd", "eur", "gbp"], index=0)
per_page = st.sidebar.slider("Number of Coins", min_value=5, max_value=100, value=10, step=5)

# Fetch live data
try:
    data = fetch_crypto_data(vs_currency=vs_currency, per_page=per_page)
    df_live = pd.DataFrame(data)
except Exception as e:
    st.error(f"Error fetching live data: {e}")
    df_live = pd.DataFrame()

# Function to update historical data CSV file
def update_historical_data(df, csv_file="crypto_history.csv"):
    df = df.copy()
    df["timestamp"] = datetime.datetime.now()
    try:
        existing_df = pd.read_csv(csv_file)
        updated_df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        updated_df = df
    updated_df.to_csv(csv_file, index=False)
    return updated_df

# If live data is available, update the historical CSV
if not df_live.empty:
    df_history = update_historical_data(df_live)
else:
    try:
        df_history = pd.read_csv("crypto_history.csv")
    except FileNotFoundError:
        df_history = pd.DataFrame()

# Display live data
st.subheader("Live Crypto Market Data")
if not df_live.empty:
    st.dataframe(df_live[["id", "symbol", "current_price", "market_cap", "total_volume"]])
    st.subheader("Price Distribution")
    st.bar_chart(df_live.set_index("id")["current_price"])
    st.subheader("Market Capitalization")
    st.bar_chart(df_live.set_index("id")["market_cap"])
else:
    st.write("No live data available.")

# Display historical data if available
st.subheader("Historical Data")
if not df_history.empty:
    st.dataframe(df_history)
    
    st.subheader("Historical Price Trends")
    # Let user select a coin from the historical data
    coin_options = df_history["id"].unique() if "id" in df_history.columns else []
    if len(coin_options) > 0:
        selected_coin = st.selectbox("Select a coin", options=coin_options)
        coin_history = df_history[df_history["id"] == selected_coin].copy()
        coin_history["timestamp"] = pd.to_datetime(coin_history["timestamp"])
        coin_history = coin_history.sort_values("timestamp")
        st.line_chart(coin_history.set_index("timestamp")["current_price"])
    else:
        st.write("No coin data available for historical trends.")
else:
    st.write("Historical data is not available yet.")

st.markdown("Data provided by [CoinGecko](https://www.coingecko.com/en/api).")
