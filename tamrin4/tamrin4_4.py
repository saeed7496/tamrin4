
def isfactoril(n):
    s=1
    for i in range(1,n+1):
        s=i*s
        if s==n:
            print('yes')
            break
        elif i == n:
            print('no')
            
isfactoril(124)       