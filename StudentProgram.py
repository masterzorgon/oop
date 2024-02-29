import StudentClass as s

def main():
    student = s.Student(
        "123",
        "Nathan",
        "07/01/2001",
        "Sr"
    )

    student.set_age()
    print(student.get_age())

    student.set_registration_date()
    print(student.get_registration_date())



main()