
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