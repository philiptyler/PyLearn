# IMPORTS
# import math
from random import randint 


#   DECLARE SENTENCE SEGMENT ARRAYS
subject = ["oren", "isaac", "chris", "tobi", "dante", "yaniv", "clayton", "justin", "philip", "jimbo"]
verb = ["eats", "runs", "sucks", "eats", "loves", "reads", "understands", "just_barely_comprehends", "is_most_scared_of"]

# PT: no need for underscores in strings, you can use spaces!
predicate = ["the poop", "the penis", "the books", "the altitude", "the penis", "the toes"]


def generate_sentence():
	#   GENERATE SENTENCE
	subj_length = len(subject)-1
	verb_length = len(verb)-1
	pred_length = len(predicate)-1


	subj_index = randint(0,subj_length)
	verb_index = randint(0,verb_length)
	pred_index = randint(0,pred_length)

	return subject[subj_index] + " " + verb[verb_index] + \
							" " + predicate[pred_index]

# PT: This looks good but lets do it in a loop!

def generate_sentences(number_of_sentences):
	for num in range(0, number_of_sentences):
		generate_sentence()

print "printing one SENTENCE"
generate_sentences(1)

print "printing 3 sentences"
generate_sentences(3)

# print len(generate_sentence().split(' ')) == 4
