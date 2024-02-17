dist = [[0]*6 for i in range(6)]
for roll_a in range(1, 7):
    for roll_b in range(1, 7):
        total = roll_a + roll_b
        dist[roll_a - 1][roll_b - 1] = total
print("Distribution of all possible combinations:")
for j in dist:
    print(j)