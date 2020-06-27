l={}
def ad():
   a=len(l.keys())
   n=int(input('\n\nHow Many Student`s details you want to Enter='))
   for y in range(n):
      s = []
      n=input('\nEnter Name:')
      s.append(n)
      print()
      Roll=input('Enter Roll No:')
      s.append(Roll)
      print()
      prn=input('Enter PRN:')
      s.append(prn)
      print()
      Cont=input('Enter Contact:')
      s.append(Cont)
      l[y+a]=s
   

