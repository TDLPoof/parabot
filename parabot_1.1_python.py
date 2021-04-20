# Reassuring parable bot
import random

def generateParable(s, computers, do):
    nounOrVerb = random.randint(0, 1)
    # pick a random key (computers can't / won't)
    can = random.randint(0, len(computers) - 1)
    s += " "
    # add that to the string
    s += computers[can]
    if (nounOrVerb == 0): # noun case
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
    else: # verb case
        # access the list I found of verbs
        verbs = open("verbs.csv")
        # take actual words
        data = verbs.read()
        # data cleaning
        data = data.splitlines()
        for wordIndex in range(len(data)):
            data[wordIndex] = data[wordIndex].lower()
        verb = random.randint(0, len(data) - 1)
        s += " " + data[verb]

    return s

# parabot now has a 50% chance of generating a verb-based phrase, like "Computers can't [verb]" in addition to noun phrases.
