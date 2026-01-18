import random

# Load words from file
def load_words(filename):
    with open(konnyebbek.csv, "r") as forrasfajl:
        return [li+ne.strip().lower() for line in file if line.strip()]

# Hangman drawings
stages = [
    """
     ------
     |    |
          |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
          |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
     |    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|    |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
          |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    /     |
          |
    --------
    """,
    """
     ------
     |    |
     O    |
    /|\\   |
    / \\   |
          |
    --------
    """
]

# Game setup
words = load_words("words.txt")
word = random.choice(words)
guessed_letters = set()
wrong_guesses = 0
max_wrong = len(stages) - 1

print("🎯 Welcome to Hangman!")

# Game loop
while wrong_guesses < max_wrong:
    print(stages[wrong_guesses])

    # Display word
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    print("Word:", display.strip())

    # Check win
    if all(letter in guessed_letters for letter in word):
        print("\n🎉 You won! The word was:", word)
        break

    guess = input("Guess a letter: ").lower()

    # Validation
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Enter one letter only.")
        continue

    if guess in guessed_letters:
        print("⚠️ Letter already guessed.")
        continue

    guessed_letters.add(guess)

    if guess not in word:
        wrong_guesses += 1
        print("❌ Wrong guess!")

else:
    print(stages[wrong_guesses])
    print("\n💀 Game over! The word was:", word)
