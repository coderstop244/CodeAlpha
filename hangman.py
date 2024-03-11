import random
import string

# Define words list
words = ["python", "programming", "computer", "hangman", "game", "challenge", "mystery", "adventure"]

# Define hangman stages (visual representation)
HANGMAN_PICS = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
      |   |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """
]

def get_word():
  """Chooses a random word from the list."""
  return random.choice(words).lower()

def display_board(wrong_guesses, display_word):
  """Prints the game board including the hangman stages, wrong guesses, and hidden word."""
  print(HANGMAN_PICS[len(wrong_guesses)])
  print(" ".join(display_word))
  print(f"Wrong guesses: {', '.join(wrong_guesses)}")

def handle_guess(guess, secret_word, display_word):
  """Checks if the guess is in the word and updates the display word."""
  if guess in secret_word:
    for i, letter in enumerate(secret_word):
      if letter == guess:
        display_word[i] = guess
  return guess in secret_word

def play():
  """Main game loop that handles turns, win/lose conditions, and user interaction."""
  secret_word = get_word()
  display_word = ["_" for _ in secret_word]
  wrong_guesses = []
  wrong_guesses_allowed = len(HANGMAN_PICS) - 1

  while wrong_guesses_allowed > 0 and "_" in display_word:
    display_board(wrong_guesses, display_word)
    guess = input("Guess a letter: ").lower()

    # Validate guess input (single letter, not guessed yet, alphabetical)
    if len(guess) != 1 or guess not in string.ascii_lowercase or guess in wrong_guesses:
      print("Invalid input. Please enter a single letter you haven't guessed yet.")
      continue

    if handle_guess(guess, secret_word, display_word):
      # Correct guess
      continue
    else:
      # Wrong guess
      wrong_guesses.append(guess)
      wrong_guesses_allowed -= 1

  # Game over message
  display_board(wrong_guesses, display_word)
  if "_" not in display_word:
    print(f"You won! The word was: {secret_word}")
  else:
    print(f"You lost! The word was: {secret_word}")

if __name__ == "__main__":
  play()