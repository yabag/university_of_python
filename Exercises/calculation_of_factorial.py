
def calculation_of_factorial(n):
    return calculation_of_factorial(n-1)*n if n > 1 else 1

n = int(input())
print(calculation_of_factorial(n))

