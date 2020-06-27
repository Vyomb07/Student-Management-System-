from pkg.add.a import ad
from pkg.delete.b import del1
from pkg.view.c import dis
from pkg2.modify.d import mod
from pkg2.search.e import sea

def main1():
        print('\n\n-----Student Management------')
        print('1)Add Details of Student')
        print('2)Delete Details ')
        print('3)View Details')
        print('4)Modify Details')
        print('5)Search Details')
        print('6)Exit')
        a=int(input('Enter Your Choice='))
        if a==1:
                ad()
        elif a==2:
                del1()
        elif a==3:
                dis()
        elif a==4:
                mod()
        elif a==5:
                sea()
        elif a==6:
                exit()
        else:
                print('Wrong Choice')
        main1()
        
        
if __name__=='__main__':
        try:
                main1()
        except Exception:
                print('Invalid Input')
        finally:
                print("Press Enter to continue ...")
                input()
                main1()



