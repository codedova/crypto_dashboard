# Cryptocurrency Dashboard

This project is a real-time cryptocurrency dashboard built with Python, Streamlit, and the CoinGecko API. It fetches live market data for various cryptocurrencies and displays it in an interactive dashboard. The project also stores historical data in a CSV file for trend analysis.

## Features

- **Real-Time Data:** Fetches live cryptocurrency market data using the free CoinGecko API (no API key required).
- **Interactive Dashboard:** Built with Streamlit, allowing users to adjust parameters (currency, number of coins) and view data in tables and charts.
- **Historical Data Storage:** Automatically appends each refresh's data with a timestamp to `crypto_history.csv` for historical analysis.
- **Auto-Refresh:** The dashboard auto-refreshes every 60 seconds.
- **Expandable:** Easily extended with additional visualizations, filtering options, or deployment configurations.

## Requirements

- Python 3.7+
- The following Python packages:
  - `requests`
  - `pandas`
  - `streamlit`
  - `streamlit-autorefresh`

## Installation

1. **Clone the Repository:**

    git clone https://github.com/codedova/crypto_dashboard.git

      cd crypto_dashboard

2. **Create and Activate a Virtual Environment:**

      python3 -m venv venv
      source venv/bin/activate  # On Windows use: venv\Scripts\activate

3. **Install Dependencies:**

      pip install -r requirements.txt

## Running the Dashboard

To launch the interactive dashboard:

1. **Activate the Virtual Environment:**

      source venv/bin/activate

2. **Run the Streamlit App:**

      python -m streamlit run crypto_dashboard.py

3. **Interact with the Dashboard:**

- Your default web browser will open the dashboard.

- Use the sidebar to select the currency (e.g., USD, EUR, GBP) and choose the number of coins to display.

- The main section displays a table of live crypto market data along with bar charts for current price distribution and market capitalization.

- Historical data is saved automatically in crypto_history.csv and can be visualized with interactive trend charts.


