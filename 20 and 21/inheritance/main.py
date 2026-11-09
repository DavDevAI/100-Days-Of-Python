class Animal:
    def __init__(self):
        self.num_eyes = 2
    def breathe(self):
        print("Inhale, Exhale")

#HERE IS WHERE INHERITANCE HAPPENS
#I ONLY HAVE TO PASS THE OTHER CLASS BETWEEN PARENTHESIS IN THIS OTHER ONE
class Fish(Animal):
    def __init__(self): #I code the constructor or initializer
        super().__init__() #I put the super of the father class or greater class using the keyword super and the initializer to mark I am calling the init of the superclass or fatherclass
        #IN THE CONSTRUCTOR THE CALL TO super() is recommended but not strictly required

        

    #what if I want to inherit a method but adjust it at my own needs
    def breathe(self):
        super().breathe() # I call to breathe from the superclass
        #does the same as the superclass, but also I want to add that the fish does it underwater
        print("doing this underwater")

    def swim(self):
        print("Swim, Swim")

nemo = Fish()
nemo.swim()
#now I can get my nemo to start breathing
nemo.breathe()
print(nemo.num_eyes) #I can also access to his eyes, because of inheritance the nemo fish now has a pair of eyes
