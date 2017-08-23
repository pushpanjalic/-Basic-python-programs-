def length():
    
    vowel = ["a","e","i","o","u"]
    string = input('enter a string')
    count=0
    for i in range(0,len(string)):
        count=count+1
        
    if(count==1):
        for i in range(0, len(vowel)):

            if string == vowel[i]:
                
                print('yes its a vowel' + '\t TRUE')
                break
                
            else:
                print('not a vowel' + '\tFALSE')
                break
    else:
         print('not entered properly')
length()
