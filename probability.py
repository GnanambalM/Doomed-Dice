sum_counts = {sum_value: 0 for sum_value in range(2, 13)}
for roll_a in range(1, 7):
    for roll_b in range(1, 7):
        total = roll_a + roll_b
        sum_counts[total] += 1
print("Probability of each possible sum occurring:")
for sum_value, count in sum_counts.items():
    probability = count / 36
    print(f"P(Sum = {sum_value}) = {probability:.2f}. There are {count} combinations")