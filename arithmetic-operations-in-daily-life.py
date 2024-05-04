
"""Task 1: Grocery Store Math
Calculate the total cost of three items you'd commonly find in a grocery store, given their individual prices. For example, what would be the cost of bread, peanut butter, and jelly be? Prices don't need to be realistic """

price_of_bread = 3.00
price_of_peanut_butter = 5.00
price_of_jelly = 3.50

total_price = price_of_bread + price_of_peanut_butter + price_of_jelly

print(total_price)


"""Task 2: Bank Interest
If you have a savings account with a particular initial amount and a fixed yearly interest rate, calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700."""

total_in_savings = 10000
interest_rate = 0.07
interest_accumulated = total_in_savings * interest_rate
total_after_interest = total_in_savings + interest_accumulated

print(total_after_interest)
