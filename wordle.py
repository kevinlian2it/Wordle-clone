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
    i = 1
    while i<=6:
        guess = input(f"Guess {i}/6: ")
        if guess not in words:
            print("Enter a valid guess!")
            continue
        else:
            check_guess(word,guess)
            i+=1
        if guess == word:
            print("You guessed right!")
            return
    print("You failed, try again next time. The word was " + word + ".")
    return

def get_word(words):
    return random.choice(words)

def check_guess(word, guess):
    word_list = list(word)  # Convert word to a list to allow for mutable operations
    for i in range(len(guess)):
        if guess[i] == word_list[i]:
            print_green(guess[i])
            word_list[i] = None  # Mark this position as correctly guessed
        elif guess[i] in word_list:
            print_yellow(guess[i])
            word_list[word_list.index(guess[i])] = None  # Mark this letter as used
        else:
            print_gray(guess[i])
    print()  # Add a newline for better readability

if __name__ == '__main__':
    main()