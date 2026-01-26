def add_student(students_dict, name, scores):
    avg = sum(scores) / len(scores)
    students_dict[name] = {
        "scores": scores,
        "avg": avg
    }


def get_letter_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'


def passing_students(students_dict):
    return {name for name, data in students_dict.items() if data["avg"] >= 70}


def print_report(students_dict):
    for name, data in students_dict.items():
        avg = data["avg"]
        grade = get_letter_grade(avg)
        print(f"Name: {name} | Avg: {avg:.2f} | Grade: {grade}")


def main():
    students = {}

    # Test data
    add_student(students, "Alice", [85, 92, 78])
    add_student(students, "Bob", [88, 65, 92])
    add_student(students, "Charlie", [95, 91, 98])
    add_student(students, "Diana", [55, 62, 58])
    add_student(students, "Eve", [78, 82, 79])

    print_report(students)
    print("Passing students:", passing_students(students))


main()
