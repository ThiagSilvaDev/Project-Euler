a = 3
b = 5
k = 999

def sum_of_multiples(num):
    num_multiples = k // num

    return num * (num_multiples * (num_multiples + 1)) // 2

result = sum_of_multiples(a) + sum_of_multiples(b) - sum_of_multiples(a * b)

print(result)