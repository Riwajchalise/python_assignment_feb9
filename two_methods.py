class Name():

    def take_str(self):
        a =  input("enter a string")
        return a

    def to_upper(self,str):
        b = str.upper()
        print(b)


n1 = Name()
stri = n1.take_str()
print(n1.to_upper(stri))