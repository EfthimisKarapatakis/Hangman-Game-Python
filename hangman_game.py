from random import choice

def get_todays_word():
    words = [
        "apple", "avocado", "banana", "ball", "bean", "beet", "bell", "berry", "blue", 
        "book", "bottle", "bread", "broccoli", "butter", "cake", "carrot", "cat", 
        "cabbage", "cane", "celery", "charm", "cherry", "chili", "coconut", "coin", 
        "corn", "cucumber", "date", "dragon", "fig", "fish", "fork", "fruit", 
        "garlic", "gold", "goat", "grape", "grapefruit", "green", "hat", "house", 
        "ice", "jalapeno", "kiwi", "kale", "lamp", "lemon", "lettuce", "lime", 
        "melon", "mango", "moon", "mushroom", "nectarine", "note", "onion", 
        "orange", "peach", "pear", "pepper", "pineapple", "plum", "pomegranate", 
        "raspberry", "rain", "rocket", "rose", "shoe", "skate", "sky", "snow", 
        "star", "train", "tree", "truck", "turnip", "zucchini", "herb", "potato", 
        "pumpkin", "tomato", "apricot", "basil", "beetroot", "brussels", "cabbage", 
        "cantaloupe", "chili", "chives", "coriander", "dill", "endive", "fennel", 
        "fig", "jalapeno", "leek", "lime", "mango", "marjoram", "mint", "okra", 
        "oregano", "parsley", "rosemary", "sage", "sorrel", "tarragon", "thyme", 
        "turnip", "wasabi", "zucchini"
    ]

    todays_word = choice(words)  # Choose a random word
    letters = set(todays_word)   # Use a set to track remaining letters
    #print(todays_word)
    return todays_word, letters

def initialize_game(todays_word):
    spaces = ["_" for _ in todays_word]  # Initialize spaces with underscores
    print(*spaces, sep = " ")
    wrong_letters = set()                # Use a set for wrong letters
    tries = 0
    return spaces, wrong_letters, tries

def handle_user_guess(todays_word, letters, spaces, wrong_letters, tries):
    print("\n\nYou have 9 wrong guesses!")
    while True:
        if tries <= 9:
            guess = input("\nGuess a letter: ").strip().lower()

            if guess.isalpha() and len(guess) == 1:
                if guess in letters:
                    print(f"\nThe letter '{guess}' is in the word!")
                    for index, letter in enumerate(todays_word):
                        if letter == guess:
                            spaces[index] = guess
                    letters.remove(guess)  # Remove guessed letter from the set

                    if "_" not in spaces:
                        print(f"You win!! The word was '{todays_word}'")
                        print(f"With {tries} tries!")
                        break
                else:
                    print(f"\nThe letter '{guess}' is not in the word!")
                    wrong_letters.add(guess)
                    print("Wrong letters:", ", ".join(wrong_letters))
                    tries += 1

                print("Current word:", " ".join(spaces))
                print("Attempts:", tries)
            else:
                print("Invalid input. Please enter a single letter.")
        else:
            print("You have run out of guesses")
            print(f"The word was '{todays_word}'")
            break


def main():
    todays_word, letters = get_todays_word()
    spaces, wrong_letters, tries = initialize_game(todays_word)
    handle_user_guess(todays_word, letters, spaces, wrong_letters, tries)
    a = input("")

if __name__ == "__main__":
    main()
