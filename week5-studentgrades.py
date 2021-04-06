keepgoing = True
array = ["Maths", "English", "History", "Geography", "Science"]
results = []    #add students grades to results array

def print_results():
    for score in results:       #for i in range(1,length of array)
        print(score)            #   score = array[i]

while keepgoing == True:
    for subject in array:
        grade = input("{} Score: ".format(subject))
        results.append(grade)
    Continue = input("Do you want to continue? (y/n) : ")
    if Continue == "y" or Continue == "yes":
        continue
    elif Continue == "n" or Continue == "no":
        keepgoing = False
    else:
        print("Error!")
        keepgoing = False

    display = input("Do you want to see all of the results? (y/n) : ")
    if display == "y" or display == "yes":
        print_results()
    else:
        continue
