# PROB 2:  Input the string “Python” as a list of characters from console, 
#          delete at least 2 characters, reverse the resultant string and print it.


PythonStr = "str"

while(PythonStr != 'Python'):                                   # Take in Python input from console
    PythonStr = input("Please type the string 'Python': ") 

pyList = list(PythonStr)                                        # convert to list of chars

pyList.remove('P')                                              # remove P and O
pyList.remove('o')

pyList.reverse()                                                # Reverse the List

newPythonStr = ''.join(pyList)                                  # Convert List to String

print(newPythonStr)