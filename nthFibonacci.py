def Fibonacci(nth):
    list = []
    for i in range(0, nth):
        if i != 0 and i != 1:
            i = list[(i-1)]+list[(i-2)]
        list.append(i)
    print(list[nth-1],(list))


Fibonacci(18)
