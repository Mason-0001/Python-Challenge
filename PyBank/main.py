"""
In this Challenge, you are tasked with creating a Python script to analyze the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyzes the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period
"""
import pandas as pd

data = pd.read_csv('PyBank/Resources/budget_data.csv')

total_months = len(data)
net_total = data["Profit/Losses"].sum()
ave_chg = round(data["Profit/Losses"].diff().mean(),2)
g_inc_m = data["Date"][data["Profit/Losses"].diff().argmax()]
g_inc_p = round(data["Profit/Losses"].diff().max())
g_dec_m = data["Date"][data["Profit/Losses"].diff().argmin()]
g_dec_p = round(data["Profit/Losses"].diff().min())

print(f"""
Financial Analysis

----------------------------

Total Months: {total_months}

Total: ${net_total}

Average Change: ${ave_chg}

Greatest Increase in Profits: {g_inc_m} (${g_inc_p})

Greatest Decrease in Profits: {g_dec_m} (${g_dec_p})""")