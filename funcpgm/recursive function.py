'''def recursion(n):
    if n<=1:
        return n
    else:
        return n+recursion(n-1)
s=recursion(5)
print(s)
'''
def recursion(n):
    if n==10:
        return 1
    else:
        return n+recursion(n+1)
s=recursion(5)
print(s)
