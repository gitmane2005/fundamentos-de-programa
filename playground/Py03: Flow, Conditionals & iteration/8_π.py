import math

result = 0
const = (2*math.sqrt(2))/9801

for k in range(50):
    dividendo = (math.factorial(4*k))*(1103+26390*k)
    divisor = (((math.factorial(k))**4)*(396**(4*k)))
    result = result + (dividendo/divisor)
print(round(1/(const*result),8))
