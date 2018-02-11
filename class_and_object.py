
class employee:
    #pass   #"putting a pass statement will let the python know to skip that class. this is done to keep a class empty"
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

    def email(self):
        return "{}.{}@charls.com" .format(self.fname,self.lname)

emp1 = employee('riwaj','chalise',50000)
emp2 = employee('ritesh','bhandari',60000)
print(emp1.email())
