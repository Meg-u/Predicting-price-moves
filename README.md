Predicting Price Moves Using Technical Indicators
Project Overview
This project analyzes historical stock price data from leading companies to compute technical indicators for predicting price movements. By applying financial indicators such as SMA, RSI, MACD, and Bollinger Bands on stock data, the goal is to provide a foundation for predictive modeling and trading strategy development.

Features
Data acquisition and preprocessing for seven major stocks: AAPL, AMZN, GOOG, META, MSFT, NVDA, and TSLA.

Calculation of multiple technical indicators on historical stock data.

Saving processed datasets with technical indicators for further analysis.

Jupyter notebooks to explore data, visualize indicators, and perform analysis.

Modular Python code to automate data processing across multiple stock files.

Project Structure
graphql
Copy
Edit
Predicting-price-moves/
│
├── data/
│   └── yfinance_data/                 # Raw historical stock CSV files
│
├── notebooks/
│   ├── processed_yfinance/            # Processed CSV files with indicators
│   ├── task_2_ta_analysis.ipynb       # Notebook for technical indicator calculations
│
├── scripts/
│   └── process_stocks.py              # Python script for batch processing stock files
│
├── README.md                         # Project overview and instructions (this file)
├── interim_report.pdf                # Interim project report (planned)
├── requirements.txt                  # Python dependencies
└── .gitignore                       # Files/folders ignored by git
Getting Started
Prerequisites
Python 3.8 or higher

pip package manager

Installation
Clone this repository:

bash
Copy
Edit
git clone https://github.com/Meg-u/Predicting-price-moves.git
cd Predicting-price-moves
Install required Python packages:

bash
Copy
Edit
pip install -r requirements.txt
Data Preparation
Place your downloaded raw stock data CSV files in the data/yfinance_data/ folder. The filenames should be in the format:

Copy
Edit
AAPL_historical_data.csv
AMZN_historical_data.csv
GOOG_historical_data.csv
META_historical_data.csv
MSFT_historical_data.csv
NVDA_historical_data.csv
TSLA_historical_data.csv
Usage
Processing the data
You can run the process_stocks.py script to process all stock files and compute technical indicators:

bash
Copy
Edit
python scripts/process_stocks.py
This will output processed CSV files with additional columns for indicators in notebooks/processed_yfinance/.

Exploratory Data Analysis
Open the Jupyter notebook notebooks/task_2_ta_analysis.ipynb to visualize and analyze the indicators and stock price trends.

Challenges and Notes
Environment setup was smoother compared to earlier attempts thanks to prior learning.

Installation of libraries and Git LFS configuration caused some initial delays.

Project work was balanced with final exam preparation, demonstrating good time management.

Technical indicator calculations serve as groundwork for upcoming predictive modeling.
