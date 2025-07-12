prime = [2, 3, 5, 7, 11, 13, 17, 19]

k = 20
number = 1   

for i in prime:
    power = 1
    highest_power = power
    while (i ** power) <= k:
        highest_power = i ** power
        power += 1
    number *= highest_power

print(number)