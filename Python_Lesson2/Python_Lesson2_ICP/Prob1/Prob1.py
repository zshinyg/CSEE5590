# Write a program, which reads weights (lbs.) of N students into a list and convert these weights to kilograms in 
# a separate list using:
# 1) Loops and
# 2) List comprehensions
# N: No of students (Read input from user)
# Ex: 	L1: [150,155, 145, 148]
# Output: [68.03, 70.3, 65.77, 67.13]


NumberOfStudents = 0
list_WeightsInLBS = []
list_WeightsInKilograms =[]
list_roundedWeightsInKilograms = []
i = 0

def lbsToKilogramsConversion(lbs = 0):                                     #function that converts lbs to kilograms
    kilograms = lbs * 0.45359237
    return kilograms


NumberOfStudents = input("Please Enter the number of students you would like in the list:")
NumberOfStudents = int(NumberOfStudents)                                                        #convert input to int

while i < NumberOfStudents:
    list_WeightsInLBS.insert(i,int(input("Enter the students weight in lbs:")))                 #insert the weights for the  
                                                                                                #specified number of students.
                                                                                                #Preemptivly converted the values
                                                                                                #to int as well.                                  
    
    list_WeightsInKilograms.insert(i,lbsToKilogramsConversion(list_WeightsInLBS[i]))            #populate the list of converted
                                                                                                #values. lbs to kilograms.
    
    i = i + 1


list_roundedWeightsInKilograms = [round(num,2) for num in list_WeightsInKilograms]              #round weights to hundreths place

print("List in lbs: ", list_WeightsInLBS)

print("List in kilograms:" , list_roundedWeightsInKilograms)


