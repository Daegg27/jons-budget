from expenses import Expenses
class Savings(Expenses):

   def __init__(self, monthly_allowance, planned_savings):
        Expenses.__init__(self, monthly_allowance)
        self.planned_savings = planned_savings

jon = Savings(2300, 100)
print(f"I want to save at least ${jon.planned_savings} each month, which leaves me ${jon.monthly_allowance - jon.planned_savings}")