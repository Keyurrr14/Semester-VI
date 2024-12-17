def soundex_generator(token):
	token = token.upper()
	soundex = ""
	soundex += token[0]
	dictionary = {
    "BFPV": "1",
    "CGJKQSXZ": "2", 
    "DT": "3",
    "L": "4", 
    "MN": "5",
    "R": "6",
    "AEIOUHWY": "."
    }
	for char in token[1:]:
		for key in dictionary.keys():
			if char in key:
				code = dictionary[key]
				if code != '.' and code != soundex[-1]:
						soundex += code
	soundex = soundex[:4]
	return soundex


print(soundex_generator('Information'))
