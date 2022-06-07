from enum import Enum
from modules.category import Category

 # * Users should be able to update their monthly income.
 # Main manager for our budgeting
class Budget:
    pass

    def __init__(self):
        self.income = 0
        self.transactions = []


    def set_monthly_income(self, income):
        self.income = income


    # * It should know how much the user's monthly costs are. 
    def get_monthly_cost(self, month):
        monthly_costs = 0
        for txn in self.transactions:
            if txn.month == month:
                monthly_costs += txn.amount
        return monthly_costs


    def get_month_costs_by_category(self, month):

        monthly_costs = 0
        category_costs = {}
        for cat in Category:
            category_costs[cat] = 0


        for txn in self.transactions:
            if txn.month == month:
                category_costs[txn.category] += txn.amount  
        return monthly_costs



    # Ability to add new transactions
    def add_transactions(self, txn):
        self.transactions.append(txn)

    # * It should be able to tell users what percent of their monthly income is being spent in each category.
    def percent_report(self, month):
        total_costs = self.get_monthly_cost(month)
        category_costs = self.get_month_costs_by_category(month)
        category_pct_cost = {}
        for cat in category_costs:
            category_pct_cost[cat] = 100 * (category_costs[cat] / total_costs)
        return category_pct_cost

        





