
def k_m_m(a,b):
    m=max(a, b)
    n=min(a,b)
    for i in range(1,m+1):
        if (i*n) % m==0:
            print(i*n)
            break
k_m_m(4,8)

