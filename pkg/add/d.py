a=int(input('How Many Student`s details you want to Enter='))
l={}
for i in range(a):
    s = []
    n=input('Enter Name:')
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
    l[i]=s
counter=0
t=input('\n\nEnter the name whose details you want:')
l_v = [val for key,val in l.items() if t==val[0]]
a=len(l_v)
if a == 0:
    print('No Entry Found regarding your search\n\n')
    b=input('Do Your Want to try again(Y/N):')
    if b == 'Y':
        sea()
    elif b =='N':
        main1()
elif a >= 1:
    print(l_v)

