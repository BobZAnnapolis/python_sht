from statistics import mean as m

admins = { 'Python':'Pass123@', 
           'user2':'pass2'
         }

studentDict = { 'Jeff':[78,88,93],
                'Alex':[92,76,88],
                'Sam':[89,92,93],
              }

print("\n24: FINAL PROJECT")
print("================\n")

print("...combine everything from previous lessons...")

## ####################################
## START - define functions
## ####################################

def separator():
    print("\n## ##################################################\n")


def enterGrades():
    nameToEnter = input("Student Name: ")

    if nameToEnter in studentDict:
        print("...Adding grade...")
        gradeToEnter = input("Grade ")
        studentDict[nameToEnter].append(int(gradeToEnter))
        print(studentDict)
    else:
        print("Student does not exist.")


def removeStudent():
    nameToRemove = input('What student to remove ?: ')
    if nameToRemove in studentDict:
        print('Removing student...')
        del studentDict[nameToRemove]
        print(studentDict)


def studentAvgs():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = m(gradeList)
        print(eachStudent,"has an average grade of",avgGrade)


def getChoice():
    print("""
    Welcome to Grade Central

    [1] - Enter Grades
    [2] - Remove Student
    [3] - Student Average Grades
    [4] - Exit
    """
    )

    action = input('What would you like to do today ? (Enter a number) ')

    if action == '1':
        enterGrades()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAvgs()
    elif action == '4':
        print("Thank you, goodbye")
        exit()
    else:
        print("No valid choice was given, try again")

## ####################################
## END - define functions
## ####################################

## *********************************** 
## START - main program 
## *********************************** 

separator()

login = input("Username: ")

if login in admins:
    passw = input("Password: ")
    if admins[login] == passw:
        print('Welcome,',login)
        while True:
            getChoice()
    else:
        print("\nInvalid password, will detonate in 5 seconds.\n")
else:
    print('\n',login,'is an invalid Username, calling FBI to report this.\n')

("\n...run  is over...\n")


