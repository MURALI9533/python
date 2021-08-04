
l=list(range(1,61))
def seat():
    count = 0
    for i in l:
        if count==0:
            if len(str(i))==1:
                print(' '+'|'+str(i)+'|'+'            ',end='')
            else:
                 print('|'+str(i)+'|' + '            ', end='')
            count+=1
        elif count==1:
            if len(str(i)) == 1:
                print(' '+'|'+str(i)+'|'+'     ',end='')
            else:
                print('|'+str(i)+'|' + '     ', end='')
            count+=1
        elif count==2:
            if len(str(i)) == 1:
                print(' '+'|'+str(i)+'|')
                print()
            else:
                print('|'+str(i)+'|')
                print()
            count=0
    print('*'*50)

while True:
    print('enter 1 seat map')
    print('enter 2 to book seat')
    print('enter 3 to cancel booking')
    print('enter 4 to exit')
    jay = input('enter choice :')
    if jay=='1':
        seat()
    elif jay=='2':
        seatno=int(input('enter seat number:'))
        if l[seatno-1]!='Booked':
            l[seatno-1]='Booked'
        else:
            print('seat already booked')
            print('try again')
    elif jay=='3':
        seatno = int(input('enter seat number:'))
        if l[seatno-1]=='Booked':
            l[seatno-1]=seatno
            seat()
            print('thanks for using murali bus booking')
            break
        else:
            print('seat not booked yet')
    elif jay=='4':
        print('thanks for using murali bus booking')
        break



