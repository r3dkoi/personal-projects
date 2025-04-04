"""CONEXT:
For example, suppose a university professor collects data about their students, 
including the number of lectures attended, the hours spent studying, and the 
final grade achieved on the end of term exam. The professor could analyze the data to determine 
if there is a relationship between the amount of studying a student undertakes and the final grade they achieve. 
The professor might use the data to test a hypothesis that only students who study for a minimum number of hours can 
expect to achieve a passing grade."""

import numpy as np

grades_data = [50,50,47,97,49,3,53,42,26,74,82,62,37,15,70,27,36,35,48,52,63,64]

#Transforming List into a NumPy Array for efficient numerical operations
grades = np.array(grades_data)

#Define an array of study hours
study_hours = [10.0,11.5,9.0,16.0,9.25,1.0,11.5,9.0,8.5,14.5,15.5,
               13.75,9.0,8.0,15.5,8.0,9.0,6.0,10.0,12.0,12.5,12.0]

#Create 2D array of student study hours and their grades
student_data = np.array([study_hours, grades])

#Show shape of 2D array
print(f"The shape of the 2D array is: {student_data.shape}")

#Show first element of the first element
print(f"The first element of the first element is: {student_data[0][0]}")

#Get the mean value of each sub-array
avg_study = student_data[0].mean() #The first array
avg_grade = student_data[1].mean() #The second array

print('Average study hours: {:.2f}\nAverage grade:{:.2f}'.format(avg_study, avg_grade))
