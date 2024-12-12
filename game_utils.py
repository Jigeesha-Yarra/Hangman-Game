def handle_guess(game, guess):
    if guess in game["guessed_letters"]:
        print(f"You already guessed '{guess}'. Try another letter.")
    elif guess in game["word"]:
        print(f"Good job! '{guess}' is in the word.")
        game["guessed_letters"].append(guess)
        updated_state = list(game["cur_state"])
        for ind, letter in enumerate(game["word"]):
            if letter == guess:
                updated_state[ind] = guess
        game["cur_state"] = "".join(updated_state)
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        game["guessed_letters"].append(guess)
        game["remaining_attempts"] -= 1

def check_game_status(game):
    if "_" not in game["cur_state"]:
        return "win"
    elif game["remaining_attempts"] <= 0:
        return "lose"
    return "ongoing"


