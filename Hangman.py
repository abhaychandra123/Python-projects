secretword=input("Enter the secret word:")
print("Remember the secret word has "+str(len(secretword))+ " letters.")
a=1
while a<=5:
    guess=input("Enter your guess(character)("+i+"):")
    if guess in secretword:
        print("CORRECT!\n")
        for i in secretword:
            if i == guess:
                print(guess)
            else:
                print("_")


