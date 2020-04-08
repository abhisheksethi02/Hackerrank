if __name__ == "__main__":
    n = int(input())
    students = []
    for i in range(0,n):
        child = ["",0.0]
        child[0] = input()
        child[1] = float(input())
        students.append(child)
    students_dict = {}
    students_dict.update(students)
    min_key = min(students_dict, key = students_dict.get)
    students_dict.pop(min_key)
    req_keys = []
    min_key_2 = min(students_dict, key = students_dict.get)
    value = students_dict[min_key_2]
    while students_dict[min(students_dict,key=students_dict.get)] == value:
        temp_key = min(students_dict,key=students_dict.get)
        req_keys.append(temp_key)
        students_dict.pop(temp_key)
    for keys in req_keys:
        print(keys)