from random import choice


def display_hangman(incorrect_guess):
    hangman_stages = [
        """
        --------
        |      |
        |
        |
        |
        |
        -----
        """,
        """
        --------
        |      |
        |      O
        |
        |
        |
        -----
        """,
        """
        --------
        |      |
        |      O
        |      |
        |
        |
        -----
        """,
        """
        --------
        |      |
        |      O
        |     /|
        |
        |
        -----
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |
        |
        -----
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     /
        |
        -----
        """,
        """
        --------
        |      |
        |      O
        |     /|\\
        |     / \\
        |
        -----
        """,
    ]
    print(hangman_stages[incorrect_guess])


def check_the_letter(letter, word):
    indexs = []
    if letter in word:
        indexs = [index for index, word in enumerate(word) if word == letter]
    return indexs


def replace_letter(index_to_replace, letter_to_replace, blank_word):
    tmp_lst = list(blank_word)
    for index in index_to_replace:
        tmp_lst[index] = letter_to_replace
    blank_word = "".join(tmp_lst)
    return blank_word


def word_lst():
    fruits = [
        "Apple",
        "Banana",
        "Grape",
        "Mango",
        "Orange",
        "Pineapple",
        "Cherry",
        "Lemon",
        "Kiwi",
    ]
    country = ["India", "China", "America", "Australia", "Russia", "Canada", "Italy"]
    word = choice(fruits + country)
    if word in fruits:
        return "Hint: The word is fruit name", word.lower()
    else:
        return "Hint: The word is country name", word.lower()


def hangman_game():
    hint, word = word_lst()
    blank_word = "_" * len(word)
    incorrect_guesses = 0
    print(hint)
    for i in range(0, 7):
        if blank_word == word:
            print("You have guessed the Word :", blank_word)
            break
        print("Guess the word :", blank_word)
        letter = input("Enter your guess : ")
        indexs = check_the_letter(letter, word)
        if len(indexs) == 0:
            incorrect_guesses = i
            display_hangman(incorrect_guesses)
        else:
            blank_word = replace_letter(indexs, letter, blank_word)
    else:
        print("You have not Guessed word!")


if __name__ == "__main__":
    hangman_game()
