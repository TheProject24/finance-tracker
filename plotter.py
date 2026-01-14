# plotter.py

import matplotlib.pyplot as plt
from expenses import summary as expense_summary

if not expense_summary.empty:

    plt.figure(figsize=(10, 6))
    expense_summary.sort_values(ascending=False).plot(kind='bar', color='skyblue', edgecolor='navy')

    plt.title('Spending by category', fontsize=15)
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Amount (₦)', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()

    plt.savefig('spending_hart.png')
    print("\n Chart saved as 'spending_chart.png")

else:
    print('\nNo expenses found to plot')