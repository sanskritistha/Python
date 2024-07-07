#wap to overload + opeartor to add time objects that contains the instance variables hr,mins,sec
class Time:
    def __init__(self,hr,mins,sec):
        self.hr=hr
        self.mins=mins
        self.sec=sec
    def __add__(self,other):
        sec=self.sec+other.sec
        mins=self.mins+other.mins +sec//60
        hr=self.hr+other.hr +mins//60
        sec=sec%60
        mins=mins%60
        return Time(hr,mins,sec)
         
t1=Time(5,40,48)
t2=Time(6,50,35)

t3=t1+t2
print(t3.hr,t3.mins,t3.sec)
