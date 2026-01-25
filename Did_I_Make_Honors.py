#Kyle Hensley
#File name: Did_I_Make_Honors?_.py
#Description: This is an app that allows you to input a student's gpa, first and last name, then it determines if that student made the Honor Roll or the Dean List. 




while True:
    last_name = input("Enter student's last name (or ZZZ to quit): ")

    if last_name == "ZZZ":
        print("Exiting program.")
        break
    if last_name == "zzz":
        print("Exiting program.")
        break
    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List.")
    elif gpa >= 3.25:
        print(first_name, last_name, "has made the Honor Roll.")
    else:
        print(first_name, last_name, "did not qualify for honors.")

    print()