print("Welcome to My Quiz Game!")

playing = input("Do you want to play?\n")

if playing.lower() != "yes":
    quit()

print("okay! Let's play :)")
score = 0

ans = input("What does RAM means on your computer?\n")
if ans.lower() == "random access memory":
    print("Yes you are Correct!")
    score += 1
else:
    print("Your answer is Incorrect! Try again later")

ans = input("What is the other name used for computer programs and information?\n")
if ans.lower() == "software":
    print("Yes you are Correct!")
    score += 1
else:
    print("Your answer is Incorrect! Try again later")

ans = input("The part of a computer that allows the user to view information on a screen is called:\n")
if ans.lower() == "monitor":
    print("Yes you are Correct!")
    score += 1
else:
    print("Your answer is Incorrect! Try again later")

ans = input("Name the part that sends signals to other parts of the computer and tells them what to do.\n")
if ans.lower() == "motherboard":
    print("Yes you are Correct!")
    score += 1
else:
    print("Your answer is Incorrect! Try again later")

ans = input("This is a flat input device that usually sits in front of the monitor.\n")
if ans.lower() == "keyboard":
    print("Yes you are Correct!")
    score += 1
else:
    print("Your answer is Incorrect! Try again later")

ans = input("This memory is for short-term storage and is lost when the computer is turned off.\n")
if ans.lower() == "ram":
    print("Yes you are Correct!")
    score += 1
else:
    print("Your answer is Incorrect! Try again later.")

print(f"You got {score} questions correct!!") 
print(f"You got {(score/6)*100}%.") 