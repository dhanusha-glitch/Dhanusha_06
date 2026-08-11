# -------------------- Student Class --------------------

class Student:

    def __init__(self, student_id, name):
        self._student_id = student_id
        self._name = name


# -------------------- Subject Class --------------------

class Subject:

    def __init__(self, subject_name, marks):
        self.__subject_name = subject_name
        self.__marks = marks

    def get_name(self):
        return self.__subject_name

    def get_marks(self):
        return self.__marks

    def set_marks(self, marks):
        self.__marks = marks


# -------------------- Grade Calculator --------------------

class GradeCalculator:

    def calculate_average(self, subjects):

        total = 0

        for subject in subjects:
            total += subject.get_marks()

        return total / len(subjects)

    def calculate_grade(self, average):

        if average >= 90:
            return "A+"
        elif average >= 80:
            return "A"
        elif average >= 70:
            return "B"
        elif average >= 60:
            return "C"
        elif average >= 50:
            return "D"
        else:
            return "F"

    def result(self, average):

        if average >= 50:
            return "PASS"
        else:
            return "FAIL"


# -------------------- Report Card --------------------

class ReportCard:

    def __init__(self, student):
        self.student = student
        self.subjects = []
        self.calculator = GradeCalculator()

    def add_subject(self):

        name = input("Enter Subject Name: ")
        marks = float(input("Enter Marks: "))

        self.subjects.append(Subject(name, marks))

        print("Subject Added Successfully.")

    def update_marks(self):

        name = input("Enter Subject Name: ")

        for subject in self.subjects:

            if subject.get_name().lower() == name.lower():

                marks = float(input("Enter New Marks: "))
                subject.set_marks(marks)

                print("Marks Updated Successfully.")
                return

        print("Subject Not Found.")

    def display_report(self):

        if len(self.subjects) == 0:
            print("No Subjects Available.")
            return

        print("\n========== REPORT CARD ==========")
        print("Student ID :", self.student._student_id)
        print("Student Name :", self.student._name)

        total = 0

        print("\nSubject\t\tMarks")

        for subject in self.subjects:

            print(subject.get_name(), "\t\t", subject.get_marks())
            total += subject.get_marks()

        average = self.calculator.calculate_average(self.subjects)
        grade = self.calculator.calculate_grade(average)
        result = self.calculator.result(average)

        print("\nTotal Marks :", total)
        print("Average :", round(average, 2))
        print("Grade :", grade)
        print("Result :", result)


# -------------------- Main Program --------------------

student_id = input("Enter Student ID: ")
student_name = input("Enter Student Name: ")

student = Student(student_id, student_name)
report = ReportCard(student)

while True:

    print("\n======= STUDENT GRADE MANAGEMENT =======")
    print("1. Add Subject")
    print("2. Update Marks")
    print("3. Display Report Card")
    print("4. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        report.add_subject()

    elif choice == "2":
        report.update_marks()

    elif choice == "3":
        report.display_report()

    elif choice == "4":
        print("Thank You.")
        break

    else:
        print("Invalid Choice.")