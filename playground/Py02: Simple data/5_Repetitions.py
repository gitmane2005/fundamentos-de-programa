text = input()
reps = int(input())

if (reps>1):
    text_sum = text + "-"
    for i in range(reps-2):
        text_sum = text_sum + text + "-" 

    text_sum = text_sum + text

    print(text_sum)
else:
    print(text)
