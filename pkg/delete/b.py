from pkg.add.a import *
def del1():
   counter = 0
   print(l)
   n=int(input('\n\nEnter the no. of entry you want to delete='))
   for i in l.copy():
      if i == n:
         del l[n]
      counter +=1
   if counter == len(l.keys()):
       print('Entry Not Found')
   
