def calc_prob(die_a, die_b):
    prob = {}
    for face_a in die_a:
        for face_b in die_b:
            total = face_a + face_b
            prob[total] = prob.get(total, 0) + 1
    total_combinations = len(die_a) * len(die_b)
    for key in prob:
        prob[key] /= total_combinations
    return prob
def spots(die_a, die_b):
    new_die_a = [min(4, x) for x in die_a]  
    total_combinations = len(die_a) * len(die_b)
    current_prob = calc_prob(die_a, die_b)
    target_prob = calc_prob(new_die_a, die_b)   
    for key in current_prob:
        target_count = int(round(current_prob[key] * total_combinations))
        current_count = int(round(target_prob.get(key, 0) * total_combinations))
        diff = target_count - current_count
        if diff > 0:
            for i in range(1, 7):
                if diff == 0:
                    break
                if i not in die_b:
                    die_b.append(i)
                    diff -= 1
        elif diff < 0:
            for i in range(1, 7):
                if diff == 0:
                    break
                if i in die_b and i != 6:
                    die_b.remove(i)
                    diff += 1
    return new_die_a, die_b
def undoom_dice(die_a, die_b):
    new_die_a, new_die_b = spots(die_a, die_b)
    return new_die_a, new_die_b
initial_die_a = [1, 2, 3, 4, 5, 6]
initial_die_b = [1, 2, 3, 4, 5, 6]
new_die_a, new_die_b = undoom_dice(initial_die_a,initial_die_b)
print("New Die A:", new_die_a)
print("New Die B:", new_die_b)
