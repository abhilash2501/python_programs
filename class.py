class basic:
    def __init__(self,name):
        self.name=name
    def show(self):
        print('name:%s'%self.name)

obj=basic("abc")
obj.show()
