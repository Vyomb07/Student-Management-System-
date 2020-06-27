from pkg.add.a import *
def sea():
    t=input('\n\nEnter the name whose details you want:')
    l_v = [val for key,val in l.items() if t==val[0]]
    a=len(l_v)
    if a == 0:
        print('No Entry Found regarding your search\n\n')
        b=input('Do Your Want to try again(Y/N):')
        if b == 'Y':
            sea()
    elif a >= 1:
        print(l_v)
    
        
