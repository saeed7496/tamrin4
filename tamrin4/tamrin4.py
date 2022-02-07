m=int(input('tedad stoon: '))
n=int(input('tedad satr: '))
for i in range(n):
    if i%2==0:
        for j in range(m):
            if j%2==0:
                print('*',end=' ')
            else:
                print('#',end=' ')
        print('')
    else:
        for j in range(m):
            if j%2==0:
                print('#',end=' ')
            else:
                print('*',end=' ')
        print('')