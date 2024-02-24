print("Welcome to my quiz!")

#asking whether the user wants to play or not
playing = input("Do you want to play? ")  #input('prompt')
if playing != "Yes":
    quit()      #'quit()' function immediately terminates (turns off) the programme
else:
    print("Okay! Put your seat belt on :) ")

score = 0   #initializing the score of the user

#asking more questions and taking answers
answer = input("What does CPU stands for? ")
if answer == "Central Processing Unit":
    print("Bang! You are awesome!")
    score += 1   #score = score+1   #adding up the user's score
else:
    print("Uh oh! Hard luck, buddy :( ")

answer = input("What does RAM stands for? ")
if answer == "Random Access Memory":
    print("Good job, dude! ")
    score += 1
else:
    print("Uh oh! Hard luck, buddy :( ")

answer = input("What does SSD stands for? ")
if answer == "Solid State Drive":
    print("You are being unstoppable! ")
    score += 1
else:
    print("Uh oh! Hard luck, buddy :( ")

answer = input("What does GPU stands for? ")
if answer == "Graphics Processing Unit":
    print("You are the GOAT! ")
    score += 1
else:
    print("Uh oh! Hard luck, buddy :( ")

print("Your total score is: ", score)
#could have used percentage as score as well [(score/questions) * 100]
print("You got " + str((score/4)*100) + "%")

if score == 0:
    print("Study! ")
elif 1 <= score <= 3:
    print("You are almost there! ")
else:
    print("You are invincible! ")

