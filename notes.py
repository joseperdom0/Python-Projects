'''Short-circuit evaluation

The last thing to mention is that logical operators in Python are short-circuited. That's why they are also called lazy. That means that the second operand in such an expression is evaluated only if the first one is not sufficient to evaluate the whole expression.

    x and y returns x if x is falsy; otherwise, it evaluates and returns y.

    x or y returns x if x is truthy; otherwise, it evaluates and returns y.

For instance:

# division is never evaluated, because the first argument is True
lazy_or = True or (1 / 0)  # True

# division is never evaluated, because the first argument is False
lazy_and = False and (1 / 0)  # False
'''
