print("welcome to computer quiz!")
playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()
else:
    print("Okay! Let's play :)")
score = 0    

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Thats correct!')
    score += 1
else:
    print('Oops! Thats incorrect!')


answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print('Thats correct!')
    score += 1
else:
    print('Oops! Thats incorrect!')


answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Thats correct!')
    score += 1
else:
    print('Oops! Thats incorrect!')


answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Thats correct!')
    score += 1

else:
    print('Oops! Thats incorrect!')
print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%.")

