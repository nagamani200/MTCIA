class Complex():
      def __init__(self,real,img):
             self.real=real
             self.img=img
      def __add__(self,ob):
             temp=self.real+ob.real , self.img+ob.img
             return temp
      def __str__(self):
             return(self.real,self.img)
ob1=Complex(3,5)
ob2=Complex(2,1)
##ob3=ob1.add(obj2)
ob3=ob1+ob2
print(ob3)
##print(ob3.img)
##print(ob3.real)
