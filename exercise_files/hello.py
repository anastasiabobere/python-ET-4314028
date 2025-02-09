from decimal import Decimal, getcontext
getcontext().prec = 2  # Set precision to 6 decimal places
result = Decimal('1') / Decimal('7')
print(result)