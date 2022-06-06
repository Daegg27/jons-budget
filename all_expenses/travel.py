from expenses import Expenses
class Travel(Expenses):

    def __init__(self, monthly_allowance, planned_vacations):
        Expenses.__init__(self, monthly_allowance)
        self.planned_vacations = planned_vacations

jon = Travel(2300, 50)
print(f"I want to set aside ${jon.planned_vacations} each month for vacation, which leaves me ${jon.monthly_allowance - jon.planned_vacations}")