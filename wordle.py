from colorama import Back
import random
def print_green(letter):
    print(Back.GREEN + f" {letter} " + Back.RESET, end='')
def print_yellow(letter):
    print(Back.LIGHTYELLOW_EX + f" {letter} " + Back.RESET, end='')
def print_gray(letter):
    print(Back.WHITE + f" {letter} " + Back.RESET, end='')

def main():
    print("Take a guess!")
    with open("wordle.txt", 'r') as file:
        words = file.readlines()
        # Remove newline characters and any potential whitespace around the words
        words = [word.strip() for word in words]
    word = get_word(words)
    for i in range(6):
        guess = input()
        if guess not in words:
            print("Enter a valid guess!")
            i-=1
        else:
            print("Guess " + str(i+1) + "/6: " + guess)
            check_guess(word,guess)
        if guess == word:
            print("You guessed right!\n")
            exit()
    print("You failed, try again next time.")

def get_word(words):
    return random.choice(words)

def check_guess(word, guess):
    for i in range(5):
        if guess[i] in word:
            if guess[i] == word[i]:
                print_green(guess[i])
            else:
                print_yellow(guess[i])
        else:
            print_gray(guess[i])
    return 0

if __name__ == '__main__':
    main()