from datetime import datetime
import time
class Bankatm:
    x=0
    l=[ ]
    pin_updated = 'no'
    def __init__(self,name,pin=1234,cardno=123400000000,mob=9533161639,adhar=436263906212):
        self.name=name
        self.pin=pin+Bankatm.x
        self.cardno=cardno+Bankatm.x
        self.bal=0
        self.mob=mob+Bankatm.x
        self.adhar=adhar+Bankatm.x
        self.mini_statement = ['                                                      ','                                                      ','                                                      ','                                                      ','                                                      ']
        Bankatm.x=Bankatm.x+1
        self.wait='no'
        c=self
        Bankatm.l=Bankatm.l+[c]

    def deposit(self):
        amt=float(self.get_amt())
        self.wait = 'wait'
        if amt>100:
            self.bal=self.add(self.bal,amt)
            now=datetime.now()
            str_date=now.strftime('%d/%m/%y %H:%M:%S')
            print(str_date,'deposit was done sucesssfully of {} available balance is {} '.format(amt, self.bal))
            trans=str_date+'          '+'deposit'+'          '+str(amt)+'          '+str(self.bal)
            self.mini_statement.append(trans)
        else:
            print('Amount should be grater than or equal to 100')
    def withdraw(self):
        amt=float(self.get_amt())
        self.wait = 'wait'
        if amt>=100:
            if amt<=self.bal:
                self.bal=self.sub(self.bal,amt)
                print('Available balance :',self.bal)
                now=datetime.now()
                str_date=now.strftime('%d/%m/%y %H:%M:%S')
                trans=str_date+'          '+'withdraw'+'          '+str(amt)+'          '+str(self.bal)
                self.mini_statement.append(trans)
                print(str_date,'withdraw was done sucessfully of ',amt,'available balance:',self.bal)
            else:
                print('insufficient balance available balance is :',self.bal)
        else:
            print('Amount should be grater than 100 and equal to 100')
    def bal_enq(self):
        print('Available balance :',self.bal)
        self.wait = 'wait'
    def mob_change(self):
        print('present mobile number is :',self.mob)
        new_mob=self.get_mob()
        self.mob=new_mob
        print('Mobile number updated sucessfully :',self.mob)
        self.wait = 'wait'
    def pin_change(self):
        print(self.pin)
        new_pin=self.get_pin()
        self.pin=new_pin
        print('updated pin :',self.pin)
        self.pin_updated='yes'
        self.wait = 'wait'
    def acc_details(self):
        print('NAME          :',self.name)
        print('Mobile Number :',self.mob)
        print('Balance       :',self.bal)
        print('Cardno        :',self.cardno)
        print('Adhar Number  :',self.adhar)


    @staticmethod
    def get_amt():
        return float(input('enter amount :'))
    @staticmethod
    def add(a,b):
        return a+b
    @staticmethod
    def sub(a,b):
        return a-b
    @staticmethod
    def get_mob():
        new_mob=int(input('Enter new mobile num :'))
        mm=str(new_mob)
        if len(mm)==10 and mm[0]=='9' or mm[0]=='8' or mm[0]=='7' or mm[0]=='6':
            return new_mob
        else:
            print('Mobile num should contain 10 digits and start with 9 or 8 or 7 or 6')
    @staticmethod
    def get_pin():
        new_pin=input('Enter new pin :')
        pp=str(new_pin)
        ii=0
        count=0
        for ii in range(4):
            for i in range(9):
                if int(pp[ii])==i:
                    count=count+1
        if len(pp)==4 and count==4:
            return int(new_pin)
        else:
            print('incorrect format of pin')


c1=Bankatm('Jayanth')
c2=Bankatm('Murali')
c3=Bankatm('Nehanth')
c4=Bankatm('Raju')
c5=Bankatm('Chand')
c6=Bankatm('Nazir')
c7=Bankatm('Deepak')
c8=Bankatm('Zeesanth')
c9=Bankatm('Abhay')
print(c1.name,':',c1.pin,'*',c2.name,':',c2.pin,'*',c3.name,':',c3.pin,'*',c4.name,':',c4.pin,'*',c5.pin,':',c5.pin,'*',c6.name,':',c6.pin,'*',c7.name,':',c7.pin,'*',c8.name,':',c8.pin,'*',c9.name,':',c9.pin)
print('Enter to Murali bank')
cc=0
while True:
    print('Press 1 for English')
    lang = input('Select Language :')
    jay=0
    if lang=='1':
        jay=1
        break
    else:
        print('incorrect option')
        print('press 11 to try again')
        option=(input('enter option :'))
        if option=='11':
            cc=cc+1
            if cc>2:
                break
        else:
            break

xx=2
vv=0

while jay==1:
    Name = (input('Enter Name :'))
    v = 0
    ee = 0
    pin = int(input('enter pin :'))
    for i in Bankatm.l:
        if i.name==Name.capitalize():
            while True:
                print('*'*50)
                if i.wait=='wait':
                    time.sleep(5)
                if i.pin_updated=='yes':
                    pin = int(input('New enter pin :'))
                if pin==i.pin:
                    print('*','welcome to Murali Bank', Name.capitalize())
                    print('*','press 2 for Withdraw')
                    print('*','press 3 for Deposit')
                    print('*','press 4 for Balance enquiry')
                    print('*','press 5 for Pin change')
                    print('*','press 6 for mobile number change')
                    print('*','Press 7 for account deatils')
                    print('*','press 8 for Mini_statement')
                    print('*','press 0 for exit')
                    choice=input('Enter choice :')
                    if choice=='2':
                        i.withdraw()
                    elif choice=='3':
                        i.deposit()
                    elif choice=='4':
                        i.bal_enq()
                    elif choice=='5':
                        i.pin_change()
                    elif choice=='6':
                        i.mob_change()
                    elif choice=='7':
                        i.acc_details()
                    elif choice=='8':
                        print(' DATE      TIME           TRANSCATION         AMT             BALANCE')
                        print(i.mini_statement[-1])
                        print(i.mini_statement[-2])
                        print(i.mini_statement[-3])
                        print(i.mini_statement[-4])
                        print(i.mini_statement[-5])

                    if choice=='0':
                        print('THANK YOU FOR BANKING')
                        ee=5
                        break
                else:
                    print('Incorrect pin')
                    print('*'*50)
                    print('Enter 142 for retry')
                    print('Enter 143 for exit')
                    print('*'*50)
                    rr=int(input('Enter choice :'))
                    if rr==142:
                        v=v+1
                        if v<=3:
                            pin = int(input('Enter pin :'))
                        else:
                            print('Maximum attempt reached chooor')
                            print('Thanking you for Banking')
                            ee=5
                            break
                    else:
                        print('choor')
                        ee=5
                        break
        if ee==5:
            break
    else:
        print('INVALID ACCOUNT')
        print('*'*50)
        rr=int(input('Enter 25 to try again 26 to exit:'))
        if rr==25:
            vv=vv+1
            if vv<3:
                pass
            else:
                print('Maximum attempts reached')
                break
        else:
            break
    if ee==5:
        break








