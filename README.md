# Hangman Game

This project is a simple command-line implementation of the classic Hangman game in Python. The game randomly selects a word from a predefined list, and the player must guess the word one letter at a time within a limited number of attempts.

## Features
- Randomly selects a word from a list.
- Displays the current state of the word, guessed letters, and remaining attempts.
- Validates user input to ensure it's a single alphabetical character.
- Provides feedback for correct and incorrect guesses.
- Ends the game with a win or loss message.

## Files
The project is divided into two Python files for better modularity:

1. **`game_utils.py`**
    - Contains utility functions to manage the game's logic and state.
      - `handle_guess`: Updates the game state based on the player's guess.
      - `check_game_status`: Checks if the game is won, lost, or ongoing.

2. **`hangman.py`**
    - The main file that runs the game loop and handles user interaction.
    - Imports functions from `game_utils.py` to manage the game's logic.


### Example Gameplay
```plaintext
Welcome to Hangman!

Current Word: _ _ _ _ _ _ _ _
Guessed Letters: 
Remaining Attempts: 6

Enter your guess (single letter): a
Good job! 'a' is in the word.

Current Word: _ a _ _ _ _ _ a
Guessed Letters: a
Remaining Attempts: 6
```

## Project Structure
```
HangmanGame/
├── game_utils.py   # Utility functions for game logic
├── hangman.py      # Main game script
└── README.md       # Project documentation
```

## Customization
- Add more words to the `words_list` in `hangman.py` to increase the variety of words.
- Adjust the number of `remaining_attempts` in `initialize_game` for easier or harder gameplay.

## Known Issues
- The game currently supports only single-word guesses. Multi-word phrases are not supported.

## License
This project is open-source and available under the MIT License.
