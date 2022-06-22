class Student:  # parentclass

    def __init__(self, student_id, student_name, roll_no):
        self.student_id = student_id
        self.student_name = student_name
        self.roll_no = roll_no

    def display_details_of_students(self):
        print(f"Student ID = {self.student_id}, Student Name = {self.student_name}, Roll_No = {self.roll_no}")


student1 = Student(1234, "Amala", 674589)
student1.display_details_of_students()


class ShortPumpElementary(Student):  # childclass
    def __init__(self, student_id, student_name, roll_no, school_name, address):
        super().__init__(student_id, student_name, roll_no)
        #Student.__init__(self,student_id, student_name, roll_no)
        self.school_name = school_name
        self.address = address

    def display_details_of_students(self):
        print(
            f"Student ID = {self.student_id}, Student Name = {self.student_name}, Roll_No = {self.roll_no},School Name = {self.school_name}, Address = {self.address}")

student2 = ShortPumpElementary(4578, "Ramya", 65678747, "Short Pump", "Pump Rd")
student2.display_details_of_students()

class ColonialTrial(Student):  # childclass(multiple)
    def __init__(self, student_id, student_name, roll_no, school_name, address):
        super().__init__(student_id, student_name, roll_no)
        #Student.__init__(self,student_id, student_name, roll_no)
        self.school_name = school_name
        self.address = address

    def display_details_of_students(self):
        print(
            f"Student ID = {self.student_id}, Student Name = {self.student_name}, Roll_No = {self.roll_no},School Name = {self.school_name}, Address = {self.address}")


class Grade5(ShortPumpElementary):  # childclass to #childclass(#multilevel inheritance)

    pt_hrs = 11

    def __init__(self, student_id, student_name, roll_no,school_name,address,subject):
        super().__init__(student_id, student_name, roll_no,school_name,address)
        #Student.__init__(self,student_id, student_name, roll_no)
        self.subject = subject

    def display_details_of_students(self,count):#instance method(it can be accessed only when object created)
        details = super().display_details_of_students()
        count += 1
        print(count)
        print(f"Subject = {self.subject}")

    @classmethod#decorator
    def display_pt_hrs(cls):
        cls.pt_hrs = 15
        print(cls.pt_hrs)

    @staticmethod #decorator
    def display_info():
        print("We are Fifth Grade Students")

#Grade5.display_pt_hrs()
#Grade5.display_info()





fifth = Grade5(244,"vidya",656575,"Short Pump","Pump Rd",["Maths","Science","Computer"])
#fifth.display_details_of_students()
#fifth.display_info()
#fifth.display_pt_hrs()
fifth_1 = Grade5(244,"vidya",656575,"Short Pump","Pump Rd",["Maths","Science","Computer"])
fifth.display_details_of_students(10)
fifth_1.display_details_of_students(20)
