'''
Given the names and grades for each student in a Physics class of N students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.
'''

if __name__ == "__main__":
    n = int(input())
    students = []
    for i in range(0,n):
        child = ["",0.0]
        child[0] = input()
        child[1] = float(input())
        students.append(child)
    names = []
    marks = []
    for student in students:
        names.append(student[0])
        marks.append(student[1])
    z = min(marks)
    while min(marks) == z:
        names.pop(marks.index(min(marks)))
        marks.pop(marks.index(min(marks)))
    z_1 = min(marks)
    output = []
    for i in range(len(marks)):
        if marks[i] == z_1 :
            output.append(names[i])
    final_output = sorted(output)
    for name in final_output:
        print(name)