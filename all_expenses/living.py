from expenses import Expenses
class Living(Expenses):

    def __init__(self, monthly_allowance, living_cost):
        Expenses.__init__(self, monthly_allowance)
        self.living_cost = living_cost

jon = Living(2300, 1200)
print(f"I must spend ${jon.living_cost} on utilities, which leaves me ${jon.monthly_allowance - jon.living_cost}")