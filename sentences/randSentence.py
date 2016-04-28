#  IMPORTS
import math
import random


#   DECLARE SENTENCE SEGMENT ARRAYS
subject = ["oren", "isaac", "chris", "tobi", "dante", "yaniv", "clayton", "justin", "philip", "jimbo"]
verb = ["eats", "runs", "sucks", "eats", "loves", "reads", "understands", "just_barely_comprehends", "is_most_scared_of"]

# PT: no need for underscores in strings, you can use spaces!
predicate = ["the_poop", "the_penis", "the_books", "the_altitude", "the_penis,the_toes"]



#   GENERATE SENTENCE
slength = len(subject)-1
vlength = len(verb)-1
plength = len(predicate)-1


s = random.randint(0,slength)
v = random.randint(0,vlength)
p = random.randint(0,plength)


print subject[s], verb[v], predicate[p]

# PT: This looks good but lets do it in a loop!

def generate_sentences(number_of_sentences):
    for num in range(0, number_of_sentences):
        # PT: PUT YOUR CODE HERE

