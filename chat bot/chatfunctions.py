import random
from getfunctions import *

def learn(new_word):
    good_or_bad = input("Is that good or bad? ")
    good_or_bad = good_or_bad.upper()
    if good_or_bad == "GOOD":
        #add to positives
        with open("positives.txt", "a") as pos:
            pos.write("\n" + new_word)
    else:
        #add to negatives
        with open("negatives.txt", "a") as neg:
            neg.write("\n" + new_word)
    print("Ok, I'll remember that. " + new_word + " is a new word for me.")

def check_positives(word):
    #open positives list
    with open("positives.txt", "r") as pos:
        pos_words = pos.read().split()
        #check if word is in list
        if word in pos_words:
            return True
        else:
            return False

def check_negatives(word):
    #open negatives list
    with open("negatives.txt", "r") as neg:
        neg_words = neg.read().split()
        #check if word in list
        if word in neg_words:
            return True
        else:
            return False

def check(word):
    word = word.upper()
    word_positive = check_positives(word)
    word_negative = check_negatives(word)
    if word_positive:
        print("I'm glad!")
    elif word_negative:
        print("Oh, that's too bad.")
    else:
        learn(word)

def check_affirmatives(word):
    with open("affirmatives.txt", "r") as aff:
        aff_words = aff.read().split()
        #check if word in list
        if word in aff_words:
            return True
        else:
            return False

def ask_random_favorite():
    #get a random thing to ask about
    random_thing = get_random_word("thing").lower()
    #ask about the users favorite
    favorite = input("What is your favorite " + random_thing + "? ")
    #say wow I like that too
    print("Wow! I like " + favorite.lower() + " too!")
    
def ask_keep_chatting():
    keep_chatting = input("Would you like to keep chatting? ")
    if check_affirmatives(keep_chatting.upper()):
        conversing = True
    else:
        conversing = False
    return conversing