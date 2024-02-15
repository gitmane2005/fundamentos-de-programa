import math
num_a = float(input())
num_b = float(input())
num_c = float(input())

result_plus = round((-num_b + math.sqrt(num_b**2 - 4*num_a*num_c))/ (num_a * 2),2)
result_minus = round((-num_b - math.sqrt(num_b**2 - 4*num_a*num_c))/ (num_a * 2),2)

print(f"The solutions are {result_plus} and {result_minus}")