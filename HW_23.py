# 1

import random
class Student:
    def __init__(self,name):
        self.name=name
        self.gladness=200
        self.progress=0
        self.money=500
        self.work=True
        self.alive=True
    def to_study(self):
        print("Time to study: ")
        self.progress+=0.12
        self.gladness-=0.3
        self.money-=0.5
    def to_sleep(self):
        print("I will sleep")
        self.gladness+=0.15
        self.money-=1.2
    def to_chill(self):
        print("Rest time: ")
        self.gladness+=0.25
        self.progress-=0.1
        self.money-=0.2
    def get_work(self):
        print("Side job,good choice")
        self.gladness-=0.8
        self.progress+=0.5
        self.money+=0.4

    def is_alive(self):
        if self.progress<-0.5:
            print('Cast out')
            self.alive=False
        elif self.gladness<=0:
            print("Depression")
            self.alive=False
        elif self.progress>100:
            print('Passed externally...')
            self.alive=False
        elif self.money<=0:
            print('starve to death')
            self.alive=False
        elif self.work== False:
            print('No money to live')
            self.alive=False

    def end_of_day(self):
        print(f"Gladness={self.gladness}")
        print(f'Progress={round(self.progress,2)}')
        print(f"Money = {self.money}")

    def live(self,day):
        day="Day"+ str(day) + 'of' +self.name + 'life'
        print(f'{day:=^50}')
#        live_cube=int(input("Enter 1 to study,"
#                            "2 - sleep, "
#                            "3 - chill, "
#                            "4 - work: "))
        live_cube=random.randint(1,4)
        if live_cube==1:
            self.to_study()
        elif live_cube==2:
            self.to_sleep()
        elif live_cube==3:
            self.to_chill()
        elif live_cube==4:
            self.get_work()

        self.end_of_day()
        self.is_alive()
nick=Student(name='Nick')
for day in range(365*4):
    if nick.alive==False:
        break
    nick.live(day)