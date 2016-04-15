# The dictonary of Synonyms and dictionary of antonyms is saved
# as a binary using python 'Pickle' for easy retrieval of key value pair

import pickle


def load_dict(filename):
	with open(filename) as fn:
		dictonary = pickle.load(fn)
	return dictonary
# Load the pickled dictonary into synon and anton

# Script dict_initialse.py is used to create pickled dict

#format is "key":["value1", "value2"]


synon = load_dict("synon.b")
anton = load_dict("anto.b")


# read input file

with open("input.txt") as ip:
	input_data = ip.read()


input_data = input_data.lower()

paras = input_data.split("\n")

para_number = 0
line_number= 0

line_count =0
para_count = 0

result = {}

for para in paras:
	para_number = para_number + 1
	lines = para.split(".")
	for line in lines:
		if len(line) > 0:
			print "Line-----" + line
			line_number = line_number + 1
			for key in synon.keys():
				line_number_key = "Line " + str(line_number)
				para_number_key = "Para " + str(para_number)
				if key in line:
					occurence = line.count(key)
					if key not in result.keys():
						result[key] = {line_number_key : occurence, para_number_key : occurence, "total" : occurence}
					else:
						if line_number_key not in result[key]:
							result[key][line_number_key] = 0
						if para_number_key not in result[key]:
							result[key][para_number_key] = 0
						result[key][line_number_key] += occurence
						result[key][para_number_key] += occurence
						result[key]["total"] += occurenceoccurence
				for synon_word in synon[key]:
					if synon_word in line:
						occurence = line.count(synon_word)
						print "occurence----" + str(occurence) 
						if key not in result.keys():
							result[key] = {line_number_key : occurence, para_number_key : occurence, "total" : occurence}
						else:
							if line_number_key not in result[key]:
								result[key][line_number_key] = 0
							if para_number_key not in result[key]:
								result[key][para_number_key] = 0
							result[key][line_number_key] += occurence
							result[key][para_number_key] += occurence
							result[key]["total"] += occurence

print synon

print anton

print input_data


print result

with open("output.txt", "w") as op:
	for key in result.keys():
		details = result[key]
		op.write(key + "\n")
		for detail in details.keys():
			if detail != "total":
				op_text = str(detail) + " : " + str(details[detail])
				op.write(op_text + "\n")
	op_text = "Total Per File: " + str(details["total"])
	op.write(op_text + "\n")
