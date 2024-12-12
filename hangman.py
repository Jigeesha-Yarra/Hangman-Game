import random
from game_utils import handle_guess, check_game_status

words_list = ["python","java","developer","programmer","hangman","javascript"]

def play_hangman(words_list):
    word = random.choice(words_list)
    game = {
        "word": word,
        "guessed_letters": [],
        "remaining_attempts": 6,
        "cur_state": "_"*len(word)
    }

    print("Welcome to Hangman!")

    while True:
        print("\nCurrect Word: ", " ".join(game["cur_state"]))
        print("\nGuessed Letters: ", " ".join(game["guessed_letters"]))
        print("\nRemaining Letters: ", (game["remaining_attempts"]))

        guess = input("Enter your guess (single letter): ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabet.")
            continue

        handle_guess(game,guess)
        status = check_game_status(game)

        if status == "win":
            print(f"Congratulations! You guessed the word: {game['word']}")
            break
        elif status == "lose":
            print(f"Game Over! The word was: {game['word']}")
            break 
    
if __name__ == "__main__":
    play_hangman(words_list)

