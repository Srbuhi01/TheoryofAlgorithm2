def magic_cows(initial, L, D):  
    memo = {}

    def count(cows, day):
        key = (cows, day)
        if key in memo:
            return memo[key]
        
        if day == D:
            return 1
        
        new_cows = cows * 2
        if new_cows > L:
            result = count(new_cows // 2, day + 1) * 2
        else:
            result = count(new_cows, day + 1)

        memo[key] = result 
        return result

    total = 0

    #main loop
    for c in initial:
        total += count(c, 0)
    return total

initial = [3, 2]  #count of cows in each ferm, 1st ferm - 3cow, 2nd ferm - 2 cow
L = 5             # L = max cows count
D = 3             # D = count of days

print(magic_cows(initial, L, D))
