numberinput=input("""
Welcome To Decimal Convertor
Steps:-
1.There is no step

Please enter the number that you want to convert from binary to decimal: """)

numberlist=[]
numberlist2=[]

decimalnumber=0

for i in range(len(numberinput)):
    numberlist.append(numberinput[i])

for i in range(len(numberlist)):
    number=int(numberlist[i])
    power=len(numberlist)-i-1
    number=number*2**power
    numberlist2.append(number)

for i in range(len(numberlist2)):
    decimalnumber=decimalnumber+numberlist2[i]

finalanswer=u"({})\u2082 = ({})\u2081\u2080".format(numberinput,decimalnumber)
  
print(finalanswer)

