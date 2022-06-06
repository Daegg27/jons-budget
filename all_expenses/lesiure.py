from expenses import Expenses
class Lesiure(Expenses):

    def __init__(self, monthly_allowance, lesiure_allowance):
        Expenses.__init__(self, monthly_allowance)
        self.lesiure_allowance = lesiure_allowance

jon = Lesiure(2300, 75)
print(f"I can spend ${jon.lesiure_allowance} on myself, which leaves me ${jon.monthly_allowance - jon.lesiure_allowance}")