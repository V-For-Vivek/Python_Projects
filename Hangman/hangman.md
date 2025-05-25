# How is Hangman Game Played?

The hangman game is a multiplayer game. In this game, one player selects a word. Other players have a certain number of guesses to guess the characters in the word. If the players are able to guess the characters in the entire word within certain attempts, they win. Otherwise, they lose

## How to Create Hangman Game in Python?

Here are the steps to create a Hangman game in Python:

1] Choose a word list: Create a list of words that the computer can randomly select from.

2] Select a random word: Use the random module to choose a word from the list.

3] Create the game board: Display the word as a series of underscores, one for each letter.

4] Get player input: Ask the player to guess a letter.

5] Check the guess:
If the letter is in the word, reveal its position(s) on the game board.
If the letter is not in the word, increment the number of incorrect guesses.

6] Update the game state:
If the player has guessed all the letters, they win.
If the player has made too many incorrect guesses (e.g., 6 for head, body, 2 arms, 2 legs), they lose.

7] Display the result: Show the player whether they won or lost, and reveal the correct word if they lost.

8] Ask to play again: Allow the player to start a new game if they wish.
