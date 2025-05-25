def factorial_dp(n):
    
    arr = [1] * (n + 1)

    for i in range(2, n + 1):
        arr[i] = arr[i - 1] * i
        
    return arr[n]    

number = int(input("Input the number"))
result = factorial_dp(number)
print(f"{number}! = {result}")
    
