if __name__ == '__main__':
    students = []
    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input(f"Student {i+1} Name: ")
        score = float(input(f"Student {i+1} Score: "))
        students.append([name, score])

    scores = set()
    for student in students:
        scores.add(student[1])
    scores = sorted(scores)
    second_lowest_score = scores[1]

    second_lowest_students = []
    for student in students:
        if student[1] == second_lowest_score:
            second_lowest_students.append(student[0])

    second_lowest_students.sort()

    for name in second_lowest_students:
        print(f"Name of the student with 2nd highest score: {name}")
