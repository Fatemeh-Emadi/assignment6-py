import math
from statistics import mode
class Time:
    def __init__(self,h=0,m=0,s=0):
        self.hour=h
        self.minute=m
        self.second=s
        self.fix_time()

    def fix_time(self):
        if self.second>=60:
            while self.second>=60:
                self.second-=60
                self.minute+=1
        if self.minute>=60:
            while self.minute>=60:
                self.minute-=60
                self.hour+=1
        
        if self.second<0:
            while self.second<0:
                self.second+=60
                self.minute-=1
        if self.minute<0:
            while self.minute<0:
                self.minute+=60
                self.hour-=1


    def show_time(self):
        print("Time:",self.hour,":",self.minute,":",self.second)

    def add(self,time2):
        result=Time()
        result.hour=self.hour + time2.hour
        result.minute=self.minute + time2.minute
        result.second=self.second + time2.second
        result.fix_time()
        return result

    def sub(self,time2):
        result=Time()
        result.hour=self.hour - time2.hour
        result.minute=self.minute - time2.minute
        result.second=self.second - time2.second
        result.fix_time()
        return result

    def secTotime(self,seconds):
        result=Time()
        result.hour=seconds/3600
        ashar1=result.hour-math.floor(result.hour)
        if(ashar1==0):
           result.minute=0
           result.second=0
        else:

            result.minute=ashar1*60
            ashar2=result.minute-math.floor(result.minute)
            if(ashar2==0):
               result.second=0
            else:
               result.second=ashar2*60
        print(int(result.hour),":",int(result.minute),":",int(result.second))
    
    def timeTosec(self,times):
        result=(times.hour*3600 + times.minute*60 + times.second)
        print("seconds:",result)
    
        
time1=Time(6,20,35)
time1.show_time()
time2=Time(4,32,43)
time2.show_time()
result1=time1.add(time2)
result2=time1.sub(time2)
print("Add->",end=" ")
result1.show_time()
print("Sub->" ,end=" ")
result2.show_time()
time1.secTotime(1374829)
time1.timeTosec(time2)










        
    
    


