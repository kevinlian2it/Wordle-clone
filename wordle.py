from colorama import Back
def print_green(letter):
    print(Back.GREEN + f" {letter} " + Back.RESET, end='')
def print_yellow(letter):
    print(Back.LIGHTYELLOW_EX + f" {letter} " + Back.RESET, end='')
def print_gray(letter):
    print(Back.WHITE + f" {letter} " + Back.RESET, end='')

def main():
    word = get_word()
    print("Take a guess!\n")
    for i in range(5):
        guess = input()
        check_guess()
        if guess == word:
            print("You guessed right!\n")
            exit()
    print("You failed, try again next time.")