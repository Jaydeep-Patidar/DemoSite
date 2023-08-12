from dynamic_data import*
students=select_all_student()
for student in students:
    print('roll no.:',student[0])
    print('name:',student[1])
    print('email:',student[2])
    print()