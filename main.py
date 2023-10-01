import re
import random

words = ["hello", "work", "bike", "python"]
selection_word = random.choice(words)
attempts = int(input("Enter numbers of try:\n"))
part_pattern = ""
count = 0

while True:

    if count == attempts:
        print("You lose")
        exit()

    elem = input("Enter letter or word: ")

    if len(elem) == 1:

        if elem in selection_word:

            part_pattern += elem

            pattern = f"[^{part_pattern}]"

            print(re.sub(pattern, "*", selection_word))
            if re.sub(pattern, "*", selection_word) == selection_word:
                print('You won!')
                exit()
            continue

        else:

            print("Invalid letter")

            count += 1

            continue



    else:

        if elem == selection_word:

            print("You won")

            exit()

        else:

            print("Invalid word")

            count += 1

