class std(Name, Rollno, prn, Cont):
   def __init__(self,Name,Rollno,PRN,Contact):
      self.Name=Name
      self.Rollno=Rollno
      self.PRN=PRN
      self.Contact=Contact

   def a():
      n=int(input('How Many Student`s details you want to Enter='))
      for i in range(n):
         l={}
         Name=input('Enter Name:')
         l['Name']=Name
         Rollno=input('Enter Roll No:')
         l['Rollno']=Rollno
         prn=input('Enter PRN:')
         l['PRN']=prn
         Cont=input('Enter Contact:')
         l['Contact']=Cont

   def d():
      # Print the names of the columns. 
      print ("{:<10} {:<10} {:<10}  {:<10}".format('NAME', 'Roll No', 'PRN','Contact')) 
        
      # print each data item. 
      for key, value in l.items(): 
          N = l['Name']
          R = l['Rollno']
          P = l['PRN']
          C = l['Contact']
          print ("{:<10} {:<10} {:<10} {:<10}".format(N, R , P, C))
          if N[0]==N[1]:
             counter=1
          else:
             counter=0

          if counter==0:
             breakpoint

obj=std()
obj()
             
   

