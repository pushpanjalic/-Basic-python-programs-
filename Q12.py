def palindrom():
     string=input('enter a string')
     reverse =(string[::-1])
     for i in range (0,len(string)):

         if(string[i] == reverse[i]):
             print('palindrom string')
             break
         else:
              print('not a palindrome')
              break
palindrom()        
