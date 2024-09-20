# Blackjack Game

A simple Python-based implementation of a **Blackjack game** where the user plays against the computer. This game allows the user to hit or stand while trying to get as close to a total score of 21 without going over.

## Features

- Each player (user and computer) gets two random cards to start with.
- Face cards (10, 11, 12, 13) are all counted as 10 points.
- Ace cards (1) can be treated as either 1 or 11, depending on the player's score.
- The player can choose to hit (draw another card) or stand (end their turn).
- The computer automatically draws cards but only reveals one at the beginning.
- The game ends when either player busts (goes over 21) or if the player stands and scores are compared.
- The player is given the option to restart the game at the end.

## Rules

1. The game starts with two random cards drawn for both the user and the computer.
2. The user can choose to either:
   - **Hit**: Draw another card.
   - **Stand**: End their turn and compare scores with the computer.
3. The value of the cards:
   - Cards 10, 11, 12, 13 all count as 10.
   - Ace (1) can count as 1 or 11.
4. The goal is to have a score as close to 21 as possible without exceeding it.
5. If both players' scores exceed 21, it's a tie.
6. The game allows the player to restart after each round.

## How to Play

- The game will display your initial cards and the computer's first card.
- You can choose to **"hit"** (draw another card) or **"stand"** (end your turn).
- The game will continue until either you or the computer bust (go over 21) or both players choose to stand.
- At the end of each round, the winner is declared, and you can choose whether to play again.

## Code Explanation

- **`calculate_user_score()` / `calculate_computer_score()`**:  
  These functions calculate the score for the user and computer. They handle converting face cards (10, 11, 12, 13) to a score of 10 and treat the Ace (1) as either 1 or 11 depending on the total score.

- **`hit_or_stand()`**:  
  Handles the user's decision to either draw another card or end their turn. It also updates the computer's cards and score.

- **`compare_scores()`**:  
  Compares the scores of both the user and computer, determining the winner, and checks if either player has busted.

- **`restart_game()`**:  
  Allows the player to restart the game once a round ends.

- **`play_game()`**:  
  Main function that runs the game. It initializes the game, handles the player's actions, and calculates the scores.
