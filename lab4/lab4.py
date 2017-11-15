##class Animal(object):
##    def __init__(self, sound, name, age, favorite_color):
##        self.sound=sound
##        self.name=name
##        self.age=age
##        self.favorite_color=favorite_color
##
##    def eat(self, food):
##        print("yummy "+self.name+" is eating "+food)
##
##    def description(self):
##        print(self.name+" is "+str(self.age)+" years old and loves the color "+self.favorite_color)
##    def make_sound(self,num):
##        print (self.sound*num)
##i=Animal("bark","shosha",2,"blue")
##i.eat("cake")
##i.description()
##i.make_sound(5)    


class Person(object):
    def __init__(self,name,age,city,gender):
        self.name=name
        self.age=age
        self.city=city
        self.gender=gender

        
    def eat(self, breakfast):
         print("yummy "+self.name+" is eating "+breakfast)
         
    def talk(self,sentence):
        print(sentence)



i=Person("noam",15,"sarid","female")
i.eat("cookies")
i.talk("hello world")   
