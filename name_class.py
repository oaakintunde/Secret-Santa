
names = 'henry','tom','jerry'
print(type(names))

class Name:

    def __init__(self,name,*args) -> None:
        self.names = {name:''}
        for arg in args:
            self.names.update(arg)
