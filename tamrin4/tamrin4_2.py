
def mull_table(n,m):
  
    for i in range(1,n+1):
        for j in range(1,m+1):
            print(repr(i*j).ljust(3,' '),end=' ')
        print('')
mull_table(4, 10)
