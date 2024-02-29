from collections import Counter
from itertools import product
def undoom_dice(Die_A, Die_B):
    def sum_of_dice(die_1, die_2):
        return Counter(i + j for i, j in product(die_1, die_2))
    normal_sum_dist = sum_of_dice(Die_A, Die_B)
    def all_dice_comb():
      dice_list = []
      for x2 in range(2, 11):
        for x3 in range(x2, 11):
          for x4 in range(x3, 11):
            for x5 in range(x4, 11):
              for x6 in range(x5, 11):
                dice_list.append([1, x2, x3, x4, x5, x6])
      return dice_list
    def find_modified_dice():
        for die_1 in all_dice_comb():
            for die_2 in all_dice_comb():
                if (
                    sum_of_dice(die_1, die_2) == normal_sum_dist
                    and die_1 != Die_A
                    and die_2 != Die_A
                ):
                    return die_1, die_2
    modified_dice = find_modified_dice()
    return modified_dice
Die_A = [1, 2, 3, 4, 5, 6]
Die_B = Die_A.copy()
print(undoom_dice(Die_A, Die_B))
