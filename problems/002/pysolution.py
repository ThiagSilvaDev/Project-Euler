k = 4000000
current_term = 1
previous_term = 1
sum_fibo = 0

even_term = current_term + previous_term

while current_term <= k:
    sum_fibo += even_term

    current_term = previous_term + even_term
    previous_term = even_term + current_term

    even_term = current_term + previous_term

print(sum_fibo)