import math
def lcm(x,y):
    a=x
    b=y
    if(a<b):
        a,b=b,a
       
    while(b!=0):
        k=a % b
        a=b
        b=k
    r=(x*y) / a
    return r


class fraction:
    def __init__(self,n1,d1,n2,d2):
        self.numerator1=n1
        self.denominator1=d1
        self.numerator2=n2
        self.denominator2=d2
    
    def add(self):
        if(self.denominator1==self.denominator2):
            print(self.numerator1+self.numerator2,"/",self.denominator1)
            

        else:

            k=lcm(self.denominator1,self.denominator2)
            print(self.numerator1*k+self.numerator2*k,"/",k)
            

    def sub(self):
        if(self.denominator1==self.denominator2):
            print(self.numerator1-self.numerator2,"/",self.denominator1)
            

        else:

            k=lcm(self.denominator1,self.denominator2)
            print(self.numerator1*k - self.numerator2*k,"/",k)
            

    def mul(self):
        print(self.numerator1*self.numerator2,"/",self.denominator1*self.denominator2)
        
    
    def div(self):
        print(self.numerator1*self.denominator2,"/",self.numerator2*self.denominator1)
        

    def print(self):
        print("Fraction1=",self.numerator1,"/",self.denominator1)
        print("Fraction2=",self.numerator2,"/",self.denominator2)

fr=fraction(2,6,5,3)
fr.print()
#menu

choice=int(input("1.add 2.sub 3.mul 4.div :"))
if(choice==1):
    fr.add()
elif(choice==2):
    fr.sub()
elif(choice==3):
    fr.mul()
elif(choice==4):
    fr.div()
else:
    print("something went wrong")


    
    



        
