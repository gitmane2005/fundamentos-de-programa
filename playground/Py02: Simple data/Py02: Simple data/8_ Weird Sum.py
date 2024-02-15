num1 = int(input())
num2 = int(input())

sum = num1 + num2
remainder = sum % 2

result = sum*(2-remainder) + num1*num2*(remainder)


print(result)