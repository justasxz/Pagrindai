class Dog():
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
    
    def __str__(self):
        return f"Dog(name={self.name})"
    
    def __repr__(self):
        return f"Dog({self.name!r})"