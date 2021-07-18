
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])

students = 0
total_height = 0
for height in student_heights:
  total_height += height
  students +=1

avg = round(total_height / students)

print(avg)