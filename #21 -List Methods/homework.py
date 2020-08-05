numbers = [3, 5, 6, 9, 8, 2, 2]
uniques = []

for number in numbers:
    if number not in uniques:
        uniques.append(number)

print(uniques)