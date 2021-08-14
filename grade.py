marks = input("Enter marks: ")
marks = int(marks)

if marks >= 80: # if the marks are equal or greater than 80
    grade = "A+"

elif marks >= 70:
    grade = "A"

elif marks >= 60:
     grade = "A-"

elif marks >=50:
      grade = "B"

else:
     grade = "Fail"

print("Grade is", grade)

# if we use elif, if the 1st one is matching with the condition,the condition will be true.