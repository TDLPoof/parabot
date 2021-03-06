def generateParable(s, computers, do):
	nounOrVerb = random.randint(0, 1)
	# pick a random key (computers can't / won't)
	key = random.randint(0, len(computers) - 1)
	s += " "
	# add that to the string
	s += computers[key]
	# same with what they can't do (feel, enjoy)
	task = random.randint(0, len(do) - 1)
	s += " "
	# same as last time
	s += do[task]
	# access the list I found of every noun
	nouns = open("nouns.csv")
	# take the actual words
	data = nouns.read()
	# data cleaning
	data = data.splitlines()
	for word in range(len(data)):
		data[word] = data[word].replace('"','')
	noun = random.randint(0, len(data) - 1)
	# if noun starts with a vowel, add an "n" to make "an"
	if data[noun][0] in ["a", "e", "i", "o", "u"] and s[-1] == "a":
		s += "n"
	s += " "
	# add the noun back
	s += data[noun]
	# return reassuring phrase
	return s

# Now, when the noun starts with a vowel, "an" is added rather than "a"
