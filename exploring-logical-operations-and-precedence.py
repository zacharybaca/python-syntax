
"""Task 1: Validating Calculations
Calculate the value of a particular arithmetic expression twice: once normally, and once using parentheses. Compare the two results to see if they match."""

first_expression = 2 * 1 + 3
second_expression = 2 * (1 + 3)
similar_expressions = first_expression == second_expression

print(similar_expressions)


"""Task 2: Mix and Match
Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression and predict the outcome. Then, compute the expression to see if the prediction was correct."""

random_expression = 30 + 3
compare_expression = random_expression > 35 or random_expression < 50

print(compare_expression)
