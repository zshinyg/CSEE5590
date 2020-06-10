#Write a program that accepts a sentence and replace each occurrence of ‘python’ with ‘pythons’ without using regex

pyWord = "python"

print("Please Type a sentence that includes the word python.\n")
sentence = input()                                                          # take in a sentence

if not pyWord in sentence:
    print("That sentence does not inlcude python. Please try again.\n")     # make sure the sentence contains python
    sentence = input()

sentence.lower()                                                            # convert the sentence to lowercase just in case
                                                                            # the first word is python. 
print("Here is your new sentence:\n")
print(sentence.replace("python", "pythons"))                                #print the new sentence
