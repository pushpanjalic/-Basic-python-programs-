num1=input("enter the first number")
num2=input("enter the second number")
num3=input("enter the third number")
def fun (n1,n2,n3):
      
    if(n1>n2 and n1>n3):
        print(n1 +"\tnumber first is greater than second and third")
    elif(n2>n1 and n2>n3):
        print(n2 +"\tnumber second is greater than first and third")
        
    else :
        print(n3 +"\tnumber third is greater than first and second ")
fun(num1,num2,num3)
