from django.http import HttpResponse
from django.shortcuts import render
import ast
# Create your views here.

def index(request):
    return render(request, "index.html")


def process(request):
    if request.method == "POST":
        parameters = request.POST
        dictonary = parameters.get('dictonary')
        input_text = parameters.get('input')
        dictonary = ast.literal_eval(dictonary)
        result = working(dictonary, input_text)
        return render(request, "result.html", {'details':result})


def working(synon, input_data):

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

                line_number = line_number + 1
                for key in synon.keys():
                    line_number_key = "Line " + str(line_number)
                    para_number_key = "Para " + str(para_number)
                    words = []
                    words_with_special_character = line.split()
                    for word in words_with_special_character:
                        words.append("".join(e for e in word if e.isalnum()))
                    print words
                    if key in words:
                        occurence = words.count(key)
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
                    for synon_word in synon[key]:
                        if synon_word in words:
                            occurence = words.count(synon_word)
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

    print result
    return result