keepgoing = True
array = ["Maths", "English", "History", "Geography", "Science"]
results = {}    #add students grades to results dictionary

def print_grades():
    for key,value in results.items():
        print("\n",key)
        for subject,score in value.items():
            print("\t",subject,score)

def maths_average():
    #compute the average

while keepgoing == True:
    name = input("Student's Name: ")
    results[name] = {}
    for subject in array:
        grade = input("{} Score: ".format(subject))
        results[name][subject] = grade
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
        print_grades()
        #maths_average()
    else:
        continue
