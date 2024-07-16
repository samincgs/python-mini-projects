print("Welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()

if playing != "yes":
    quit()
    
print("Sounds good! Let's start the game :) \n")

answer = input("What does CPU stand for? ").lower()

if answer == "central processing unit":
    print("Correct!")
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ").lower()

if answer == "graphics processing unit":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
else:
    print("Incorrect!")
    
answer = input("What does PSU stand for? ").lower()

if answer == "power supply unit":
    print("Correct!")
else:
    print("Incorrect!")