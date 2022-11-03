import random

def get_random_positive():
    with open("positives.txt", "r") as pos:
        pos_words = pos.read().split()
        word = pos_words[random.randint(0, len(pos_words) - 1)]
        return word

def get_random_negative():
    with open("negatives.txt", "r") as neg:
        neg_words = neg.read().split()
        word = neg_words[random.randint(0, len(neg_words) - 1)]
        return word

def get_pos_neg():
    #generate a random word
    random_number = random.randint(0, 1)
    if random_number == 0:
        #get a positive
        word = get_random_positive()
    else:
        #get a negative
        word = get_random_negative()
    #return a random word
    return word

def get_thing():
    with open("things.txt", "r") as things:
        things = things.read().split()
        word = things[random.randint(0, len(things) - 1)]
    return word

def get_random_word(kind):
    if kind == "eval":
        word = get_pos_neg()
    elif kind == "thing":
       word = get_thing()
    return word