# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:45:31 2024

@author: Geoffrey Chemwa
"""

print("Welcome to my computer quiz!")       #This line prints a welcoming message to the user.

playing = input("Do you want to play? ")    #This line asks the user if they want to play the quiz and stores their response in the variable playing.

if playing.lower() != "yes":   #This condition checks if the user's input is not equal to "yes" (ignoring case differences by using .lower()). If the input is not "yes", the program ends using the quit() function.
    quit()

print("Okay! Let's play :)")    #The program confirms that the game is starting with a message and initializes a score variable to keep track of correct answers, starting at 0.
score = 0

answer = input("What does CPU stand for? ")         #The program asks the user what "CPU" stands for and checks if their answer (converted to lowercase) matches "central processing unit". If correct, it increments the score by 1; otherwise, it tells the user they are incorrect
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")       #The program asks questions about the meanings of "GPU", "RAM", and "PSU", and applies the same check as before, updating the score accordingly.
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")  #The program prints the number of questions the user got correct. The score is converted to a string using str() so it can be concatenated with the rest of the message.
print("You got " + str((score / 4) * 100) + "%.")       #The program calculates the user's percentage score by dividing their score by the total number of questions (4), multiplying by 100, and converting it to a string to print the final message.