class belva:

    def introduce(self):
        print("My name is", self.name)
        print("I am an", self.ethnicity)
        print("I am", self.age)

b1 = belva()
b1.name = "Belva"
b1.age = 18
b1.ethnicity = "Indonesian"

b1.introduce()