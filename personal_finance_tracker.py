import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import git

class PersonalFinanceTracker:
    """
    A simple personal finance tracker that allows users to add transactions, 
    analyze spending, and summarize their budget.
    """
    
    def __init__(self):
        """
        Initializes an empty DataFrame to store financial transactions.
        """
        self.transactions = pd.DataFrame(columns=['Date', 'Category', 'Amount', 'Type'])
    
    def add_transaction(self, date, category, amount, transaction_type):
        """
        Adds a transaction to the tracker.
        
        Parameters:
        date (str): Date of the transaction
        category (str): Category of expense or income
        amount (float): Amount of money involved
        transaction_type (str): 'Income' or 'Expense'
        """
        new_transaction = pd.DataFrame({'Date': [date], 'Category': [category], 'Amount': [amount], 'Type': [transaction_type]})
        self.transactions = pd.concat([self.transactions, new_transaction], ignore_index=True)
    
    def view_transactions(self):
        """
        Returns all recorded transactions.
        """
        return self.transactions
    
    def analyze_spending(self):
        """
        Analyzes spending by category and visualizes it using a bar chart.
        """
        expenses = self.transactions[self.transactions['Type'] == 'Expense']
        category_totals = expenses.groupby('Category')['Amount'].sum()
        
        plt.figure(figsize=(8, 5))
        category_totals.plot(kind='bar', color='salmon')
        plt.title("Monthly Spending by Category")
        plt.ylabel("Amount Spent")
        plt.xticks(rotation=45)
        plt.show()
    
    def budget_summary(self, budget):
        """
        Summarizes the user's budget, showing total income, expenses, remaining budget, and savings.
        
        Parameters:
        budget (float): User-defined budget limit
        """
        total_expenses = self.transactions[self.transactions['Type'] == 'Expense']['Amount'].sum()
        total_income = self.transactions[self.transactions['Type'] == 'Income']['Amount'].sum()
        savings = total_income - total_expenses
        
        print(f"Total Income: ${total_income}")
        print(f"Total Expenses: ${total_expenses}")
        print(f"Remaining Budget: ${budget - total_expenses}")
        print(f"Total Savings: ${savings}")
    
    def setup_git(self, repo_path):
        """
        Initializes a git repository and makes an initial commit if not already set up.
        
        Parameters:
        repo_path (str): The path to the git repository
        """
        if not os.path.exists(repo_path):
            os.makedirs(repo_path)
        
        if not os.path.exists(os.path.join(repo_path, ".git")):
            repo = git.Repo.init(repo_path)
            with open(os.path.join(repo_path, "README.md"), "w") as f:
                f.write("# Personal Finance Tracker\nThis project helps track and manage personal finances.")
            repo.index.add(["README.md"])
            repo.index.commit("Initial commit: Added README and setup repository")
        else:
            print("Git repository already initialized.")
    
# Example Usage
if __name__ == "__main__":
    tracker = PersonalFinanceTracker()
    tracker.add_transaction('2025-03-01', 'Groceries', 50, 'Expense')
    tracker.add_transaction('2025-03-02', 'Salary', 2000, 'Income')
    tracker.add_transaction('2025-03-03', 'Rent', 800, 'Expense')
    tracker.add_transaction('2025-03-04', 'Entertainment', 100, 'Expense')
    
    tracker.analyze_spending()
    tracker.budget_summary(1500)
    
    # Setup Git repository (Optional)
    tracker.setup_git("./finance_tracker_repo")