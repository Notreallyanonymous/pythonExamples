def getGuess():
    guess = int(input("Enter a guess: ")); 
    return guess


def main():
    guess = getGuess()
    if guess == 50:
        print("You are correct")
    else: 
        print("You are incorrect")


main()