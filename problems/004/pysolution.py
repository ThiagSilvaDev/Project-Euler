max_palindrome = 0

for a in range(999, 99, -1):
    if a % 11 == 0:
        b_start = 999
        b_step = 1
    else:
        b_start = 990 
        b_step = 11

    for b in range(b_start, a - 1, -b_step):
        product = a * b
        if product <= max_palindrome:
            break
        if str(product) == str(product)[::-1]:
            max_palindrome = product

print(max_palindrome)
