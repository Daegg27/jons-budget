from expenses import Expenses

class Food(Expenses):

    def __init__(self, monthly_allowance, food_allowance):
        Expenses.__init__(self, monthly_allowance)
        self.food_allowance = food_allowance
    
jon = Food(2300, 124)
print(f"I can spend ${jon.food_allowance} on groceries which leaves me ${jon.monthly_allowance - jon.food_allowance}")

        
