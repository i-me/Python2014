#-*- Coding:latin-8 -*-
a,b,c,n=0,1,0,0
while(n<50):
    a,b,n=b,c,(n+1)
    c=(a+b)
    print("#", n, ":", a, "-", b, "-", c)
   
