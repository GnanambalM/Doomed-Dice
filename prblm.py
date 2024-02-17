import random
class Dice:
    def __init__(self):
        self.faces = [1, 2, 3, 4, 5, 6]
    def roll(self):
        return random.choice(self.faces)
def play():
    die_a = Dice()
    die_b = Dice()
    while True:
        user = input("Press Enter to roll the dice (or any input to exit): ")
        if user:
            print("Exiting the game...")
            break
        roll_a = die_a.roll()
        roll_b = die_b.roll()
        total = roll_a + roll_b
        print(f"Die A = {roll_a}, Die B = {roll_b}, Total = {total}")
if __name__ == "__main__":
    play()
