students=[]
password="khadija130"

class Student:
    def __init__(self,StudentID,Name,Age,Marks):
        self.StudentID=StudentID
        self.Name=Name
        self.Age=Age
        self.marks=Marks

    def totalMarks(self):
        total=0
        for subject in self.marks:
            total=total+self.marks[subject]
        return total

    def averageMarks(self):
        total_subjects=len(self.marks)
        if total_subjects==0:
            return 0
        return self.totalMarks()/total_subjects

    def assignGrades(self):
        avg=self.averageMarks()
        if avg>=80:
            return "A"
        elif avg>=70:
            return "B"
        elif avg>=60:
            return "C"
        elif avg>=50:
            return "D"
        else:
            return "F"

    def display_info(self):
        print("-----Student Information-----")
        print("ID:",self.StudentID)
        print("Name:",self.Name)
        print("Age:",self.Age)
        print("Marks:")
        for subject in self.marks:
            print(subject,":",self.marks[subject])
        print("Total:",self.totalMarks())
        print("Average:",round(self.averageMarks(),2))
        print("Grade:",self.assignGrades())

#-------------File Handiling -------------
def save_to_file():
    file=open("students.txt","w")
    for student in students:
        marks_data=""
        for subject in student.marks:
            marks_data=marks_data+subject+":"+str(student.marks[subject])+","
        data=student.StudentID+"|"+student.Name+"|"+str(student.Age)+"|"+marks_data+"|"+"\n"
        file.write(data)
    file.close()


def load_from_file():
    try:
        file=open("students.txt","r")
        for line in file:
            line=line.strip()
            if line!="":
                parts=line.split("|")
                student_id=parts[0]
                name=parts[1]
                age=int(parts[2])
                marks_data=parts[3]
                marks={}
                subjects=marks_data.split(",")
                for item in subjects:
                    if item!="":
                        subject_info=item.split(":")
                        subject_name=subject_info[0]
                        subject_marks=int(subject_info[1])
                        marks[subject_name]=subject_marks
                student=Student(student_id,name,age,marks)
                students.append(student)
        file.close()
    except:
        print("No previous file found.")

#--------------- Main Menu Functions ---------------
def add_student():
    StudentID=input("Enter Student ID: ")
    name=input("Enter Student Name: ")
    age=int(input("Enter Age: "))
    marks={}
    total_subjects=int(input("Enter Number of Subjects: "))
    for i in range(total_subjects):
        subject=input("Enter Subject Name: ")
        score=int(input("Enter Marks: "))
        marks[subject]=score
    student=Student(StudentID,name,age,marks)
    students.append(student)
    save_to_file()
    print("Student Added Successfully")


def view_students():
    if len(students)==0:
        print("No students available")
        return
    for student in students:
        student.display_info()


def search_student():
    choice=input("Search by ID or Name: ")
    found=False
    for student in students:
        if student.StudentID==choice or student.Name.lower()==choice.lower():
            student.display_info()
            found=True
    if found==False:
        print("Student Not Found.")


def update_marks():
    StudentID=input("Enter Student ID: ")
    found=False
    for student in students:
        if student.StudentID==StudentID:
            subject=input("Enter Subject Name: ")
            if subject in student.marks:
                new_marks=int(input("Enter New Marks: "))
                student.marks[subject]=new_marks
                save_to_file()
                print("Marks Updated Successfully")
            else:
                print("Subject Not Found")
            found=True
    if found==False:
        print("Student Not Found.")


def show_topper():
    if len(students)==0:
        print("No students available.")
        return
    topper=students[0]
    for student in students:
        if student.averageMarks()>topper.averageMarks():
            topper=student
    print("\nTopper Student")
    topper.display_info()


def delete_student():
    student_id=input("Enter Student ID to Delete: ")
    found=False
    for student in students:
        if student.StudentID==student_id:
            students.remove(student)
            save_to_file()
            print("Student Deleted Successfully!")
            found=True
            break
    if found==False:
        print("Student Not Found.")

entered_password=input("Enter System Password: ")

if entered_password!=password:
    print("Wrong Password!")
    print("Access Denied.")
else:
    print("Login Successful!")
    load_from_file()

    while True:
        print("\n----Smart Student Management System----")
        print("1.Add Student")
        print("2.View All Students")
        print("3.Search Student")
        print("4.Update Marks")
        print("5.Show Topper")
        print("6.Delete Student")
        print("7.Exit")

        choice=input("Enter Your Choice: ")

        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice=="4":
            update_marks()
        elif choice=="5":
            show_topper()
        elif choice=="6":
            delete_student()
        elif choice=="7":
            print("Exiting Program...")
            save_to_file()
            break
        else:
            print("Invalid Choice.")