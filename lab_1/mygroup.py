def print_students(students, mark):
    num = 1
    cols = [3, 0, 0, 0, 0, 4]

    for stud in students:
        col = 1
        for key in stud.keys():
            if len(str(stud[key])) > cols[col]:
                cols[col] = len(str(stud[key]))
            col += 1
    
    print("Num", "Name".ljust(cols[1]), "Surname".ljust(cols[2]),
          "Exams".ljust(cols[3]), "Marks".ljust(cols[4]), "Mid mark")
    
    for stud in students:
        mid_mark = sum(stud["marks"])/len(stud["marks"])
        if mid_mark > mark:
            print(str(num).ljust(cols[0]),
                  stud["name"].ljust(cols[1]), 
                  stud["surname"].ljust(cols[2]), 
                  str(stud["exams"]).ljust(cols[3]),
                  str(stud["marks"]).ljust(cols[4]),
                  str(round(mid_mark, 2)).ljust(cols[5]))
            num += 1
    return 0


students = [
    {
        "name": "Павел",
        "surname": "Горшков",
        "exams": ["Вышмат", "Аиг", "Физика"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Дмитрий",
        "surname": "Орлов",
        "exams": ["История", "Английский", "Русский язык"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Елизавета",
        "surname": "Жукова",
        "exams": ["Философия", "ЭВМ", "Вычтех"],
        "marks": [5, 5, 5]
    },
    {
        "name": "Иван",
        "surname": "Плюшкин",
        "exams": ["Аиг", "История", "ЭВМ"],
        "marks": [3, 3, 3]
    },
    {
        "name": "Владимир",
        "surname": "Попов",
        "exams": ["Английский", "Физика", "Вышмат"],
        "marks": [4, 4, 5]
    },
    {
        "name": "Николай",
        "surname": "кузнецов",
        "exams": ["История", "Русский язык", "Философия"],
        "marks": [3, 5, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Зайцева",
        "exams": ["Аиг", "Вычтех", "Русский язык"],
        "marks": [4, 3, 4]
    }
]


print_students(students, int(input()))



