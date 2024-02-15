def valid(octal_str):
    for i in range(len(octal_str)):
        if int(octal_str[i])>=0 and int(octal_str[i])<=7:
            continue
        else:
            print("Not a valid number.")
            return False
    return True

def octal_to_decimal(octal_number):
    t = 0
    result = 0
    while octal_number != 0:
        bite = octal_number % 10
        result =result +bite*(8**t)
        octal_number = int(octal_number//10)
        t = t + 1
    return result

    

octal = int(input())
if valid(str(octal)):
    print(octal_to_decimal(octal))