def p(n): return n>1 and all(n%i for i in range(2,n))
print(p(7))