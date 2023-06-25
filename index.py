import random


print("Guess the secret word!")

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
]

questionMarks = list("?????")
answer = random.choice(secretWords)

gotCorrectWord = False
lives = 9


def guessedLetter(Userletter):
    for x in answer:
        if x == Userletter:
            answerIndex = answer.index(x)
            questionMarks[answerIndex] = Userletter
            print(questionMarks)
            print("You found one! Do it again!")
            break


while lives != 0:
    if gotCorrectWord == True:
        break

    print(questionMarks)
    userGuess = input("Type a letter or the whole word")

    if userGuess == answer:
        print("Correct! " + "The word is " + answer)
        break

    elif userGuess in answer:
        guessedLetter(userGuess)
        if "".join(questionMarks) == answer:
            print("Correct! " + "The word is " + answer)
            gotCorrectWord = True

    else:
        print("Wrong answer! Life lost.")
        lives -= 1
        if lives == 0:
            print("Game Over")
