# tracker.py

import pandas as pd

def load_data(filename):
    df = pd.read_csv(filename)
    
    # Use raw strings (r'') to avoid SyntaxWarnings
    df['Debits'] = pd.to_numeric(df['Debits'].replace(r'[\,]', '', regex=True)).fillna(0)
    df['Credits'] = pd.to_numeric(df['Credits'].replace(r'[\,]', '', regex=True)).fillna(0)
    
    df['Amount'] = df['Credits'] - df['Debits']
    return df

df = load_data('trsx.csv')

income = df[df['Amount'] > 0]['Amount'].sum()
expenses = df[df['Amount'] < 0]['Amount'].sum()

print(f"💰 Total Income: ₦{income:,.2f}")
print(f"💸 Total Expenses: ₦{abs(expenses):,.2f}")
print(f"📉 Net Savings: ₦{(income + expenses):,.2f}")