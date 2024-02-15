def test_looping(input):
    i = 10
    while input != 0:
        result1 = int(input % i)
        input = int(input / 10)
        result2 = int(input % i)
        
        if abs(result1 - result2) == 1 or abs(result1 - result2) == 9:
            continue
        else:
            print("Not a looping number")
            return
    print("Looping number")
    

n = int(input())
test_looping(n)