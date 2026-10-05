secret = 13

print("\nWelcome to the Number Guessing Game!\nIn this game, the computer will choose a number between 1 and 50 and you have to guess it.\nGood Luck!\n\n")

num_guesses = 5
i = 5
state = False

while num_guesses > 0 and not state:
    guess = int(input("Enter your guess:"))

    if guess == secret:
        print(f"\n🎉Congratulations! You guessed the secret number correctly in {num_guesses} guesses left!🎉")
        state = True
    else:
        num_guesses -= 1

    difference = abs(secret - guess)

    if difference <= 15:
        print("🔥 Hot!!")
    elif difference <= 20:
        print("🌡️ Warm!")
    elif difference <= 35:
        print("🥶 Cold.")
    else:
        print("🧊 ICE COLD!!!")

    if num_guesses > 0:
        lives = ""

        for i in range(num_guesses):
            lives += "❤️ "

        print(f"Remaining lives : {lives}")

if not state:
    print(f"You lost!!\nYour number of attempts : {num_guesses}\nThe secret number was : {secret}")