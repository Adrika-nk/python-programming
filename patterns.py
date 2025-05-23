#square pattern
'''n=int(input("Enter a number"))

for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')''' 
#plus pattern
'''n=int(input("Enter a number"))

for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

    *     
    *     
* * * * * 
    *     
    * 
'''
#cross
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


*       * 
  *   *   
    *     
  *   *   
*       *'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if (i+j)%2==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

*   *   * 
  *   *   
*   *   * 
  *   *   
*   *   *'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 and j<=n//2 or j==2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * *     
    *     
    *     
    *     
    * '''  

n='''int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==0 and j<=n//2 or i==4 and j>=2 :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * *     
    *     
* * * * * 
    *     
    * * *'''

'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j==n//2 or i==0 and j<=n//2 or i==4 and j>=n//2 or j==4 and i<=n//2 or j==0 and i>=n//2 :
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')  
* * *   * 
    *   * 
* * * * * 
*   *     
*   * * *
'''

#diamond
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i+j==n//2 or i-j==n//2 or j-i==n//2 or i+j==n+n//2-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

        *         
      *   *       
    *       *     
  *           *   
*               * 
  *           *   
    *       *     
      *   *       
        *

'''

#arrow
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==n//2 or j-i==n//2 or i+j==n+n//2-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


        *         
          *       
            *     
              *   
* * * * * * * * * 
              *   
            *     
          *       
        *         
'''
