from pkg.add.a import *
from pkg.view.c import *
def mod():
   t=input('Enter the name whose details you want to modify:')
   x=0
   for i in l[x]:
       for x in l.values():
           pass
   if x[0] == t:
       a=int(input('\n1)Name\n2)Roll No\n3)PRN\n4)Contact\n5)Exit\nEnter which detail you want to change:'))
       if a == 1 :
           b=input('Enter New Name:')
           x[0]=b
       elif a == 2:
           b=input('Enter New Roll No:')
           x[1]=b
       elif a == 3:
           b=input('Enter New PRN:')
           x[2]=b
       elif a == 4:
           b=input('Enter New Contact:')
           x[3]=b
       elif a == 5:
           main()
       else:
           print('Wrong Choice!!')
       m=input('Do you want to view updated list(Y/N):')
       if m == 'Y':
           dis()
       else:
           main()
   else:
       print('No Entry Found')
