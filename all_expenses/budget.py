class Budget:

    def __init__(self, monthly_income):
        
        self.monthly_income = monthly_income

jon = Budget("3,000")
print(f"You have a monthly income of ${jon.monthly_income}")