# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = tip_percent/100 * meal_cost
    tax = tax_percent * meal_cost / 100
    total = round(float(tip + tax + meal_cost), 3)
    #print(round(tip,3))
    #print(round(tax,3))
    sub = tip + tax
    round((sub+meal_cost),3)
    print('%.f'%total)

solve(10.5,17,5)