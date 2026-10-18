class student:
    def __init__(self,name,age,puppy,game):
        self.name=name
        self.age=age
        self.puppy=puppy
        self.game=game
    def intro(self):
        print("my name is",self.name)
        print("my age is",self.age)
        print("my favorite game is",self.game)
    def add(self):
        print("my pet name is",self.puppy)
ob=student("Shahmir",13,"oreo","football")
ob.intro()
ob.add()

    