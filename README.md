# 💰 Bank Statement Finance Tracker

A Python-based utility to liberate financial data from locked PDF bank statements and visualize spending habits. Built for Manjaro Linux users who need to bypass proprietary formats.

## 🚀 Features

- **PDF Decryption**: Automated unlocking of password-protected bank statements using `qpdf`.
- **Data Liberation**: Converts PDF tables to CSV using `tabula-py`.
- **Smart Processing**: Merges disparate 'Debit' and 'Credit' columns into a unified 'Amount' column.
- **Auto-Categorization**: Uses keyword mapping to group transactions (Transport, Food, etc.).
- **Visual Analytics**: Generates a Matplotlib bar chart of monthly expenses.

## 🛠️ Setup & Requirements

### System Dependencies (Arch/Manjaro)

```bash
sudo pacman -S qpdf jre-openjdk snapd
sudo snap install tabula
Python Environment
Bash

python -m venv venv
source venv/bin/activate
pip install pandas matplotlib
📈 Usage
Unlock PDF: qpdf --password=YOUR_PASS --decrypt input.pdf unlocked.pdf

Convert: /snap/bin/tabula -p all unlocked.pdf > trsx.csv

Analyze: python expenses.py

📊 Output
Summary of Income, Expenses, and Net Savings in terminal.

spending_chart.png visualizing top expense categories.
```
