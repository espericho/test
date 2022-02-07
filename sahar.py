class Animal:

    def __init__(self,species,name):
        self.species=species
        self.name=name

    def sound(self):
        if self.species=='Cat':
            print('meyooo')
        elif self.species=='Dog':
            print('woof')
        else:
            print('no way')

class Human(Animal):

    def __init__(self,name):
        Animal.__init__(self)
        self.name=name


cat=Animal('Cat','pishi')
cat.sound()
human=Human('sahar')
human.sound()
