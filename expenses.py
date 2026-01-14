# expenses.py

from tracker import df
from tracker import pd

def categorize_expenses(description):
    if pd.isna(description):
        return 'Other'
        
    description = str(description).lower()

    categories = {
        'Transport': ['uber', 'bolt', 'petrol', 'shell', 'fuel', 'transport'],
        'Entertainment': ['netflix', 'spotify', 'amazon prime', 'cinema'],
        'Food': ['shoprite', 'restaurant', 'kfc', 'buka', 'eat'],
        'Income': ['salary', 'deposit', 'transfer']
    }

    for category, keywords in categories.items():
        for word in keywords:
            if word in description:
                return category
            
    return 'Other'

# Changed 'Descripiton' to 'Remarks' to match your bank columns
df['Category'] = df['Remarks'].apply(categorize_expenses)

# Group by category and show totals
summary = df.groupby('Category')['Amount'].sum()
print("\n--- Spending by Category ---")
print(summary.map('₦{:,.2f}'.format)) # Formats the output nicely