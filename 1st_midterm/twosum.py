def numsum(arr, target):
    num_dict = {}

    for i, num1 in enumerate(arr):  # enumerate() returns both the index and the value
        num2 = target - num1

        if num2 in num_dict:
            return [num_dict[num2], i]
        num_dict[num1] = i

    return []

arr = [2, 7, 11, 15, 20, 4, 56, 80]
target = 100
print(numsum(arr, target))

