dict_wordCount = dict()

with open('prob3.txt', 'r') as file:
    for line in file:
        for word in line.split():
            if word in dict_wordCount:
                dict_wordCount[word] = dict_wordCount[word] + 1
            if not word in dict_wordCount:
                dict_wordCount[word] = 1
file.close()

file = open('prob3.txt', 'w')
for x in dict_wordCount: 
    print(x,":", dict_wordCount[x])
    file.write(x)
    file.write(": ")
    file.write(str(dict_wordCount[x]))
    file.write("\n")

    
file.close
        
