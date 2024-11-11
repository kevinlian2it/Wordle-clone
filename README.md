# Wordle

Wordle Rules: 

Objective: The player's goal is to guess a secret word which is five letters long.

Number of Attempts: The player has six attempts to guess the word correctly.

Guess Rules:

Each guess must be a valid five-letter word. Invalid guesses (words not in the game's dictionary or words of incorrect length) are not accepted and do not count as an attempt.
After each guess, feedback is provided for each letter in the guessed word, indicating how close the guess is to the secret word.

Feedback Mechanism:

- Correct Position: If a letter in the guess is in the correct position, it is highlighted (e.g., with a green background). Wrong Position but Correct Letter: If a letter is in the word but in the wrong position, it is highlighted differently (e.g., with a yellow background).
- Incorrect Letter: If a letter is not in the word at all, it is marked differently (e.g., with a gray background or simply not highlighted).
- Winning Condition: The player wins if they guess the word correctly within six attempts.

Losing Condition: The player loses if they fail to guess the word correctly after six attempts.

Dictionary: The game uses a specific dictionary of valid words. Both the secret word and the player's guesses must be from this dictionary.

Input: The player inputs their guess through a simple text interface (using input()), and the game provides feedback through text output (using print()), potentially utilizing color coding via the colorama package for visual feedback.

Replayability: Each game session randomly selects a new secret word from the dictionary, offering a fresh challenge each time.

