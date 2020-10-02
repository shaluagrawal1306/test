def checkprime (n):
 flag = 'true'
 if n<2:
   flag = 'false'
 else:
     if n==2:
      flag = 'true'
 for i in range (2,n):
     if n%i == 0:
       flag = 'false'
 return flag
n=int(input("enter a number"))
a = checkprime (n)
if a=='true':
 print('no.is prime')
else:
 print('no.is not prime')