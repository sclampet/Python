# # Starting with the code snippet below, write a regex that will match:
# All words that contain a v
# All words that contain a double-s
# All words that end with an e
# All words that contain a b, any character, then another b
# All words that contain a b, at least one character, then another b
# All words that contain a b, any number of characters (including zero), then another b
# All words that include all five vowels in order
# All words that only use the letters in regular expression (each letter can appear any number of times)
# All words that contain a double letter

import re

def get_matching_words(regex):
	words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]

	return [word for word in words if re.search(regex, word)]

print get_matching_words(r'v')
print get_matching_words(r'ss')
print get_matching_words(r'e$') #ends with an e
print get_matching_words(r'b.b') #dinds one letter in between
print get_matching_words(r'b.+b') #at least one character between
print get_matching_words(r'b.*b') #any number of character between
print get_matching_words(r'aeiou') #all five vowels in order
print get_matching_words(r'[a-zA-z]') #only uses letter in regex expression
print get_matching_words(r'(.)\1') #any word containg a double letter