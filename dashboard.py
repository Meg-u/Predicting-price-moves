import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load or pass your merged_df here
# merged_df = ...
merged_df = pd.read_csv('notebooks/merged_df.csv', parse_dates=['Date'])
st.title("Stock Sentiment & Price Dashboard")

# Sidebar filters
stocks = merged_df['stock'].unique()
selected_stocks = st.sidebar.multiselect("Select Stock(s):", stocks, default=stocks.tolist())

date_min = merged_df['Date'].min()
date_max = merged_df['Date'].max()

selected_date_range = st.sidebar.date_input("Select Date Range:", [date_min, date_max])

# Filter data
filtered_df = merged_df[
    (merged_df['stock'].isin(selected_stocks)) &
    (merged_df['Date'] >= pd.to_datetime(selected_date_range[0])) &
    (merged_df['Date'] <= pd.to_datetime(selected_date_range[1]))
]

if filtered_df.empty:
    st.warning("No data for the selected filters.")
else:
    # Summary stats
    avg_sentiment = filtered_df['avg_sentiment'].mean()
    avg_return = filtered_df['daily_return'].mean()
    correlation = filtered_df['avg_sentiment'].corr(filtered_df['daily_return'])

    st.write(f"### Summary Statistics")
    st.write(f"- Average Sentiment: {avg_sentiment:.4f}")
    st.write(f"- Average Daily Return: {avg_return:.4%}")
    st.write(f"- Correlation (Sentiment vs Return): {correlation:.4f}")

    # Line plots for sentiment and stock price
    st.write("### Sentiment and Stock Price Over Time")
    fig, ax1 = plt.subplots(figsize=(12,6))

    sns.lineplot(data=filtered_df, x='Date', y='avg_sentiment', hue='stock', ax=ax1)
    ax1.set_ylabel('Average Sentiment')
    ax1.set_title('Average Daily Sentiment')

    st.pyplot(fig)

    fig2, ax2 = plt.subplots(figsize=(12,6))
    sns.lineplot(data=filtered_df, x='Date', y='Close', hue='stock', ax=ax2)
    ax2.set_ylabel('Closing Price')
    ax2.set_title('Stock Closing Price Over Time')

    st.pyplot(fig2)

    # Scatter plot Sentiment vs Daily Return
    st.write("### Sentiment vs Daily Return")
    fig3, ax3 = plt.subplots(figsize=(8,6))
    sns.scatterplot(x='avg_sentiment', y='daily_return', hue='stock', data=filtered_df, ax=ax3)
    ax3.axhline(0, color='grey', linestyle='--')
    ax3.axvline(0, color='grey', linestyle='--')
    st.pyplot(fig3)

    # Show filtered data table (optional)
    if st.checkbox("Show raw data"):
        st.dataframe(filtered_df)
