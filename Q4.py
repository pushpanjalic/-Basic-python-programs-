a=input('a no.divisible by 2')
a=int(a)
flag=0
if(a%2==0):
    
    print('correct no is divisible by 2')
    flag= -1
else:
    print("enter a correct no.")
    flag= 1
    
while (flag== 1 or flag==0):
    
    a=input('a no.divisible by 2')
    a=int(a)
    flag=0
    if(a%2==0):
    
        print('correct no is divisible by 2')
        flag-=1
        
