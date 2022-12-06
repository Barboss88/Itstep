# 1

'''class Human:
    def about (self,average_height=171, average_mass=77, average_lifecycle=70):
        super().__init__()
        print("For human  being: ")
        self.average_height=average_height
        self.average_mass=average_mass
        self.average_lifecycle=average_lifecycle
        print(f"Average height for human being is: {average_height}")
        print(f"Average mass for human being is: {average_mass}")
        print(f"Average life cycle for human being is: {average_lifecycle}")
        print("________________")

class Builder(Human):
    def builder (self):
        super().about()
        profession="Builder"
        self.capabilities="construct buildings"
        self.coordination="coordinates his part of project"
        self.organisation="organises contractors to work on the project"
        print(f"{profession} as a representative of human species has the next: ")
        print(f"Average height: {self.average_height}")
        print(f"Average mass: {self.average_mass}")
        print(f"Average life cycle: {self.average_lifecycle}")
        print(f"{profession} being the representative of his/her profession has to do: {self.capabilities}")
        print(f"During his work {profession}: {self.coordination}")
        print(f"The average life cycle for this profession is: {self.organisation}")
        print("________________")
class Sailor(Human):
    def sailor (self):
        super().about()
        profession = "Sailor"
        self.capabilities="operate the vessel"
        self.coordination="coordinates the maintenance of the vessel"
        self.organisation="take direction and follow the chain of command"
        print(f"{profession} as a representative of human species has the next: ")
        print(f"Average height: {self.average_height}")
        print(f"Average mass: {self.average_mass}")
        print(f"Average life cycle: {self.average_lifecycle}")
        print(f"{profession} being the representative of his/her profession has to do: {self.capabilities}")
        print(f"During his work {profession}: {self.coordination}")
        print(f"The average life cycle for this profession is: {self.organisation}")
        print("________________")
class Pilot(Human):
    def pilot (self):
        super().about()
        profession = "Pilot"
        self.capabilities="operate the  air vessel"
        self.coordination="coordinates the maintenance of the air vessel"
        self.organisation="take direction of air vessel"
        print(f"{profession} as a representative of human species has the next: ")
        print(f"Average height: {self.average_height}")
        print(f"Average mass: {self.average_mass}")
        print(f"Average life cycle: {self.average_lifecycle}")
        print(f"{profession} being the representative of his/her profession has to do: {self.capabilities}")
        print(f"During his work {profession}: {self.coordination}")
        print(f"The average life cycle for this profession is: {self.organisation}")

human=Human()
builder=Builder()
print(builder.builder())
sailor=Sailor()
print(sailor.sailor())
pilot=Pilot()
print(pilot.pilot())'''

# 2

'''class Passport:
    def __init__(self,firstname,lastname,pass_num):
        super().__init__()
        self.firstname=firstname
        self.lastname=lastname
        self.pass_num=pass_num
    def about(self):
        return f"Person first name-{self.firstname};\n" \
               f"Last name-{self.lastname}\n" \
               f"Id number-{self.pass_num}"
class Foreign_Passport(Passport):
    def __init__(self,firstname,lastname,foreign_id,visa):
        super().__init__(firstname, lastname,pass_num)
        self.foreign_id=foreign_id
        self.visa=visa

    def for_pass (self):
        return super().about() + "\n"+f'foreign passport id: {self.foreign_id} + "\n"+f"number of open visas: {self.visa}"'
print("Info about national passport: ")
person=Passport(firstname=input("Enter surname: "),lastname=input("Enter name: "),pass_num=int(input("Enter national passport number: ")))
print("________________________________________")
print("Information about foreign passport: ")
person_1=Foreign_Passport(firstname=input("Enter surname: "), lastname=input("Enter name: "),
                          foreign_id=int(input("Enter foreign id number: ")),visa=int(input("Number of open visas: ")))
print(person.about() + person_1.for_pass())'''



# 3

'''class Animal:
    def __init__(self, eukaryotic, multicellular, heterotroph, motile, respire_aerobically):
        super().__init__()
        self.eukaryotic = eukaryotic
        self.multicellular = multicellular
        self.motile = motile
        self.heterotroph = heterotroph
        self.respire_aerobically = respire_aerobically

    def about(self):
        print("The main particularities from Kingdom of 'Animals' are the next :")
        return f"\nTheir cells have a nucleus so they are - {self.eukaryotic};" \
               f"\nTheir organisms consist of more then one cell< so they are - {self.multicellular};" \
               f"\nThey can move independently, using metabolic energy, so they are - {self.motile};" \
               f"\nThey cannot produce their own food, instead taking nutrition from other sources of organic carbon, so they are - {self.heterotroph};" \
               f"\nThey use oxygen for respiration, so they - {self.respire_aerobically} etc."


class Reptile(Animal):
    def __init__(self,vertebrates,scale, cold_blood, eggs,eukaryotic, multicellular, heterotroph, motile, respire_aerobically):
        super().__init__(eukaryotic, multicellular, heterotroph, motile, respire_aerobically)
        self.vertebrates=vertebrates
        self.scale=scale
        self.cold_blood=cold_blood
        self.eggs=eggs

    def get_info(self):
        print("\nFrom Kingdom Animal they take:")
        return super().about() + f"\nReptiles have backbones, so they are {self.vertebrates};" \
                                 f"\nTheir bodies are completely covered with scales, so they are {self.scale};" \
                                 f"\nIn an organism of Reptile internal physiological sources of heat are of relatively small or of quite negligible importance in controlling body temperature, so they are {self.cold_blood};" \
                                 f"\nAs for their live young they {self.eggs} etc."


class Mammal(Animal):
    def __init__(self,hair_or_fur, warm_blood, milk, born_alive, brain,eukaryotic, multicellular, heterotroph, motile, respire_aerobically):
        super().__init__(eukaryotic,multicellular,heterotroph,motile,respire_aerobically)
        self.hair_or_fur=hair_or_fur
        self.warm_blood=warm_blood
        self.milk=milk
        self.born_alive=born_alive
        self.brain=brain

    def mammal_info(self):
        return super().about() + f"\nMammals could be classified in the next way:" \
                                 f"\nMammals have {self.hair_or_fur};" \
                                 f"\nThey are {self.warm_blood};" \
                                 f"\nTheir young are fed {self.milk} produced by the mother's mammary glands;" \
                                 f"\nMost of them are {self.born_alive};" \
                                 f"\nThey have more {self.brain} than other animals etc."

class Crocodile(Reptile):
    def __init__(self,largest_reptiles,tears,food, digestion,eukaryotic,multicellular,heterotroph,motile,respire_aerobically,vertebrates,scale,cold_blood,eggs):
        super().__init__(eukaryotic,multicellular,heterotroph,motile,respire_aerobically,vertebrates,scale,cold_blood,eggs)
        self.largest_reptiles=largest_reptiles
        self.tears=tears
        self.food=food
        self.digestion=digestion

    def crocodile_info(self):
        return reptile.get_info() + f"\nAt the same time Crocodiles are:" \
                                                    f"\n{self.largest_reptiles} in the whole world;" \
                                                    f"\nCrocodile really do produce {self.tears};" \
                                                    f"\nThey can not {self.food};" \
                                                    f"\nThey swallow stones to improve {self.digestion} etc."


class Tiger(Mammal):
    def __init__(self, largest_cat, roar, speed, stripe, hair_or_fur, warm_blood, milk, born_alive, brain, eukaryotic,
                 multicellular, heterotroph, motile, respire_aerobically):
        super().__init__(hair_or_fur, warm_blood, milk, born_alive, brain, eukaryotic, multicellular, heterotroph,
                         motile, respire_aerobically)
        self.largest_cat=largest_cat
        self.roar=roar
        self.speed=speed
        self.stripe=stripe

    def tiger_info(self):
        return mammal.mammal_info() + f"\nSome facts about tigers:" \
                                                    f"\n{self.largest_cat} in the whole world;" \
                                                    f"\nA tiger’s {self.roar} can be heard as far as three kilometres away;" \
                                                    f"\nAt full speed, tigers can reach up to {self.speed};" \
                                                    f"\nNo two tigers have the same {self.stripe} etc."


class Kangaroos(Mammal):
    def __init__(self, Marsupials, left_hande, mob, enemie,hair_or_fur, warm_blood, milk, born_alive, brain,
                 eukaryotic, multicellular, heterotroph, motile, respire_aerobically):
        super().__init__(hair_or_fur, warm_blood, milk, born_alive, brain, eukaryotic, multicellular, heterotroph,
                             motile, respire_aerobically)
        self.Marsupials=Marsupials
        self.left_hande=left_hande
        self.mob=mob
        self.enemie=enemie

    def kangaroos_facts(self):
        return mammal.mammal_info() + f"\nSome facts about kangaroos:" \
                                                    f"\nKangaroos are {self.Marsupials} in the whole world;" \
                                                    f"\nRecent research suggests {self.left_hande} is also common in kangaroos;" \
                                                    f"\nKangaroos travel and feed in groups known as {self.mob}, troops, or herds it may include a handful or several dozen individuals;" \
                                                    f"\nOnce a kangaroo is chest-deep in the water, it will sometimes turn around and confront the {self.enemie}, grabbing it with its forelimbs and attempting to drown it, etc."


animal = Animal("Eukaryotics","Multicellulars","Heterotrophs","Motiles","Respire aerobically")
print(animal.about())
print("________________________________")
reptile=Reptile ("Vertebrates","Scaled","Cold-blooded","produce shelled eggs or bear live young","Eukaryotics","Multicellulars","Heterotrophs","Motiles","Respire aerobically")
print(reptile.get_info())
print("________________________________")
crocodile=Crocodile("Largest reptiles","tears","chew food","digestion","Vertebrates","Scaled","Cold-blooded","produce shelled eggs or bear live young","Eukaryotics","Multicellulars","Heterotrophs","Motiles","Respire aerobically")
print(crocodile.crocodile_info())
print("________________________________")
mammal=Mammal("hair or fur","warm-blooded","by milk","mostly born alive","complex brain", "Eukaryotics","Multicellulars","Heterotrophs","Motiles","Respire aerobically")
print(mammal.mammal_info())
print("________________________________")
tiger=Tiger("The largest wild cat","roar","65 km/h","stripes", "hair or fur","warm-blooded","by milk","mostly born alive","complex brain", "Eukaryotics","Multicellulars","Heterotrophs","Motiles","Respire aerobically")
print(tiger.tiger_info())
print("________________________________")
kangaroos=Kangaroos("biggest Marsupials","handedness","mob","predator","hair or fur","warm-blooded","by milk","mostly born alive","complex brain", "Eukaryotics","Multicellulars","Heterotrophs","Motiles","Respire aerobically")
print(kangaroos.kangaroos_facts())'''