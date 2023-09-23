question_answer_dict = {
    "What does CPU stand for? " : "central processing unit", "What does GUI stand for? ": "graphical user interface",
    "Who is the co-founder of Microsoft Corporation?" : "bill gates",
    "Which programming language is often used for web development and is known for its client-side scripting capabilities?" : "javascript",
    "What does HTML stand for in the context of web development?" : "hypertext transfer market language",
    " Which computer operating system is developed by Apple Inc.?" : "ios",
    "What does URL stand for in the context of web addresses?" : "universal resource locator"
    
    }

counter = 0

print("This is a quiz about computers!\n")

playing = input("Do you want to play the game? (Please answer YES OR NO)\n")

if playing.upper() != "YES":
    quit()

print("Okay! Let's start right away!\n")

for question, answer in question_answer_dict.items():
    print(question)
    
    guess = input().lower()
    
    if guess == answer:
        print("Correct Answer!\n")
        counter += 1
    else:
        print("Wrong Answer:(\n")
        
print(f"\nYour Score is: {counter} / {len(question_answer_dict)}\n\nThank you for playing my quiz game:)")
