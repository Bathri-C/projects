'''FIRST METHOD '''
import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}

dice = []
total = 0
num_of_dice = int(input("How many dice?: "))

for die in range(num_of_dice):
    dice.append(random.randint(1, 6))

# PRINT VERTICALLY
# for die in range(num_of_dice):
#    for line in dice_art.get(dice[die]):
#        print(line)

# PRINT HORIZONTALLY
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for die in dice:
    total += die
print(f"total: {total}")

'''SECOND METHOD (simple approach)'''

x = 'yes'
while x == "yes":

    no = random.randint(1, 6)

    if no == 1:
        print("┌─────────┐",
              "\n│         │",
              "\n│    ●    │",
              "\n│         │",
              "\n└─────────┘")
    if no == 2:
        print("┌─────────┐",
              "\n│ ●       │",
              "\n│         │",
              "\n│       ● │",
              "\n└─────────┘")

    if no == 3:
        print("┌─────────┐",
              "\n│ ●       │",
              "\n│    ●    │",
              "\n│       ● │",
              "\n└─────────┘")

    if no == 4:
        print("┌─────────┐",
              "\n│ ●     ● │",
              "\n│         │",
              "\n│ ●     ● │",
              "\n└─────────┘")

    if no == 5:
        print("┌─────────┐",
              "\n│ ●     ● │",
              "\n│    ●    │",
              "\n│ ●     ● │",
              "\n└─────────┘")

    if no == 6:
        print("┌─────────┐",
              "\n│ ●     ● │",
              "\n│ ●     ● │",
              "\n│ ●     ● │",
              "\n└─────────┘")

    x = input("press 'yes' to roll again and 'no' to exit:")
    print("\n")
