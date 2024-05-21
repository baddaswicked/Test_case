class Animal:
    color="white"

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def say(self):
        return " My cat [{:^5}] says Meow. And he is {:*^11}.".format(self.name,Animal.color)

cat=Animal("Robert",10)
print(cat.say())