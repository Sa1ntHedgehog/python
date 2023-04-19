import random

NUM_DIGITS = 3
NUM_GUESSES = 100
SYMBOLS = [
    "",
    "~",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    "(",
    ")",
    "_",
    "-",
    "+",
    "=",
    "<",
    ">",
    "?",
    ":",
    '"',
    "'",
    "\\",
    "/",
    "|",
]


def getSecret():
    alphabets = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = list("0123456789")
    random.shuffle(digits)
    random.shuffle(alphabets)
    secret = ""
    secret_counter = 0
    while secret_counter < NUM_DIGITS:
        if secret_counter < NUM_DIGITS:
            secret += str(digits[secret_counter])
            secret_counter += 1
        if secret_counter < NUM_DIGITS:
            secret += str(alphabets[secret_counter])
            secret_counter += 1
    random.shuffle(list(secret))
    return secret


def getClues(guess, secret):
    if guess == secret:
        return "You got it"
    clues = []
    for i in range(len(guess)):
        if guess[i] == secret[i]:
            clues.append("Fermi")
        elif guess[i] in secret:
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagels"
    else:
        clues.sort()
        return " ".join(clues)


def inputGuess(countGuessess):
    print("Guess #{}: ".format(countGuessess))
    guess = ""
    guess = input("> ")
    flag = False
    for element in guess:
        if element in SYMBOLS:
            flag = True
            break
    if flag == True:
        return inputGuess(countGuessess)
    else:
        return guess

def main():
    print(
        """=============================
Bagels, a deductive logic game.
I am thinking of a {}-digit number with no repeated digits and alphbet symbols.
Try to guess what it is. Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.

For example, if the secret number was 2W8 and your guess was 8W3, the
clues would be Fermi Pico.
=============================""".format(
            NUM_DIGITS
        )
    )

    while True:
        secret = getSecret()
        print("I have thought secret number from {} symbols".format(NUM_DIGITS))
        print("You have {} guessess to get it.".format(NUM_GUESSES))

        countGuessess = 1
        while countGuessess <= NUM_GUESSES:
            guess = ""
            while len(guess) != NUM_DIGITS:
                guess = inputGuess(countGuessess)
            clues = getClues(guess, secret)
            print(clues)
            countGuessess += 1

            if guess == secret:
                break
            if countGuessess > NUM_GUESSES:
                print("You ran out of guessess")
                print("The answer was {}.".format(secret))

        print("Do you want to play again y/n?")
        if not input("> ").lower().startswith("y"):
            break
    print("Thank you for playing!")


if __name__ == "__main__":
    main()
