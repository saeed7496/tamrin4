def b_m_m(a, b):
    m=min(a, b)
    n=max(a, b)
    for j in range(m, 0, -1):
        if  m%j==0 and n%j==0:
            print(j)
            break   
b_m_m(13, 12)






