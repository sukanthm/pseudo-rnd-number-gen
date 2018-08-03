import time
import datetime
a=datetime.timedelta(milliseconds=0)
names=['sukanth','akanksha','jobin','rahul','soumik','suraj','yasha','ronith','sudheer','abhabya','rakesh','alok','sandeep','nethra','naveen']
#print [x for x in names if len(x)>5] #1 line array iterator
names=sorted(names)
while len(names)>0:
 x=datetime.datetime.now()+a
 y=x.year+x.month+x.day+x.hour+x.minute+datetime.datetime.now().second+datetime.datetime.now().microsecond
 if(datetime.datetime.now().microsecond/1000%2==0):
  y=int(str(y)[::-1])
  a+=datetime.timedelta(milliseconds=datetime.datetime.now().microsecond/1000) #to increase randomness
 
 else:
  y=y%3
  a+=2*datetime.timedelta(milliseconds=datetime.datetime.now().microsecond/1000) #to increase randomness
 z=float(int(y))/10**(len(str(y)))
 i=int(z*len(names))
 #print i,len(names),a #compare numbers generated with total
 time.sleep(0.3)
 names[i]
 del names[i]


