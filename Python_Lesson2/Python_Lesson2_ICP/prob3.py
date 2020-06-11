dict_wordCount = dict()

with open("prob3.txt", 'w+') as infile:
    for line in infile:
        for word in line.split():
            if word in dict_wordCount:
                dict_wordCount[word] = dict_wordCount[word] + 1
            if not word in dict_wordCount:
                dict_wordCount[word] = 1

print(dict_wordCount)
        
