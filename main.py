import matplotlib.pyplot as plt
import numpy as np

def House_Investment_Calculation(house_price, percentage_down_payment, interest_rate, years_loan_term):
    #Calculate Monthly Mortgage Payment
    #cost of house
    house_cost = house_price
    #down payment
    down_payment = house_cost * percentage_down_payment
    #loan amount
    loan_amount = house_cost - down_payment
    #monthly interest rate
    monthly_interest_rate = interest_rate / 12
    #number of payments
    number_of_payments = years_loan_term * 12
    #monthly payment
    monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)
    #total cost of house
    total_cost = monthly_payment * number_of_payments
    return total_cost, monthly_payment

def Investment_Calculator(investment_amount, interest_rate, time_invested):
    #Calculate Future Value of Investment
    #future value of investment
    return investment_amount * ((1 + interest_rate) ** time_invested) + (investment_amount * (((1 + interest_rate) ** time_invested - 1) / interest_rate))

home_appreciation_rate = 0.032
home_interest_rate = 0.05
investment_appreciation_rate = 0.1
down_payment_percentage = 0.25
cost_of_house = 500000

fifteen_year_total_cost, fifteen_year_monthly_payment = House_Investment_Calculation(cost_of_house, down_payment_percentage, home_interest_rate, 15)
fifteen_year_investment_value = Investment_Calculator(fifteen_year_monthly_payment, investment_appreciation_rate, 15)

thirty_year_total_cost, thirty_year_monthly_payment = House_Investment_Calculation(cost_of_house, down_payment_percentage, home_interest_rate, 30)
thirty_year_investment_value = Investment_Calculator(fifteen_year_monthly_payment-thirty_year_monthly_payment, investment_appreciation_rate, 30)

#price of the house after 30 years assuming 3.2% appreciation
house_price_after_30_years = cost_of_house * (1 + home_appreciation_rate) ** 30

#net worth of 15 year mortgage
fifteen_year_net_worth = fifteen_year_investment_value - fifteen_year_total_cost + house_price_after_30_years

#net worth of 30 year mortgage
thirty_year_net_worth = thirty_year_investment_value - thirty_year_total_cost + house_price_after_30_years

print(f"After 30 Years Home Worth: {house_price_after_30_years:,.0f}")
print(f"30 Year Mortgage Net Worth: {thirty_year_net_worth:,.0f}\n30 Year Investment Value {thirty_year_investment_value:,.0f}")
print(f"15 Year Mortgage Net Worth: {fifteen_year_net_worth:,.0f}\n15 Year Investment Value {fifteen_year_investment_value:,.0f}")

#Plotting
#plot the data as stacked bar chart
types_of_mortgage = ['30 Year Mortgage Net Worth', '15 Year Mortgage Net Worth']

categories = {
    "Investment Value": [fifteen_year_investment_value, thirty_year_investment_value],
    "House Price After 30 Years": [house_price_after_30_years, house_price_after_30_years],
    "Total Cost of House": [fifteen_year_total_cost, thirty_year_total_cost]
}