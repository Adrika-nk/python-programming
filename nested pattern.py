'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n-i):
        print(i,end='')
    print('')

00000
1111
222
33
4
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n-i):
        print(j,end='')
    print('')

01234
0123
012
01
0
'''

'''n=int(input("Enter a number"))
for i in range(n+1):
    for j in range(i):
        print(i,end='')
    print('')

1
22
333
4444
55555
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(i+1):
        print(i,end='')
    print('')

0
11
222
3333
44444
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print('')

*
**
***
****
*****
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n-i):
        print("*",end='')
    print('')

*****
****
***
**
*
'''
'''n=int(input("Enter a value"))
letter=65
for i in range(n):
    for j in range(i+1):
        print(chr(letter+i),end='')
    print('')

A
BB
CCC
DDDD
EEEEE
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i+1):
            print("*",end='')
    print('')

     *
    **
   ***
  ****
 *****
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(i+1):
        print(' ',end='')
    for k in range(n-i):
            print("*",end='')
    print('')

*****
 ****
  ***
   **
    *
'''
#triangle
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n-i):
        print(' ',end='')
    for k in range(i*2+1):
            print("*",end='')
    print('')


     *
    ***
   *****
  *******
 *********
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for k in range(2*(n-i)-1):
            print("*",end='')
    print('')

*********
 *******
  *****
   ***
    *
'''

'''n=int(input("Enter a value"))
for i in range(n):
    for j in range(i+1):
        print("*",end='')
    print('')
for i in range(n):
    for j in range((n-i)-1):
        print("*",end='')
    print('')

*
**
***
****
*****
****
***
**
*
'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range((n-i)-1):
        print(' ',end='')
    for k in range(i+1):
            print("*",end='')
    print('')
for i in range(1,n):
    for j in range(i):
        print(' ',end='')
    for k in range(n-i):
            print("*",end='')
    print('')

    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *
'''
#hourglass
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(i):
        print(' ',end='')
    for k in range(2*(n-i)-1):
            print("*",end='')
    print('')
for i in range(1,n):
    for j in range((n-i)-1):
        print(' ',end='')
    for k in range(i*2+1):
            print("*",end='')
    print('')

*********
 *******
  *****
   ***
    *
   ***
  *****
 *******
*********
'''


#square
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        print("*",end=' ')
    print(' ')

* * * * *  
* * * * *  
* * * * *  
* * * * *  
* * * * *  

'''

#upside down triangle
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range((n-i)-1): 
        print('*',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print(' ')

  * * * * * * * * *  
    * * * * * * *  
      * * * * *  
        * * *  
          *  
'''

#diamond
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n-i):
        print(' ',end=' ')
    for k in range(i):
        print('*',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print(' ')
for i in range(1,n):
    for j in range(i+1):
        print(' ',end=' ')
    for k in range((n-i)-1):
        print('*',end=' ')
    for k in range(n-i):
        print('*',end=' ')
    print(' ')

          *  
        * * *  
      * * * * *  
    * * * * * * *  
  * * * * * * * * *  
    * * * * * * *  
      * * * * *  
        * * *  
          *  
'''
