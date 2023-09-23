print("This is a quiz about computers!\n")

playing = input("Do you want to play the game? (Please answer YES OR NO)\n")

if playing.upper() != "YES":
    quit()

print("Okay! Let's start right away!\n")

answer = input("What does CPU stand for? ")
if answer == "central processing unit".lower():
    print("Correct Answer!")
else:
    print("Sorry! That's the Wrong Answer:(")