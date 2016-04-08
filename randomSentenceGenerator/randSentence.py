#  IMPORTS
import math
import random


#   DECLARE SENTENCE SEGMENT ARRAYS
subject = ["oren", "isaac", "chris", "tobi", "dante", "yaniv", "clayton", "justin", "philip", "jimbo"]
verb = ["eats", "runs", "sucks", "eats", "loves", "reads", "understands", "just_barely_comprehends", "is_most_scared_of"]
predicate = ["the_poop", "the_penis", "the_books", "the_altitude", "the_penis,the_toes"]



#   GENERATE SENTENCE
slength = len(subject)-1 
vlength = len(verb)-1
plength = len(predicate)-1


s = random.randint(0,slength)
v = random.randint(0,vlength)
p = random.randint(0,plength)


print subject[s], verb[v], predicate[p]
		  
