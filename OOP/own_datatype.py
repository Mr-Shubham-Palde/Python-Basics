#befor going to study to create our own datatype you should read the following.


"""
Golden rule of oop: all the atrributes and methods
in the class  are  only accesed by the object of the class.
that means the object is able to accesed everything present in the class only and only object not the function .

Concept of self: aas we see that only the object of a class can accessed the methods and attrbutes of class and if two methods want to talk to each other it is possible with the help of "self".constructor calls the object that is self and that self calls the methods so that they can talk to each other.  self is nothing but the object.(understand with the help of Basic Atm machine code )

Single line to explain: Gangadhar hi sakthiman hai

"""

''''
Magic Methods:__str__:  1)it's superpower is ki jab bhi aap apne object ko print function mai daloge, to wo print karne ke liye direct str function mai jayega 
there are also different magic methods like add subtract ,multiply division
'''



#in this we are going to create our own datatype fraction

class Fraction:
    def __init__(self,a,b):#parameterized constructor:which accept the parameters
        self.num=a
        self.den=b

    def __str__(self):
        return "{}/{}".format(self.num,self.den)
    def __add__(self,other):#it accpets two objets self and other one
        new_num= (self.num*other.den+self.den*other.den)
        new_den=(self.den*other.den)
        return "{}/{}".format(new_num,new_den)


fr1=Fraction(3,4)
fr2=Fraction(7,4)
print(type(fr1))
print(fr1)
print(fr1+fr2)#similiarly we can do for oother stuff like -,* and/ (this have same syntax as that of add only the calculations are different)
