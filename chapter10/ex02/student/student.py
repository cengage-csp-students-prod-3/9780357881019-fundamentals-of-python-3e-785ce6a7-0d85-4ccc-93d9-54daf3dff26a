def __str__(self):
    scores_str = ' '.join(str(score) for score in self.scores)
    return f"Name: {self.name}\nScores: {scores_str}"
class Student:
    def __init__(self, name, scores=None):
        self.name = name
        self.scores = scores if scores is not None else [0]*10

    def __str__(self):
        scores_str = ' '.join(str(score) for score in self.scores)
        return f"Name: {self.name}\nScores: {scores_str}"

    def __lt__(self, other):
        return self.name < other.name
import random
from student import Student

def main():
    # Create a list of Student objects
    students = [
        Student("Name1"),
        Student("Name3"),
        Student("Name5"),
        Student("Name2"),
        Student("Name4")
    ]

    print("Unsorted list of students:")
    for student in students:
        print(student)
    print()  # Blank line

    # Shuffle the list
    random.shuffle(students)

    print("Shuffled list of students:")
    for student in students:
        print(student)
    print()  # Blank line

    # Sort the list (uses __lt__ defined in Student)
    students.sort()

    print("Sorted list of students:")
    for student in students:
        print(student)

if __name__ == "__main__":
    main()
