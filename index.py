import random


print("\n*******Guess the secret word!*******")

secretWords = [
    "floor",
    "light",
    "manga",
    "comic",
    "train",
    "phone",
    "steal",
    "pizza",
    "movie",
    "gumbo",
    "apple",
    "spies",
    "grand",
    "dress",
    "character",
    "pie",
    "base",
    "car",
    "panda",
    "pillow",
    "bike",
    "japan",
    "whopper",
    "cannon",
    "tire",
    "china",
    "view" "laptop",
    "crow",
    "hit",
    "soccer",
    "president",
    "autograph",
]

answer = random.choice(secretWords)
gotCorrectWord = False
lives = 9
hearts = "\u2764"
questionMarks = []

for char in answer:
    questionMarks.append("?")


def guessedLetter(Userletter):
    for x in answer:
        if x == Userletter:
            answerIndex = answer.index(x)
            questionMarks[answerIndex] = Userletter
            print(questionMarks)
            print("\nYou found one! Do it again!")
            break


while lives != 0:
    if gotCorrectWord == True:
        break

    print(questionMarks)
    print("\n" + hearts * lives)
    userGuess = input("Type a letter or the whole word\n")

    if userGuess == answer:
        print("Correct! " + "The word is " + answer)
        break

    elif userGuess in answer:
        guessedLetter(userGuess)
        if "".join(questionMarks) == answer:
            print("Correct! " + "The word is " + answer)
            gotCorrectWord = True

    else:
        print("\nWrong answer! Life lost.")
        lives -= 1
        if lives == 0:
            print("Game Over!" + "The word was " + answer)
