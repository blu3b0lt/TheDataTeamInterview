import pickle

synon = {"madras":["chennai"],
		"mas":["maa"]}

anton = {"hard" : ["soft", "easy"]}
with open('synon.b', 'w') as sy:
	pickle.dump(synon, sy)

with open('anto.b', 'w') as an:
	pickle.dump(anton, an)