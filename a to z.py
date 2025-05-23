#A shape
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * * * * 
*       * 
* * * * * 
*       * 
*       *



'''

#A arch
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 and i!=0 or i==0 and j!=0 and j!=n-1 or j==n-1 and i!=0 or i==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')'''

#B
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 and j!=n-1 or i==n//2 and j!=n-1 or i==n-1 and j!=n-1 or j==n-1 and i!=0 and i!=n//2 and i!=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


* * * * * * * *   
*               * 
*               * 
*               * 
* * * * * * * *   
*               * 
*               * 
*               * 
* * * * * * * *   

'''

#C
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 and j!=0 or j==0 and i!=0 and i!=n-1 or i==n-1 and j!=0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

  * * * * * * 
*             
*             
*             
*             
*             
  * * * * * * 
'''


#D
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 and j!=n-1 and j!=n-2 or i==n-1 and j!=n-1 and j!=n-2 or j==n-1 and i==n//2 or j==n-2 and i!=0 and i!=n//2 and i!=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')
* * *     
*     *   
*       * 
*     *   
* * *     
'''

#E
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 and j!=0 or i==n//2 or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


* * * * * * * 
*             
*             
* * * * * * * 
*             
*             
* * * * * * *


'''
#F
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 and j!=0 or i==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')
    
* * * * * * * 
*             
*             
* * * * * * * 
*             
*             
*


'''

#G shape
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if (i==0 and j!=0) or (j==0 and i!=0 and i!=n-1) or (i==n-1 and j!=0 and j!=n-1) or (j==n-1 and i!=n-1 and i>=n//2) or (i==n//2 and j>=n//2):
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')



  * * * * * * 
*             
*             
*     * * * * 
*           * 
*           * 
  * * * * *   
'''

#H
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==n//2 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


*           * 
*           * 
*           * 
* * * * * * * 
*           * 
*           * 
*           * 

'''
#I
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


      *       
      *       
      *       
      *       
      *       
      *       
      *       
'''
#J
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==n//2 and i!=n-1 or i==n-1 and j<=n//2 and j!=0 or j==0 and i>=n//2 and i!=n-1 or i==0 and j!=0 and j!=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

    
  * * *   
    *     
*   *     
*   *     
  * *     

'''

#K
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==n//2 or i==j and i>=n//2 or i+j==n-1 and j>=n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

      *     * 
      *   *   
      * *     
      *       
      * *     
      *   *   
      *     * 
'''


#L shape
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==n-1 or j==0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


*             
*             
*             
*             
*             
*             
* * * *
'''


#M
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==j and j<=n//2 or i+j==n-1 and i<=n//2 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

*           * 
* *       * * 
*   *   *   * 
*     *     * 
*           * 
*           * 
*           * 

'''


#N
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==j or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


*           * 
* *         * 
*   *       * 
*     *     * 
*       *   * 
*         * * 
*           * 

'''

#O
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 and i!=0 and i!=n-1 or i==n-1 and j!=n-1 and j!=0 or i==0 and j!=0 and j!=n-1 or j==n-1 and i!=n-1 and i!=0:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')
    
  * * *   
*       * 
*       * 
*       * 
  * * *

  '''
#P
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 and j!=n-1 or j==n-1 and i<=n//2 and i!=0 and i!=n//2 or i==n//2 and j!=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * * * * *   
*           * 
*           * 
* * * * * *   
*             
*             
*             
'''

#Q
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 and j!=0 and j!=n-1 or j==0 and i!=0 and i!=n-1 or i==n-1 and j<=n//2 and j!=0 and j!=n-1 or j==n-1 and i<=n//2 and i!=0 and i!=n-1 or i==j and j>=n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')


  * * * * *   
*           * 
*           * 
*     *     * 
*       *     
*         *   
  * * *     * 
'''

#R
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i==0 and j!=n-1 or j==n-1 and i<=n//2 and i!=0 and i!=n//2 or i==n//2 and j!=n-1 or i==j and j>=n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * * * * *   
*           * 
*           * 
* * * * * *   
*       *     
*         *   
*           * 

'''


#S
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 and j!=0 or j==0 and i<=n//2 and i!=0 and i!=n//2 or i==n//2 and j!=n-1 and j!=0 or j==n-1 and i>=n//2 and i!=n-1 or i==n-1 and j!=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

  * * * * 
*         
  * * * * 
        * 
* * * *   
'''

#T
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 or j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * * * * * * 
      *       
      *       
      *       
      *       
      *       
      *       
'''


#U
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 and i!=n-1 or i==n-1 and j!=0 and j!=n-1 or j==n-1 and i!=n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

*       * 
*       * 
*       * 
*       * 
  * * *

  '''

#V
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i+j==n+n//2-1 or i-j==n//2:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

              
*           * 
  *       *   
    *   *     
      *       

'''
#W
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if j==0 or i+j==n-1 and i>=n//2 or i==j and i>=n//2 or j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

*           * 
*           * 
*           * 
*     *     * 
*   *   *   * 
* *       * * 
*           * 

'''

#X
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==j or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

*           * 
  *       *   
    *   *     
      *       
    *   *     
  *       *   
*           *

'''

#Y
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==j and j<=n//2 or i+j==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

*           * 
  *       *   
    *   *     
      *       
    *         
  *           
*             

'''

#Z
'''n=int(input("Enter a number"))
for i in range(n):
    for j in range(n):
        if i==0 or i+j==n-1 or i==n-1:
            print("*",end=' ')
        else:
            print(" ",end=' ')
    print('')

* * * * * * * 
          *   
        *     
      *       
    *         
  *           
* * * * * * * 
'''
