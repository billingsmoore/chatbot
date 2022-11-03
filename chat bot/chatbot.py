from chatfunctions import *
from getfunctions import *

conversing = True
question_counter = 0

#greeting
print("Hello")
input()

#ask name
print("What is your name? ")
user_name = input()
print("It's nice to meet you, " + user_name + ".")

#ask about your day
print("How was your day? ")
user_day = input()
check(user_day)
random_pos_neg = get_pos_neg().lower()
print("My day has been " + random_pos_neg + ".")

#ask about the weather
weather = input("How is the weather today? ")
check(weather)

#ask about favorites
ask_random_favorite()

while conversing:
    question_counter += 1
    ask_random_favorite()
    if question_counter > 2:
        conversing = ask_keep_chatting()
        question_counter = 0
        
print("Goodbye!")