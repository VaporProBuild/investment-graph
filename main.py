import matplotlib

#assuming interest rate of 5%, compounded monthly, and a 15 year mortgage the graph will show the amount of cash you will have left over if you pay the mortgage every month if you invest the money instead
interest_rate = 0.05
compound_period = 12
years = 15
house_price = 500000
down_payment = 25000    #i.e 5% of house price
mortgage = house_price - down_payment
monthly_payment = mortgage / (years * 12)
monthly_interest = interest_rate / compound_period
total_months = years * 12
investment_return_rate = 0.07

#calculate the amount of money you will have left over if you pay the mortgage every month and invest the rest
def calculate_mortgage_and_investment_return():
    #graph each month using matplotlib
    mortgage_and_investment_return = 0
    for i in range(total_months):
        mortgage_and_investment_return += monthly_payment
        mortgage_and_investment_return *= (1 + monthly_interest)
        mortgage_and_investment_return += monthly_payment
        mortgage_and_investment_return *= (1 + investment_return_rate / compound_period)
        print(mortgage_and_investment_return)
    return mortgage_and_investment_return

#print each function
print(calculate_mortgage_and_investment_return())



print('hi')