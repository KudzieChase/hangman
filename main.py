# Write your code here
import random

words = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")
play = "play"
quit_game = "exit"


def prompt():
    mode = input('Type "play" to play the game, "exit" to quit: ')
    if mode == play:
        play_game()
    elif mode == quit_game:
        quit_game()
    else:
        prompt()


def play_game():
    computer = random.choice(words)
    hint = "{}".format("-" * len(computer))
    attempts = 8
    seen = set()

    while attempts != 0:
        print()
        print(hint)
        letter = input("Input a letter: ")

        if len(letter) == 1 and not letter.islower():
            print("It is not an ASCII lowercase letter")
            continue

        if len(letter) != 1:
            print("You should input a single letter")
            continue

        computer_set = set(computer)

        if letter in seen:
            print("You already typed this letter")
            continue
        else:
            seen.add(letter)

        if letter not in computer_set:
            print("No such letter in the word")
            attempts = attempts - 1
            continue

        hint = list(hint)
        for i in range(len(computer)):
            if hint[i] == letter:
                print("You already typed this letter")
                break
            elif computer[i] == letter:
                hint[i] = letter
            else:
                continue

        hint = "".join(hint)
        if hint == computer:
            print("You survived!")
            break
    else:
        print("You are hanged!")


def quit_game():
    exit()


if __name__ == '__main__':
    prompt()
