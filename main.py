# 🚨 FOR Loop. Average Height

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    #print(student_heights)
    # [156, '178', '165', '171', '187']
    # [156, 178, '165', '171', '187']
    # [156, 178, 165, '171', '187']
    # [156, 178, 165, 171, '187']
    # [156, 178, 165, 171, 187]

# simple way
# total_height = sum(student_heights)
# number_of_students = len(student_heights)
# average_height = round(total_height / number_of_students)
# print(average_height)
# #171 - result

# hard way
# replicate "sum" function
total_height = 0
for hight in student_heights:
    #"total_height = total_height + hight" the same "total_height += hight"
    total_height += hight
    # print(total_height)
    # 156
    # 334
    # 499
    # 670
    # 857
print(total_height)
#857 - result