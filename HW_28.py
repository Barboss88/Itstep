class Student:
    def __init__(self,name,surname,age):
        self.imya = name
        self.surname = surname
        self.age = age
        self.kabinet = 0
        self.budj =''

    @classmethod
    def speccialityChange(cls,spec):
        cls.specciality=spec

    @classmethod
    def vartistChange(cls,cina):
        cls.vartist=int(cina)

    @classmethod
    def  tryvalist_kursu(cls,tryv):
        cls.tryv=int(tryv)

    @classmethod
    def place_of_birth(cls,place):
        cls.place = place

    @classmethod
    def grupa(cls,group):
        cls.group=int(group)

    @classmethod
    def prof (cls,teacher):
        cls.teacher = teacher

    def auditory(self):
        if self.specciality == 'Python':
            self.kabinet = 33
        elif self.specciality == 'UI/UX':
            self.kabinet = 21
        elif self.specciality == "Economy":
            self.kabinet = 18
        else:
            self.kabinet = "We dont have this speciality"

    def budj_or_kontract(self):
        if self.vartist == 0:
            self.budj = "budjet"
        elif 10000 > self.vartist > 0:
            self.budj= "kontract"
        elif self.vartist > 10000:
            self.budj= f"kontract i zaborgovanist {self.vartist - 10000} grn"
        else:
            self.budj= "can not be -"

    def showInfo(self):
        return f"name: {self.imya}\n" \
               f"surname: {self.surname}\n" \
               f"place of birth: {self.place}\n" \
               f"speciality: {self.specciality}\n" \
               f"cabinet №: {self.kabinet}\n" \
               f"vartist navchannya: {self.vartist}\n" \
               f"forma oplaty: {self.budj}\n" \
               f"tryvalist kursu: {self.tryv}\n" \
               f"number of students in the group: {self.grupa}\n" \
               f"Group teachers name: {self.prof}"

    @staticmethod
    def propusk():
        x = int(input("Enter num of lessons which student doesnt visit: "))
        if x >= 10:
            print("You need to compensate your courses to pass exam")
        else:
            print('Ok, you can pass your exam')



    @staticmethod
    def exam():
        t = "Does student need to pass exams?: "
        if t == 'y':
            print("You will have exam next week")
        else:
            print(" You will have your exam next month")

    @staticmethod
    def info_about_program():
        print("This program can help you get info about student")

    @staticmethod
    def administration():
        print(" In any case please contact our administration by number 222-11-44")


    @staticmethod
    def feedback():
        m = int(input("Please evaluate our courses from 1 to 5, where 1 - very bad, 5 - where good"))
        if m == 1:
            print(input("Please describe what we were wrong to do: "))
        elif m == 2:
            print(input("Please describe what we were wrong to do: "))
        elif m == 3:
            print(input("Please input what we could improve: "))
        elif m == 4:
            print(input("Thanks for your feedback, any questions: "))
        elif m == 5:
            print(input("Thanks for your feedback< what we can do for you else?: "))
        else:
            return "Please enter from 1 to 5!"


    @staticmethod
    def end():
        print("Thank you for using this app!")

Student.info_about_program()
while True:
    try:
        a = input("info about student?")
        if a == 'y':
            name, surname, age, place, speciality, price, tryv, grupa, teacher = map(str, input("Enter name, surname, age, place of birth, speciality, price, tryvalist, group, teachers name: ").split())
            Student.speccialityChange(speciality)
            Student.vartistChange(price)
            Student.tryvalist_kursu(tryv)
            Student.grupa(grupa)
            Student.prof(teacher)
            Student.place_of_birth(place)
            stud = Student(name,surname,age)
            stud.auditory()
            stud.budj_or_kontract()
            print(stud.showInfo())
            print(stud.propusk())
            print(stud.exam())
            print(stud.administration())
            print(stud.feedback())
        elif a == "n":
            Student.end()
            break
    except:
        print('not correct info')