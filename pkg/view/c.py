from pkg.add.a import *
def dis():
    a = bool(l)
    if a == False:
        print('No Entries Found')
        c=input('Do You want to add Details(Y/N):')
        if c == 'Y':
            ad()
        elif c == 'N':
            main1()
    elif a == True:
        print ("\n\n{:<10} {:<10} {:<10}  {:<10}".format('NAME', 'Roll No', 'PRN','Contact')) 
        for key, value in l.items():
            N, R,P,C= value
            print ("{:<10} {:<10} {:<10} {:<10}".format(N, R , P, C))
    
        
