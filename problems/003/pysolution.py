k = 600851475143
factor = 2
greatest_factor = 0

while factor * factor <= k:
    if k % factor == 0:
        greatest_factor = factor
        k //= factor
    else:
        factor += 1

if k > 1:
    greatest_factor = k

print(greatest_factor)