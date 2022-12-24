import random
from datetime import date
class Person:
    hobby='Drawimg'
    def __init__(self,firstName,lastName,age):
        #public proerties
        self.firstName=firstName
        self.lastName=lastName
        self.age=age
        #private properties
        self.__personId=random.randint(1,100)
    #private method
    def __showId(self):
        print(self.__personId)
    #public methods
    def getInfo(self):
        self.__showId()
        return f"Person first name-{self.firstName};\n" \
               f"last name-{self.lastName}\n" \
               f"age-{self.age}"
    def getHi(self,msgText):
        return f'{msgText}! I am {self.firstName}'
    #static method
    @staticmethod
    def sayGreeting():
        print('These are our colleagues')

    @staticmethod
    def per():
        print('There are all our colleagues!')

    #class method
    @classmethod
    def setdefaulthobby(cls):
        cls.hobby='Programming'

    @classmethod
    def BasedonYear(cls,firstName,lastName,bYear):
        personAge=date.today().year-bYear
        return cls(firstName,lastName,personAge)

    @classmethod
    def is_sick(cls):
#        cls.__sick=sick_leave

        sick_leave=input("Was the person ill during last time, yes/no?: ")
        if sick_leave=="yes":
            day_of_sick=int(input("Enter quantity of days the person was ill: "))
            print(f"Due to disease your promotion postpone for {day_of_sick} days ")
        else:
            print("You'll receive your promotion as soon as possible")


    @classmethod
    def basedonStr(cls,strinf):
        firstName,lastName,age=strinf.split(' ')
        return cls(firstName,lastName,age)
class Developer(Person):
    def __init__(self,firstName,lastName,age,jobTitle):
        super().__init__(firstName,lastName,age)
        self.jobTitle=jobTitle
        self.__salary=0
        self.bonus=int(input("Enter quantity of positive feedbacks: "))
    def setBasicSalary(self):
        if self.__rung=='Junior':
            self.__salary=1000
        elif self.__rung=='Middle':
            self.__salary=2000
        elif self.__rung=='Senior':
            self.__salary=5000
        elif self.__rung=='Lead':
            self.__salary=10000

    @classmethod
    def feedback(cls,bonus):

        return (bonus//100)

    @classmethod
    def setRung(cls,rungName):
        cls.__rung=rungName



    def calculateSalary(self,perc):
        return self.__salary+self.__salary*perc

    def getInfo(self):
        return super().getInfo()+f'\njobTitle - {self.jobTitle}' \
                                 f'\nrung - {self.__rung}' \
                                 f'\nbasic salary - {self.__salary}'



person_1=Person("Kate","Smith",22)
print(person_1.sayGreeting())
Developer.is_sick()

Developer.setRung('Junior')
jun1=Developer('Kate','Smith',22,'UI designer')
jun2=Developer("Joe","Black",30, 'back-end developer')
for jun in zip((jun1,jun2),(0.25,0.3)):
    jun[0].setBasicSalary()
    print(jun[0].getInfo())
    print(f'expected salary:{jun[0].calculateSalary(jun[1])} + {jun[0].feedback(jun[1])} as bonus \n')
    print(jun1.is_sick())
    print(jun2.is_sick())


Developer.setRung('Middle')
midl1=Developer("Alice","fox",29,'Web developer')
midl2=Developer('Anna','Morning',35,'Data scientist')
midl3=Developer('Bob',"Dilan",32,'System analyst')

for mid in zip((midl1,midl2,midl3),(0.2,0.41,0.15)):
    mid[0].setBasicSalary()
    print(mid[0].getInfo())
    print(f'expected salary:{mid[0].calculateSalary(mid[1])} + {mid[0].feedback(mid[1])} as bonus  \n')
    print(midl1.is_sick())
    print(midl2.is_sick())
    print(midl3.is_sick())

Developer.setRung('Senior')
sen1=Developer('Max',"White",43,'System analyst')
sen2=Developer('John',"Lenon",39,'Full stack')
for sen in zip((sen1,sen2),(0.15,0.4)):
    sen[0].setBasicSalary()
    print(sen[0].getInfo())
    print(f'expected salary:{sen[0].calculateSalary(sen[1])}\n')
    print(sen1.is_sick())
    print(sen2.is_sick())

Developer.setRung('Lead')
lead=Developer('Nick','Black',38,'Team lead')
lead.setBasicSalary()
print(lead.getInfo())
print(f'expected salary:{lead.calculateSalary(0.32)}\n')
person_2=Person("Nick","Black",38)
print(person_2.per())
print(lead.is_sick())