#Variables Practice
import datetime
mynow = datetime.datetime.now()
print(mynow)

mynumber = 10
mytext = "Hello"

print(mynumber, mytext)

#Lists Practice

student_grades = {"Mary": 9.1, "John": 8.8, "Jeff": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean) 
