print("=============WELCOME BACK=============")
print(" ")
print("=========🎒High School Grades=========")
print(" ")

grade_question = int(input("Enter your high school grade number: "))

if grade_question == 9:
    print("Freshman")
elif grade_question == 10:
    print("Sophomore")
elif grade_question == 11:
    print("Junior")
elif grade_question == 12:
    print("Senior")
else:
    print("TBD")
